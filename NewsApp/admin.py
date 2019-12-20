from django.contrib import admin
from .models import UserCredentials, UserDetail, UserSessionTable

admin.site.register(UserCredentials)
admin.site.register(UserDetail)
admin.site.register(UserSessionTable)