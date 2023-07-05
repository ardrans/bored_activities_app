from django.db import models
from django.contrib.auth.models import User
from datetime import date
from enum import Enum

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email_verified = models.BooleanField(default=False)
    #TYPE_CHOICES = []
    #types = models.CharField(max_length=20, choices=TYPE_CHOICES)
    USERNAME_FIELD = 'email'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #activity_type = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    edit_mode = models.BooleanField(default=False)


    class Meta:
        permissions = [
            ("delete_activities", "Can delete activity"),
        ]


class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    type_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'types'


class UserAction(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)


    class Meta:
        managed = True
        db_table = 'user_activity'

class UserActions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'user_actions'