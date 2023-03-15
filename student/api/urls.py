from django.urls import path
from student.api import views as student_views
urlpatterns = [
    path('',student_views.StudentView.as_view()),
    path('<student_id>/',student_views.StudentDetailsView.as_view()), 
    path('filter/<grade>/',student_views.StudentFilterView.as_view()),
    path('account/login/',student_views.StudentLoginView.as_view()),



]