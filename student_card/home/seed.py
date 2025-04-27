from .models import Student, Marks, Department, Subject
from faker import Faker
import random
from django.db.models import *

fake = Faker()

def fakefeed(n=10) -> None:
    try:
        for i in range(n):
            departments = Department.objects.all()
            randon_index = random.randint(0, len(departments)-1)
            randon_dep = departments[randon_index]
            Student.objects.create(
                department = randon_dep,
                std_id = f'STD-{random.randint(101, 999)}',
                std_name = fake.name(),
                std_age = random.randint(18, 30)
            )
        print(f'{n} records feeded successfully')
    except Exception as e:
        print(e)



# Define a function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Fetch all students and subjects
def feedmarks() -> None:

    students = Student.objects.all()
    subjects = Subject.objects.all()

    # Insert marks for each student in each subject
    marks_list = []
    for student in students:
        for subject in subjects:
            marks = random.uniform(40, 100)  # Generate random marks between 40 and 100
            grade = calculate_grade(marks)

            marks_list.append(
                Marks(student=student, subject=subject, marks=marks, grade=grade)
            )

    # Bulk insert for performance
    Marks.objects.bulk_create(marks_list)

    print("Marks added successfully for all students.")


def round_marks() -> None:
    try:
        for mark in Marks.objects.all():
            mark.marks = round(mark.marks, 2)  # Round to 2 decimal places
            mark.save()
        print('Marks rounded')
    except:
        print('Error')

    