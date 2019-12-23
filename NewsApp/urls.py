from django.urls import path
from .import views


urlpatterns = [
    path('login/', views.LoginApi, name="loginapi"),
    path('register/', views.RegisterApi, name="register"),
    path('checksession/', views.CheckUserSession, name="checksession"),
    path('forgot-password/', views.ForgetPasswordRequest, name="forgotpasswoedreq"),
    path('check/forget/password/session/', views.ForgotPasswordSession, name="checkForgetPasswordSession"),
    path('check/OTP/',views.CheckUserOPT, name="optcheck"),
    path('set-new-password/', views.SetNewPassword, name="setnewpasswordurl"),
    path('logout/', views.EndUserSession, name="logout")
]