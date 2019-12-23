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
        try:
                request.session['user_session']
                data = {"success": True}

        except Exception as e:
                if request.method == 'POST':
                        try:
                                usrname = request.POST['usrname']
                                psw = request.POST['psw']
                                uobj = models.UserCredentials.objects.get(email=usrname)
                                if uobj.password == psw:
                                        try:
                                                request.session['user_session'] = uobj.uni_id
                                                data = {"success": True}

                                        except Exception as e:
                                                print("Session Error : ", e)
                                                data = {"success": False}

                                        # return_val = CreateUserSession(uobj.email, request.session['user_session'])
                                        # if return_val:
                                        #         data = {"success": True}
                                        # else:
                                        #         data = {"success": False}

                                else:
                                        data = {"success": False}

                        except Exception as e:
                                print("LoginApi", e)
                                data = {"success": False}
                
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

                                except Exception as e:
                                        print(e)
                                        data = {"success": False}

                        else:
                                data = {"success": False}

                except Exception as e:
                        print("RegisterApi", e)
                        data = {"success": False}
        
        else:
                data = {"success": False}
        
        return JsonResponse(data)




# ---------------------------------------- Forgot Password -----------------------------------------

@api_view(['POST'])
def ForgetPasswordRequest(request):
        try:
                usrname = request.POST['usrname']
                request.session['forgetpsw'] = usrname
                # Send OTP to USER
                data = {"success": True}

        except Exception as e:
                data = {"success": False}
        
        return JsonResponse(data)


def ForgotPasswordSession(request):
        try:
                usrname = request.session['forgetpsw']
                data = {"user": True}

        except Exception as e:
                data = {"user": True}
        
        return JsonResponse(data)


@api_view(['POST'])
def CheckUserOPT(request):
        try:
                usrotp = request.POST['usrotp']
                if int(usrotp) == 1234:
                        data = {"success": True}
                else:
                        data = {"success": False}
        
        except Exception as e:
                data = {"success": False}
        
        return JsonResponse(data)


@api_view(['POST'])
def SetNewPassword(request):
        try:
                psw1 = request.POST['psw1']
                psw2 = request.POST['psw2']
                # logic 
                data = {"success": True}

        except Exception as e:
                data = {"success": False}
        
        return JsonResponse(data)

# --------------------------------------------------------------------------------------------------




# ----------------------------------------- Session Management ---------------------------------------
def CreateUserSession(mail, session_val):
        try:    
                # Fetching Data from UserDetails Table media/Image/UserImage/images.jpeg
                usrDetailObj = models.UserDetail.objects.get(email=mail)
                todayDate = datetime.datetime.now()

                fullname = usrDetailObj.fullname
                useriamge = usrDetailObj.userimage.url
                uni_id = helpPackage.HideMyData(mail)
                user_email = mail
                session_value = session_val
                session_start_date = todayDate
                session_end_date = todayDate

                # Creating Session Table
                session_obj = models.UserSessionTable(fullname=fullname, useriamge=useriamge, uni_id=uni_id, \
                        user_email=user_email, session_value=session_value)
                session_obj.save()
                return True

        except Exception as e:
                print("Session Create Issue : ", e)
                return False


def CheckUserSession(request):
        try:
                user_session = request.session['user_session']
                data = {"loggedin": True}
        except Exception as e:
                print("Create Session Exception : ", e)
                data = {"loggedin": False}
        
        return JsonResponse(data)


def EndUserSession(request):
        try:
                user_session = request.session['user_session']
                del request.session['user_session']
                data = {"loggedout": True}
        except Exception as e:
                print("End Session Exception : ", e)
                data = {"loggedout": False}
        
        return JsonResponse(data)

#---------------------------------------------Pagination---------------------------------------------------------------#

def home(request):
        number_list = range(1,1000)
        page = request.Get.get('page', 1)
        paginator = Paginator(number_list,20)
        try:
                numbers = paginator.page(page)
        except PageNotAnInteger:
                numbers = paginator.page(1)
        except EmptyPage:
                numbers = paginator.page(paginator.num_pages)
        return render(request,'blog/home.html',{'numbers':numbers})



