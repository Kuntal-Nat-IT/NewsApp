# from django.db import models
from djongo import models


class AdminProfile(models.Model):
    uni_id = models.TextField(default="12345")
    firstname = models.TextField(default="Admin")
    lastname = models.TextField(default="Admin")
    email = models.EmailField(default="admin@gmail.com")
    password = models.TextField(default="12345")
    aboutadmin = models.TextField(default="About Admin")
    adminimage = models.ImageField(upload_to='Image/AdminImage/', default="https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80")

    def __str__(self):
        return self.email