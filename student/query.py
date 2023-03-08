from student import models as student_models


class StudentHandler:

    @classmethod
    def create_bulk_student(cls, payload: list):
        students_obj = []
        for student in payload:
            students_obj.append(student_models.Student(
                name=student.get('name'),
                username=student.get('username'), password=student.get('password'),
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