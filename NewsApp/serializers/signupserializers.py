from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from ..models import UserDetail


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['fullname', 'email', 'username', 'userimage']
    
    def validate_fullname(self, fullname):
        return fullname
    
    def validate_email(self, email):
        return email
    
    def validate_username(self, username):
        return username
    
    def validate_usrimage(self, password):
        return password
    
    