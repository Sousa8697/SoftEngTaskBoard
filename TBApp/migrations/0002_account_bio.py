# Generated by Django 3.0.3 on 2020-11-05 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TBApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]