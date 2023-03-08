from rest_framework import serializers
from account import models as account_models

class SchoolSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = account_models.User
        fields = ["email","name","city","pin_code","password"]


class SchoolLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()