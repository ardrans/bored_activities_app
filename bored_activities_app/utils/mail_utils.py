from .redis_utils import *
from .util import *
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string

redis_client = RedisUtil()
URL = 'http://localhost:8000/'

def send_verification_email(email):
    try:
        secret_code = random_string_generator(32)
        redis_client.set_value(secret_code,email)
        confirmation_link = f'{URL}verify_email?key={secret_code}'
        return send_mail(
            'Welcome!!! Confirmation link',
            render_to_string('verification_email.html', {'confirmation_link': confirmation_link}),
            'nsardra@gmail.com',
            [email],
            fail_silently=True,
        )
    except BadHeaderError as e:
        print(f"Error occurred while sending the email: {str(e)}")
