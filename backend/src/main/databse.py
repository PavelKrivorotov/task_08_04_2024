from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy import URL

from . import settings


url = URL.create(
    drivername=settings.DATABASE['MIDDLWARE'],
    username=settings.DATABASE['USER'],
    password=settings.DATABASE['PASSWORD'],
    database=settings.DATABASE['NAME'],
    host=settings.DATABASE['HOST'],
    port=settings.DATABASE['PORT']
)

engine = create_engine(
    url=url,
    # echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


class Base(DeclarativeBase):
    pass


def get_connect():
    connect = SessionLocal()
    try:
        yield connect
    finally:
        connect.close()

