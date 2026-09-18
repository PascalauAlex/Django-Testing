from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from products.models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """ Send a welcome email when a new user is created """


    if created:
        send_mail(
            subject='Welcome!',
            message="Thanks for signing ",
            from_email="admin@django.com",
            recipient_list=[instance.email],
            fail_silently=False
        )