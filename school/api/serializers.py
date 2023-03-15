from rest_framework import serializers
from school import models as school_models

class SchoolSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = school_models.School
        fields = ["email","name","city","pin_code","password"]


class SchoolLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()