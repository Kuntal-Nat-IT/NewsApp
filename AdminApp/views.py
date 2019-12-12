from django.shortcuts import render


def Demo(request):
    return render(request, 'AdminApp/index.html', context={})
