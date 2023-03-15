from rest_framework.response import Response
from rest_framework.views import APIView
from school import services as school_services

class configSignupView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            status, data = school_services.SchoolSignupService.validate_signup_payload(request.data)
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)
        
class configLoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            status, data = school_services.SchoolLoginService.validate_login_payload(request.data)
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)
