import uuid
import datetime

from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy import Uuid, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from main.databse import Base


class Word(Base):
    __tablename__ = 'words'

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    word: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    count_in_all_documents: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False
    )

    documents = relationship('WordDocument')


class Document(Base):
    __tablename__ = 'documents'

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    count_words: Mapped[int] = mapped_column(
      Integer,
      nullable=False
    )

    published: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    words = relationship('WordDocument')


class WordDocument(Base):
    __tablename__ = 'word_document'

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('documents.id', ondelete='CASCADE'),
        index=True,
        nullable=False
    )
    word_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('words.id', ondelete='CASCADE'),
        index=True,
        nullable=False
    )
    count_in_document: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

