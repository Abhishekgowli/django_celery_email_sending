from django.contrib import admin
from django.urls import path,include
from . import views
from send_mail import views
urlpatterns = [
  path('',views.home,name='home')
]