'''
        view.py
   @ Author  Kuntal & Sudipto
   @ Company Nat It Solved Pvt Ltd
   @ version  0.1
   @date      10/12/2019
'''

from django.shortcuts import render
from .import models
from .import helpPackage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
import datetime
from datetime import date

# Serializers
from .serializers import signupserializers

# Rest Framework
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def LoginApi(request):
        if request.method == 'POST':
                try:
                        usrname = request.POST['usrname']
                        psw = request.POST['psw']
                        uobj = models.UserCredentials.objects.get(email=usrname)
                        data = {"success": True}
                        return JsonResponse(data)
                        # return Response("Okay", status=status.HTTP_200_OK)

                except Exception as e:
                        print("LoginApi", e)
                        return Response("Key-Value Error", status=status.HTTP_400_BAD_REQUEST)
        
        else:
                return Response("Not Okay", status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def RegisterApi(request):
        if request.method == 'POST':
                try:
                        serializerObj = signupserializers.RegisterSerializer(data=request.data)
                        if serializerObj.is_valid():
                                serializerObj.save()
                                try:
                                        UsrDetailsObj = models.UserDetail.objects.get(email=request.POST['email'])
                                        usrmail = UsrDetailsObj.email
                                        usrname = UsrDetailsObj.username
                                        usrpass = UsrDetailsObj.password
                                        usr_uni_id = helpPackage.HideMyData(usrmail)
                                        uobj = models.UserCredentials(email=usrmail,username=usrname,password=usrpass,uni_id=usr_uni_id)
                                        uobj.save()
                                        return Response("Okay", status=status.HTTP_200_OK)

                                except Exception as e:
                                        print(e)
                                        return Response("Not Okay", status=status.HTTP_503_SERVICE_UNAVAILABLE)

                        else:
                                return Response("Invalid Data", status=status.HTTP_406_NOT_ACCEPTABLE)

                except Exception as e:
                        print("RegisterApi", e)
                        return Response("Key-Value Error", status=status.HTTP_400_BAD_REQUEST)
        
        else:
                return Response("Not Okay", status=status.HTTP_400_BAD_REQUEST)
