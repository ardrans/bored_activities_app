from django.db import models
from django.contrib.auth.models import User
from datetime import date

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #TYPE_CHOICES = []
    #types = models.CharField(max_length=20, choices=TYPE_CHOICES)
    USERNAME_FIELD = 'email'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #activity_type = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)

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
        db_table = 'Types'

class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activities_fetched_today = models.PositiveIntegerField(default=0)
    last_fetch_date = models.DateField(default=date.today)

    class Meta:
        managed = True
        db_table = 'user_activity'