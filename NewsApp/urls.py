from django.urls import path
from .import views


urlpatterns = [
    path('login/', views.LoginApi, name="loginapi"),
    path('register/', views.RegisterApi, name="register"),
]