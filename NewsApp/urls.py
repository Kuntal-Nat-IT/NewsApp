from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('login/', views.LoginApi, name="loginapi"),
    path('register/', views.RegisterApi, name="register"),
    path('forgotPassword/', views.ForgotPassword.as_view()),
    path('sendVerificationEmail/', views.SendVerificationEmail.as_view()),
    path('verifyEmail/<str:usernameb64>/', views.VerifyEmail.as_view(), name='verifyEmail'),
]