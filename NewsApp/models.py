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
    userphone = models.BigIntegerField(default="9292929292")
    useraddress = models.TextField(default="Adress ...")
    aboutuser = models.TextField(default="About Me ...")
    activeuser = models.BooleanField(default=True)

    def __str__(self):
        return self.email 
   

class UserSessionTable(models.Model):
    fullname = models.CharField(max_length=30, default="User")
    useriamge = models.TextField(default="/home/Image")
    uni_id = models.TextField(default="abcd1234", unique="True")
    user_email = models.EmailField(default="a@b.com")
    session_value = models.TextField(default="123abc")
    session_start_date = models.DateTimeField(auto_now_add=True)
    session_end_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email


class ArticleReader(models.Model):
    articleid = models.TextField(default="123")
    image = models.ImageField(upload_to="Image/ArticleImage")
   # image2 = models.ImageField(upload_to="Image/ArticleImage")
   # image3 = models.ImageField(upload_to="Image/ArticleImage")
   # Image4 = models.ImageField(upload_to="Image/ArticleImage")
   # Image5 = models.ImageField(upload_to="Image/ArticleImage")
    heading = models.TextField(default="ABCD")
    body = models.TextField(default="XYZ")
    categories = models.TextField(default="default")
    createdOn = models.DateTimeField(auto_now_add=True)


#     # class Meta:
#     #     verbose_name_plural = 'Article of users'

    def __str__(self):
        return self.articleid   