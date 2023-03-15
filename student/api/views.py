from rest_framework.response import Response
from rest_framework.views import APIView
from student import services as student_services
from rest_framework import permissions
from student import permisions as student_permisions

class StudentView(APIView):
    permission_classes = [student_permisions.configOnlyPermission]
    def post(self, request, *args, **kwargs):
        try:
            status, data = student_services.StudentService.validate_post_payload(request.data)
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)

    def get(self, request, *args, **kwargs):
        try:
            status, data = student_services.StudentService.get_students()
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)
    
   
        
class StudentFilterView(APIView):
    permission_classes = [student_permisions.configOnlyPermission]
    def get(self, request,grade, *args, **kwargs):
        try:
            status, data = student_services.StudentService.get_students_by_grade(grade)
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)

class StudentDetailsView(APIView):
    permission_classes = [permissions.AllowAny]
    def patch(self, request, student_id,*args, **kwargs):
        try:
            status, data = student_services.StudentService.validate_patch_payload(request.data,student_id)
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)


class StudentLoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            status, data = student_services.StudentAuthService.validate_login_payload(request.data)

        except Exception as e:
            status, data = 400, f"{e}"

        finally:
            return Response({"status":status,"message":data}, status=status)