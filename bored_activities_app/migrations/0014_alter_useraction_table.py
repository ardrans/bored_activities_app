# Generated by Django 4.2.1 on 2023-07-05 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bored_activities_app', '0013_alter_useraction_options_alter_useraction_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='useraction',
            table='user_activity',
        ),
    ]