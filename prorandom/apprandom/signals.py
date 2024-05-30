# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Website'
        message = f'Hello {instance.username}, welcome to our website!'
        recipient_list = [instance.email]
        send_mail(subject, message, 'from@example.com', recipient_list)
