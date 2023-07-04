from .redis_utils import *
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string


def send_verification_email():
    try:
        print('mail')
        secret_code = key()
        confirmation_link = f'http://localhost:8000/verify_email?key={secret_code}'
        status = send_mail(
            'Welcome!!! Confirmation link',
            render_to_string('verification_email.html', {'confirmation_link': confirmation_link}),
            'nsardra@gmail.com',
            ['nsardra@gmail.com'],
            fail_silently=True,
        )
        print(status)
    except BadHeaderError as e:
        print(f"Error occurred while sending the email: {str(e)}")
