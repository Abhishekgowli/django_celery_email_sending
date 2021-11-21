from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func,send_main_func
# Create your views here.
def home(request):
    test_func.delay()
    return HttpResponse("The Http Response")


def celery_sending_mail(request):
    send_main_func.delay()
    return HttpResponse("The mail is snet to the user")
    
