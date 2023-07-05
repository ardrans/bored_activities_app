# Generated by Django 4.2.1 on 2023-07-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bored_activities_app', '0016_alter_useractions_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraction',
            name='created_at',
        ),
        migrations.AddField(
            model_name='activity',
            name='edit_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='type',
            table='types',
        ),
        migrations.AlterModelTable(
            name='useractions',
            table='user_actions',
        ),
    ]