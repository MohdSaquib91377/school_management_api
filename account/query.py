from account import models as account_models
from django.contrib.auth import authenticate
class SchoolSignupHandler:

    @classmethod
    def create_single_user(cls, payload):
        account_models.User.objects.create(**payload)
    

class SchoolLoginHandler:
    @classmethod
    def is_authenticate_user(cls, email, password):
        user = authenticate(email=email, password=password)
        if user:
            return user
        return None