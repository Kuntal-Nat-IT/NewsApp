# from django.db import models
from djongo import models


class UserCredentials(models.Model):
    email = models.EmailField(primary_key="True")
    username = models.TextField(max_length=20, unique="True")
    password = models.TextField(default="12345")
    uni_id = models.TextField(default="abcd1234", unique="True")

    def __str__(self):
        return self.email


class UserDetail(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField(primary_key="True")
    username = models.TextField(max_length=20, unique="True")
    userimage = models.ImageField(upload_to='Image/UserImage/')
    usercreated = models.DateTimeField(auto_now_add=True)
    lastlogin = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email 
   

class UserSessionTable(models.Model):
    user_email = models.EmailField(default="a@b.com")
    session_value = models.TextField(default="123abc")
    session_start_date = models.DateTimeField(auto_now_add=True)
    session_end_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usr_uni_id

    