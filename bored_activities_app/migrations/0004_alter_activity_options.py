# Generated by Django 4.2.1 on 2023-07-03 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bored_activities_app', '0003_remove_activity_activity_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'permissions': [('delete_activities', 'Can delete activity')]},
        ),
    ]