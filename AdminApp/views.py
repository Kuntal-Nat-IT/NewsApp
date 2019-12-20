from django.shortcuts import render
from NewsApp import models
from .models import AdminProfile


def Login(request):
    try:
        if request.method == 'GET':
            usrid = request.session['usrid']
            return Dashboard(request)
    except Exception as e:
        print(e)
        return render(request,'AdminApp/login.html',context={})


def Logout(request):
    try:
        request.session['usrid']
        del request.session['usrid']
        return Login(request)
    except:
        return Login(request)


def Logincontroler(request):
    try:
        email = request.POST['usrmail']
        password = request.POST['usrpsw']
        request.session['usrid'] = 'admin'
        return Dashboard(request)
    except Exception as e:
        print(e)
        return render(request,'AdminApp/login.html',context={})


def Register(request):
    return render(request,'AdminApp/register.html',context={})


def Profile(request):
    try:
        profileobj = AdminProfile.objects.get(email="kuntal.samanta@cbnits.com")
    except Exception as e:
        print(e)
    
    context = {'profileobj': profileobj}
    return render(request,'AdminApp/adminprofile.html',context=context)


def EditProfileData(request):
    try:
        try:
            firstname = request.POST['firstname']
        except:
            firstname = None
        try:
            lastname = request.POST['lastname']
        except:
            lastname = None
        try:
            emailaddress = request.POST['emailaddress']
        except:
            emailaddress = None
        try:
            about = request.POST['about']
        except:
            about = None
        try:
            adminimg = request.FILES['adminimg']
        except:
            adminimg = None

        newdataobj = AdminProfile.objects.get(email=emailaddress)
        if firstname != None:
            newdataobj.firstname = firstname
        if lastname != None:
            newdataobj.lastname = lastname
        if about != None:
            newdataobj.aboutadmin = about
        if adminimg != None:
            newdataobj.adminimage = adminimg
        newdataobj.save()

        return Profile(request)

    except Exception as e:
        print(e)
        return Profile(request)


def AdminChangePassword(request):
    return render(request,'AdminApp/changepassword.html',context={})


def Dashboard(request):
    try:
        # usrid = request.session['usrid']
        return render(request, 'AdminApp/dashboard.html', context={})
    except Exception as e:
        print("Dashboard", e)
        return Login(request)


def ShowAllUserList(request):
    try:
        alluser = models.UserDetail.objects.all()
    except Exception as e:
        print(e)
    
    context = {'alluser': alluser}
    return render(request,'AdminApp/Userdetails.html',context=context)


def ShowUserProfileData(request, slug):
    try:
        usrObj = models.UserDetail.objects.get(username=slug)
        context = {'usrObj': usrObj}
        return render(request,'AdminApp/userprofile.html',context=context)
    except Exception as e:
        print(e)
        return ShowAllUserList(request)


def ShowLoggedInUser(request):
    try:
        loggedinuser = models.UserSessionTable.objects.all()
    except Exception as e:
        print(e)
    
    context = {'loggedinuser': loggedinuser}
    return render(request,'AdminApp/loggedinuser.html',context=context)
