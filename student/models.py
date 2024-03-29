from django.db import models
from school import models as school_models
# Create your models here.

class Grade(school_models.TimeStampModel):
    GRADE_TYPE_CHOICES = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),

    )
    grade = models.CharField(choices=GRADE_TYPE_CHOICES, max_length=16, default="12")


    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f"{self.grade}"
    

class Student(school_models.TimeStampModel):
    grade = models.ForeignKey(Grade, related_name="students",on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=64,null=True, blank=True)
    password = models.CharField(max_length=128)
    
    class Meta:
        ordering = ("-created_at",)

    
    def __str__(self) -> str:
        return f"{self.name}"