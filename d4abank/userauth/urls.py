from django.urls import path
from userauth import views


urlpatterns = [
    path('register/', views.RegisterView , name='register'),
]