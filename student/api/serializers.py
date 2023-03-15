from rest_framework import serializers
from student import models as student_models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_models.Student
        fields = ["name","username","password","grade"]
        extra_kwargs = {"name": {"required": False, "allow_null": True}}



class StudentsListSerializer(serializers.ListSerializer):
    child = StudentSerializer()

    def validate(self, data):
        """
        Validate each student in the list.
        """
        for student in data:
            StudentSerializer(data=student).is_valid(raise_exception=True)
        return data
    
    
class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_models.Student
        fields = ["username","password"]