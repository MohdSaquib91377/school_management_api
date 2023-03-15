from student import models as student_models
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256


class StudentHandler:

    @classmethod
    def create_bulk_student(cls, payload: list):
        students_obj = []
        for student in payload:
            students_obj.append(student_models.Student(
                name=student.get('name'),
                username=student.get('username'), 
                password=make_password(student.get('password')),
                grade=student.get("grade")
            ))

        student_models.Student.objects.bulk_create(
            students_obj
        )

    @classmethod
    def get_all_students(cls):
        return student_models.Student.objects.all()
    
    @classmethod
    def get_students_by_grade(cls, grade):
        return student_models.Student.objects.filter(grade_id=grade)

    @classmethod
    def get_students_by_id(cls, student_id):
        return student_models.Student.objects.filter(id = student_id).first()

class StudentAuthHandler:
    @classmethod
    def validate_by_username_and_password(cls, username, password):
        hash = make_password(password)
        student = student_models.Student.objects.filter(username = username).first()
        if student:
            return django_pbkdf2_sha256.verify(password, hash)
        return False    