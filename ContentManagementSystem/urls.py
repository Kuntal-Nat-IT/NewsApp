from django.urls import path
from django.conf.urls import url



app_name = 'ContentManagementSystem' 
 
urlpatterns =[
    url(r'^faq/',views.faq,name='faq'),