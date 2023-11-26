# your_project/utils/email_utils.py

from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_email(subject, message, to_email):
    send_mail(
        subject,
        message,
        'from@example.com',  # O'zgartiring
        [to_email],
        fail_silently=False,
    )
