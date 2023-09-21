import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, insert
from sqlalchemy.orm import declarative_base, sessionmaker
import random

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


class StudentSubject(Base):
    __tablename__ = 'student_subject'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)


students = session.query(Base.metadata.tables['students']).all()
subjects = session.query(Base.metadata.tables['subjects']).all()

for student in students:
    assigned_subject = random.choice(subjects)

    session.execute(
        insert(Base.metadata.tables['student_subject']).values(
            student_id=student[0],
            subject_id=assigned_subject[0]
        )
    )

session.commit()
