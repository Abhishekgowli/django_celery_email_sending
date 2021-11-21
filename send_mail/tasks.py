from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_celery_project import settings



@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def send_main_func(self):
    users=get_user_model().objects.all()
    for user in users:
        mail_subject="Hello I am Sending the Mail"
        message="thankyou for registration for the website"
        to_email=user.email
        send_mail(subject=mail_subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[to_email],fail_silently=True)


