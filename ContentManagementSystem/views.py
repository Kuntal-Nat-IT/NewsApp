from django.shortcuts import render
from ContentManagementSystem.models import Faq


def faq(request):
    faq = Faq.objects.all()
    return render(request, 'ContentManagementSystem/faq.html', {'faqs': faq})
