from django.urls import path
from student import apis as student_apis
urlpatterns = [
    path('',student_apis.StudentView.as_view()),
    path('<student_id>/',student_apis.StudentDetailsView.as_view()), 
    path('filter/<grade>/',student_apis.StudentFilterView.as_view()),


]