# from django.db import models
from djongo import models


class UserCredentials(models.Model):
    email = models.EmailField(default="a@b.com")
    username = models.TextField(max_length=20)
    password = models.TextField(default="12345")
    uni_id = models.TextField(default="abcd1234")

    def __str__(self):
        return self.email


class UserDetail(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField(default="a@abc.com")
    password = models.TextField(default="12345")
    userimage = models.ImageField(upload_to='Image/UserImage/')
    usercreated = models.DateTimeField(auto_now_add=True)
    lastlogin = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email 
   




    
    