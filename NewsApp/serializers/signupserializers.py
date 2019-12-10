from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from ..models import UserDetail


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['fullname', 'email', 'username', 'password', 'userimage']
    
    def validate_fullname(self, fullname):
        return fullname
    
    def validate_fullname(self, email):
        return email
    
    def validate_fullname(self, username):
        return username
    
    def validate_fullname(self, password):
        return password
    
    def validate_fullname(self, userimage):
        return userimage