from django.contrib import admin
from .models import UserCredentials, UserDetail

admin.site.register(UserCredentials)
admin.site.register(UserDetail)