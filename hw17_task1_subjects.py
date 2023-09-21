import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

db_password = os.getenv("DB_PASSWORD")

DATABASE_URI = f'postgresql://postgres:{db_password}@localhost:5432/studentsdb'

engine = create_engine(DATABASE_URI)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)


subjects = ['English', 'Math', 'History', 'Spanish']

for s in subjects:
    subj_name = Subject(name=s)
    session.add(subj_name)

session.commit()
