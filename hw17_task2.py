import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, aliased

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


ss = aliased(StudentSubject)

english_students = (
    session.query(Student.name)
    .join(ss, Student.id == ss.student_id)
    .join(Subject, ss.subject_id == Subject.id)
    .filter(Subject.id == 1)
    .all()
)

english_student_names = [student.name for student in english_students]

print(english_student_names)


session.commit()
