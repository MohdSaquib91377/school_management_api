from django.urls import path
from account import apis as account_apis
urlpatterns = [
    path('signup/',account_apis.SchoolSignupView.as_view()),
    path('login/',account_apis.SchoolLoginView.as_view()),

]