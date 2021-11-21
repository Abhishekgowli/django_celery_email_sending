from django.contrib import admin
from django.urls import path,include

from send_mail.tasks import send_main_func
from . import views
from send_mail import views
urlpatterns = [
  path('',views.home,name='home'),
  path('mailsend/',views.celery_sending_mail,name="mailsend")
]