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
from datetime import datetime, timezone, timedelta,date
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import json
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


#------------------------------------------- Email verification -------------------------------------------------------------------

class SendVerificationEmail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        email = UserDetail.objects.get(user=request.user).email
        if email == '':
            return Response({
                'ack': '0',
                'details': 'No email for the user'
            })
        user_data = {'username': request.user.username, 'email': email, 'random_string': randomDigits(10)}
        signer = TimestampSigner()
        signed_user_data = signer.sign(json.dumps(user_data))
        current_site = get_current_site(request)
        mail_subject = 'Email verification for NewsApp'
        message = render_to_string('NewsApp/activate_email.html',{
            'user': request.user,
            'domain': current_site.domain,
            'user_data': urlsafe_base64_encode(force_bytes(signed_user_data)),
        })
        if sendMail(email, message, mail_subject):
            return Response({
                'ack': '1',
                'details': 'Email sent',
            })
        else:
            return Response({
                'ack': '0',
                'details': 'Unable to send email',
            })


class VerifyEmail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, usernameb64):

        try:
            signed_username = force_text(urlsafe_base64_decode(usernameb64))
        except (TypeError, ValueError, OverflowError):
            return render(request, 'NewsApp/email_verified.html', {'message': 'bad url'})

        signer = TimestampSigner()
        try:
            user_data = json.loads(signer.unsign(signed_username, max_age=timedelta(hours=24)))
        except BadSignature:
            return render(request, 'NewsApp/email_verified.html', {'message': 'bad url'})

        except SignatureExpired:
            return render(request, 'NewsApp/email_verified.html', {'message': 'url expired'})
        try:

            account = UserDetail.objects.get(user__username=user_data['username'])
            if account.email != user_data['email']:
                return render(request, 'NewsApp/email_verified.html', {'message': 'email does not match'})
            else:
                if not account.verifiedEmail:
                    account.verifiedEmail = True
                    account.save()
                    try:
                        #check if the task is already complete
                        TaskCompleted.objects.get(task__name='Provide Email Address', user=request.user)
                    except TaskCompleted.DoesNotExist:
                        task_completed.send(sender=self.__class__, user_details={'account': account, 'name': 'Provide Email Address'})

        except UserDetail.DoesNotExist:
            return render(request, 'NewsApp/email_verified.html', {'message': 'no such user'})

        return render(request, 'NewsApp/email_verified.html', {'message': 'Email verified successfully'})


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


