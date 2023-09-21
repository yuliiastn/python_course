import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from random import randint, choice

db_password = os.getenv("DB_PASSWORD")

DATABASE_URI = f'postgresql://postgres:{db_password}@localhost:5432/studentsdb'

engine = create_engine(DATABASE_URI)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


random_names = ['Joe', 'Winston', 'Benedict', 'Andrea', 'Fillipe', 'Iria', 'Eric', 'Joan', 'Pablo', 'Brian', 'Timothy', 'Lee']

for _ in range(10):
    student = Student(name=choice(random_names), age=randint(18, 25))
    session.add(student)


session.commit()
