# Generated by Django 3.0.3 on 2020-11-18 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TBApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
    ]
