import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float, String, desc
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def connect_db(db):
    """
    Connecting MySQL database, and generate Engine.
        Engine(mysql://root:***@localhost/mydb_test)
    """
    global engine

    url = URL(
        drivername = 'mysql',
        username = 'root',
        password = '',
        host = 'localhost',
        database = db
    )
    engine = create_engine(url, encoding="utf-8")


connect_db('mydb_test')


def define_model(tb):
    """
    Define model, and generate Session.

    DB Columns
        | id | name | score | stars |
    """
    global Subject, session

    Base = declarative_base()

    class Subject(Base):
        __tablename__ = tb

        id = Column(Integer, primary_key=True)
        name = Column(String)
        score = Column(Float)
        stars = Column(Integer)

    session = sessionmaker(autocommit=False, bind=engine)()


define_model('menu')
