import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, aliased
from hw17_task1_models import Student, Subject, StudentSubject

db_password = os.getenv("DB_PASSWORD")
DATABASE_URI = f'postgresql://postgres:{db_password}@localhost:5432/studentsdb'

engine = create_engine(DATABASE_URI)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

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
