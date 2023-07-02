from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    TYPE_CHOICES = (
        ('education', 'type 1'),
        ('recreational', 'type 2'),
        ('social', 'type 3'),
        ('diy', 'type 4'),
        ('charity', 'type 5'),
        ('cooking', 'type 6'),
        ('relaxation', 'type 7'),
        ('music', 'type 8'),
        ('busywork', 'type 9'),

    )
    types = models.CharField(max_length=20, choices=TYPE_CHOICES)


