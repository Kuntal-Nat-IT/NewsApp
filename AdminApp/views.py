from django.shortcuts import render


def Demo(request):
    return render(request, 'AdminApp/index.html', context={})

def login(request):
    return render(request,'AdminApp/login.html',context={})

def register(request):
    return render(request,'AdminApp/register.html',context={})

def profile(request):
    return render(request,'AdminApp/profile.html',context={})

