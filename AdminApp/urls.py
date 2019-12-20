from django.urls import path
from .import views


urlpatterns = [
   path('', views.Dashboard, name="admindashboard"),
   path('login/',views.Login,name="adminlogin"),
   path('login/submit', views.Logincontroler, name="loginsubmit"),
   path('logout/', views.Logout, name="logout"),
   path('register/',views.Register,name="adminregister"),
   path('profile/',views.Profile,name="adminprofile"),
   path('chnage-password/', views.AdminChangePassword, name="changepassword"),
   path('edit-profile/', views.EditProfileData, name="editprofile"),
   path('userlist/', views.ShowAllUserList, name="showuserlist"),
   path('user-profile/<slug:slug>/', views.ShowUserProfileData, name="showUserProfile"),
   path('logged-in-userlist/', views.ShowLoggedInUser, name="allloggedinuser"),
]