
from account import services as account_services
from student import serializers as student_serializers
from student import query as student_query
class StudentService:

    @staticmethod
    def validate_post_payload(payload):
        serializer = student_serializers.StudentSerializer(data=payload, many=True)
        serializer.is_valid(raise_exception=True)
      
        student_query.StudentHandler.create_bulk_student(serializer.validated_data)
        return 200, "student created in bulk sucessfully"
    
    @staticmethod
    def get_students():
        students = student_query.StudentHandler.get_all_students()
        serializer = student_serializers.StudentSerializer(students, many=True)
        return 200, serializer.data
    
    @staticmethod
    def get_students_by_grade(grade):
        students = student_query.StudentHandler.get_students_by_grade(grade)
        serializer = student_serializers.StudentSerializer(students, many=True)
        return 200, serializer.data
    
    @staticmethod
    def validate_patch_payload(payload, student_id):
        student = student_query.StudentHandler.get_students_by_id(student_id)

        # Update the object with the request data
        serializer = student_serializers.StudentSerializer(student, data=payload, partial=True)
        if serializer.is_valid():
            serializer.save()
            return 200, f"records updated successfully"
        return 400, serializer.errors