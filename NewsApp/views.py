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
                        if uobj.password == psw:
                                request.session['user_session'] = uobj.uni_id
                                return_val = CreateUserSession(uobj.email, request.session['user_session'])
                                if return_val:
                                        data = {"success": True}
                                        return JsonResponse(data)
                                else:
                                        data = {"success": False}
                                        return JsonResponse(data)
                        else:
                                data = {"success": False}
                                return JsonResponse(data)

                except Exception as e:
                        print("LoginApi", e)
                        data = {"success": False}
                        return JsonResponse(data)
        
        else:
                data = {"success": False}
                return JsonResponse(data)




@api_view(['POST'])
def RegisterApi(request):
        if request.method == 'POST':
                try:
                        usrpass = request.POST['password']
                        serializerObj = signupserializers.RegisterSerializer(data=request.data)
                        if serializerObj.is_valid():
                                serializerObj.save()
                                try:
                                        UsrDetailsObj = models.UserDetail.objects.get(email=request.POST['email'])
                                        usrmail = UsrDetailsObj.email
                                        usrname = UsrDetailsObj.username
                                        usrpass = usrpass
                                        usr_uni_id = helpPackage.HideMyData(usrmail)
                                        uobj = models.UserCredentials(email=usrmail,username=usrname,password=usrpass,uni_id=usr_uni_id)
                                        uobj.save()
                                        data = {"success": True}
                                        return JsonResponse(data)

                                except Exception as e:
                                        print(e)
                                        data = {"success": False}
                                        return JsonResponse(data)

                        else:
                                data = {"success": False}
                                return JsonResponse(data)

                except Exception as e:
                        print("RegisterApi", e)
                        data = {"success": False}
                        return JsonResponse(data)
        
        else:
                data = {"success": False}
                return JsonResponse(data)




# ----------------------------------------- Session Management ---------------------------------------
def CreateUserSession(mail, session_val):
        try:
                todayDate = datetime.datetime.now()
                session_obj = models.UserSessionTable(user_email=mail, session_value=session_val, \
                        session_start_date=todayDate, session_end_date=todayDate)
                session_obj.save()
                return True
        except Exception as e:
                print("Session Create Issue : ", e)
                return False


def CheckUserSession(request):
        try:
                user_session = request.session['user_session']
                data = {"loggedin": True}
                return JsonResponse(data)
        except Exception as e:
                print("Create Session Exception : ", e)
                data = {"loggedin": False}
                return JsonResponse(data)


def EndUserSession(request):
        try:
                user_session = request.session['user_session']
                del request.session['user_session']
                data = {"loggedin": True}
                return JsonResponse(data)
        except Exception as e:
                print("End Session Exception : ", e)
                data = {"loggedin": False}
                return JsonResponse(data)
