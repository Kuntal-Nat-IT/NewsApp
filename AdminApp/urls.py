from django.urls import path
from .import views


urlpatterns = [
   path('', views.Demo, name=""),
   path('login/',views.login,name=""),
   path('register/',views.register,name=""),
]