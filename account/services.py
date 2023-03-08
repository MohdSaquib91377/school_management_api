
from account import serializers as account_serializers
from account import query as account_query
from django.contrib.auth.hashers import make_password

from service import jwt as service_jwt


class UserSignupService:

    @staticmethod
    def validate_signup_payload(payload: dict):
        serializer = account_serializers.SchoolSignupSerializer(payload)
        if serializer.is_valid():
           

            #TODO: hash password
            data["password"] = make_password(data["password"])
            
            
            account_query.SchoolSignupHandler.create_single_user(data)
            return 200, "school signup successful"
        
        status, data = 400, serializer.errors
        return status, data
    

class UserLoginService:
    @staticmethod
    def validate_login_payload(payload: dict):
        serializer = account_serializers.SchoolLoginSerializer(data = payload)
        if serializer.is_valid():
            #TODO: hash password
            data = serializer.validated_data
            user = account_query.SchoolLoginHandler.is_authenticate_user(data["email"], data["password"])
            if user is None:
                status,data = 400, "Invalid credentials"
                return status,data
            data = service_jwt.JWT.get_tokens_for_user(user)
            return 200, data
        return 400, serializer.errors
        
        