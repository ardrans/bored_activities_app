# Generated by Django 4.2.1 on 2023-07-02 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bored_activities_app', '0002_type_alter_userprofile_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='activity_type',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='types',
        ),
    ]