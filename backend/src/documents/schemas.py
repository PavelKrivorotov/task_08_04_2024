import typing
import uuid
import datetime
import decimal

from pydantic import BaseModel, ConfigDict
from pydantic import model_serializer


class WordRetrieve(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    word: str
    tf: decimal.Decimal
    idf: decimal.Decimal

    @model_serializer
    def serializer(self) -> dict[str, typing.Any]:
        return {
            'word': self.word,
            'tf': float(self.tf),
            'idf': float(self.idf)
        }
    

class DocumentRetrieve(BaseModel):
    words: list[WordRetrieve] = []

    @model_serializer
    def serializer(self) -> list[WordRetrieve]:
        return self.words


class DocumentSingl(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID = None
    title: str = None
    published: datetime.datetime = None
    count_words: int = None

    def convrt_id(self) -> typing.Union[str, None]:
        return str(self.id) if self.id is not None else None
    
    def convert_title(self) -> typing.Union[str, None]:
        return self.title if self.title is not None else None
    
    def convert_published(self) -> typing.Union[str, None]:
        if self.published is None:
            return None
        return self.published.strftime('%Y-%m-%d %H:%M:%S')
    
    def convert_count_words(self) -> typing.Union[int , None]:
        return int(self.count_words) if self.count_words is not None else None

    @model_serializer
    def serializer(self) -> dict[str, typing.Any]:
        return {
            'id': self.convrt_id(),
            'title': self.convert_title(),
            'published': self.convert_published(),
            'count_words': self.convert_count_words(),
        }


class DocumentList(BaseModel):
    docs: list[DocumentSingl]

    @model_serializer
    def serializer(self) -> list[DocumentSingl]:
        return self.docs

