# Generated by Django 4.2.1 on 2023-07-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bored_activities_app', '0009_alter_useractivity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
