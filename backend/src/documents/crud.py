import typing

from fastapi import UploadFile
from fastapi import HTTPException, status

from sqlalchemy import func
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from sqlalchemy import Result, Tuple

from documents.models import Word, Document, WordDocument
from documents.schemas import DocumentRetrieve, DocumentList, DocumentSingl
from documents.text_parser import TextParser
from documents.filters import Filter
from documents.response import make_response_content


class DocumentCRUD:
    def create(self, db: Session, file: UploadFile) -> dict[str, str]:
        objs = TextParser(file)

        # create document object
        document = Document(title=file.filename, count_words=objs.count)
        db.add(document)
        db.commit()
        db.refresh(document)

        # create or update words objects and create word-document relations
        for word, count in objs.words.items():        
            try:
                query = (
                    insert(Word)
                    .values(word=word)
                    .returning(Word.id)
                )
                word_id = db.execute(query).scalar()
                db.commit()

            except Exception:
                db.rollback()

                query = (
                    update(Word)
                    .where(Word.word == word)
                    .values(count_in_all_documents = Word.count_in_all_documents + 1)
                    .returning(Word.id)
                )
                word_id = db.execute(query).scalar()
                db.commit()

            finally:
                query = (
                    insert(WordDocument)
                    .values(
                        document_id=document.id,
                        word_id=word_id,
                        count_in_document=count
                    )
                )
                db.execute(query)
                db.commit()

        return {'id': str(document.id)}
    
    def retrieve(self, db: Session, id: str) -> dict[str, typing.Any]:
        res = db.get(Document, id)
        res_m = DocumentSingl.model_validate(res)
        return res_m.model_dump()
    
    def list(self, db: Session, filter: Filter) -> dict[str, typing.Any]:
        query = (
            select(Document)
            .order_by(Document.published.desc())
            .limit(filter.limit())
            .offset(filter.offset())
        )
        res = db.scalars(query).all()

        if filter.page != 1 and len(res) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        query = select(func.count(Document.id))
        count = db.scalar(query)

        res_m = DocumentList(docs=res).model_dump()
        return make_response_content(res_m, count)
    
    def delete(self, db: Session, id: str) -> None:
        query = (
            update(Word)
            .where(
                Word.id.in_(
                    select(Word.id)
                    .join_from(Word, WordDocument, Word.id == WordDocument.word_id)
                    .where(WordDocument.document_id == id)
                )
            )
            .values(count_in_all_documents = Word.count_in_all_documents - 1)
        )
        db.execute(query)

        query = delete(Word).where(Word.count_in_all_documents == 0)
        db.execute(query)

        query = delete(Document).where(Document.id == id)
        db.execute(query)
        
        db.commit()

    def list_words_of_document(
            self,
            db: Session,
            id: str,
            filter: Filter
        ) -> dict[str, typing.Any]:

        subquery = select(func.count(Document.id)).subquery()
        query = (
            select(
                (WordDocument.count_in_document / Document.count_words).label('tf'),
                Word.word.label('word'),
                (func.log(subquery.as_scalar() / Word.count_in_all_documents)).label('idf')
            )
            .join_from(Document, WordDocument, Document.id == WordDocument.document_id, isouter=True)
            .join_from(WordDocument, Word, WordDocument.word_id == Word.id, isouter=True)
            .where(Document.id == id)
            .order_by(
                func.log((subquery.as_scalar() / Word.count_in_all_documents)).desc(),

                # for uniqe result
                WordDocument.id,
            )
            .limit(filter.limit())
            .offset(filter.offset())
        )
        res = db.execute(query)
        res_l = _convert_words(res)

        if filter.page != 1 and len(res_l) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        query = (
            select(func.count(WordDocument.id))
            .where(WordDocument.document_id == id)
        )
        count = db.scalar(query)

        res_m = DocumentRetrieve(words=res_l).model_dump()
        return make_response_content(res_m, count)

document_crud = DocumentCRUD()


def _convert_words(result: Result[Tuple]) -> list[typing.Any]:
    words: list = []

    for tf, word, idf in result.columns('tf', 'word', 'idf').all():        
        if word is not None:
            words.append({
                'word': word,
                'tf': tf,
                'idf': idf
            })

    return words

