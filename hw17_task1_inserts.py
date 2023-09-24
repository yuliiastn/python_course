import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from random import randint, choice
from hw17_task1_models import Student, Subject, StudentSubject


db_password = os.getenv("DB_PASSWORD")

DATABASE_URI = f'postgresql://postgres:{db_password}@localhost:5432/studentsdb'

engine = create_engine(DATABASE_URI)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Populating 'students' table
random_names = ['Joe', 'Winston', 'Benedict', 'Andrea', 'Fillipe', 'Iria', 'Eric', 'Joan', 'Pablo', 'Brian', 'Timothy', 'Lee']

for _ in range(10):
    student = Student(name=choice(random_names), age=randint(18, 25))
    session.add(student)

# Populating 'subjects' table
subjects = ['English', 'Math', 'History', 'Spanish']

for s in subjects:
    subj_name = Subject(name=s)
    session.add(subj_name)

# Populating 'student_subject' table
students = session.query(Student).all()
subjects = session.query(Subject).all()

for student in students:
    assigned_subject = choice(subjects)

    student_subject = StudentSubject(student_id=student.id, subject_id=assigned_subject.id)
    session.add(student_subject)

session.commit()
