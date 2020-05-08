import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float, String
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
    engine = create_engine(url)


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

    session = sessionmaker(bind=engine)()


define_model('menu')


def create_record(new_name, new_score, new_stars):
    """
    Create new record.
    """
    new_subject = Subject(
        name = new_name,
        score = new_score,
        stars = new_stars
    )
    session.add(new_subject)
    session.commit()


# create_record("database", 77.7, 7)
create_record("security", 88.8, 8)


def read_table():
    """
    Read table.
    """
    subjects = session.query(Subject).all()

    subject = subjects[0]

    for subject in subjects:
        print(
          subject.name,
          subject.score,
          subject.stars
        )


read_table()


# Disconnect DB
session.close()
