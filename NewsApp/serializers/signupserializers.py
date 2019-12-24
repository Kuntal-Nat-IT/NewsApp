from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from ..models import UserDetail,ArticleReader


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
    

class ArticleReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleReader
        fields = ['articleid', 'image', 'heading' ,'body', 'categories', 'createdon']

        def validate_image(self,image):
            return image
        def validate_heading(self,heading):
            return heading
        def validate_body(self,body):
            return body
        def validate_categories(self,categories):
            return categories

        
    