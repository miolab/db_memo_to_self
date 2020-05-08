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
# create_record("security", 88.8, 8)


def update_record(target_name, update_score):
    """
    Update record.
        e.g) update score
    """
    subject = session.query(Subject).filter(Subject.name == target_name).first()
    subject.score = update_score
    session.commit()


# update_record("database", 131.1)


def delete_record():
    """
    Delete record.
    """
    # -- DELETE FROM menu WHERE name = "hoge";
    # subject = session.query(Subject).filter(Subject.name == "security").delete()

    # -- DELETE FROM menu WHERE score > 131;
    subject = session.query(Subject).filter(Subject.score > 131).delete()

    session.commit()


# delete_record()


def read_table():
    """
    Read table.
    """
    # -- SELECT * FROM menu;
    subjects = session.query(Subject).all()
    # subject = subjects[0]    # NOT USE

    # -- SELECT name, score FROM menu;
    # subjects = session.query(Subject.name, Subject.score).all()

    # -- SELECT name FROM menu WHERE name = "math";
    # subjects = session.query(Subject).filter(Subject.name == "math").all()

    # -- SELECT * FROM menu ORDER BY score DESC LIMIT 3;
    # subjects = session.query(Subject).order_by(desc(Subject.score)).limit(3).all()

    for subject in subjects:
        print(
          subject.name,
          subject.score,
          subject.stars
        )


# read_table()


# SQL execute directly
sql = "select * from menu order by stars desc limit 1"
subjects = session.execute(sql)
for subject in subjects:
    print(
      subject.name,
      subject.score,
      subject.stars
    )


# Disconnect DB
session.close()
