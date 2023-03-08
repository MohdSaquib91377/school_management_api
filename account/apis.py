from rest_framework.response import Response
from rest_framework.views import APIView
from account import services as account_services

class SchoolSignupView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            status, data = account_services.UserSignupService.validate_signup_payload(request.data)
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)
        
class SchoolLoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            status, data = account_services.UserLoginService.validate_login_payload(request.data)
            return Response({"status": status, "msg": data}, status=status)
        except Exception as e:
            status, data = 400, f"{e}"
            return Response({"status": status, "msg": data}, status=status)
