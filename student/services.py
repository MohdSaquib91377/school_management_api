
from school import services as school_services
from student.api import serializers as student_serializers
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


class StudentAuthService:
    def validate_login_payload(payaload): 
        serializer = student_serializers.StudentLoginSerializer(data = payaload)
        if serializer.is_valid():
            status = student_query.StudentAuthHandler.validate_by_username_and_password(serializer.validated_data["username"], serializer.validated_data["password"])
            if not status:
                return 400, "invalid credentials"

                
            return 200, 'login successfully'
        return 400, serializer.errors