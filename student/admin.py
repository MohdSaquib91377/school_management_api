from django.contrib import admin
from student import models as student_models

# Register your models here.


admin.site.register(student_models.Grade)
admin.site.register(student_models.Student)
