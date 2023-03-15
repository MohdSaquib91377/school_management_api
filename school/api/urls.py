from django.urls import path
from school.api import views as school_views
urlpatterns = [
    path('signup/',school_views.configSignupView.as_view()),
    path('login/',school_views.configLoginView.as_view()),

]