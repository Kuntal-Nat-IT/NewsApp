from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from NewsApp.models import UserDetail
from rest_framework import serializers
from NewsApp.models import UserDetail
from django.contrib.auth.models import User
from datetime import datetime, timezone
from NewsApp.utils import isEmail, OTP_LENGTH, OTP_TIMEOUT,sendMailOtp



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

    def validate(self, data):
        if data['email'] == '':
            raise serializers.ValidationError('Empty phone number')
            if isEmail(data['email']):
                try:
                    account = UserDetail.objects.get(email=data['email'])
                    raise serializers.ValidationError('Account already exists')
                except UserDetail.DoesNotExist:
                    pass
                otp = sendMailOtp(account.email)
                if otp:
                    data['otp'] = otp
                else:
                    raise serializers.ValidationError('Could not send otp to mail')
            else:
                raise serializers.ValidationError('Invalid phone number')
        return data

    def validate_email(self, data):
        email = data.strip()
        if isEmail(email):
            return email
        else:
            raise serializers.ValidationError('Not a valid email')
    
    