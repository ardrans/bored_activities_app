# Generated by Django 4.2.1 on 2023-07-04 09:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bored_activities_app', '0005_userprofile_activities_fetched_today_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='activities_fetched_today',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_fetch_date',
        ),
        migrations.CreateModel(
            name='UserActivityInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities_fetched_today', models.PositiveIntegerField(default=0)),
                ('last_fetch_date', models.DateField(default=datetime.date.today)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
