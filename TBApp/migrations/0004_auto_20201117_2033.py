# Generated by Django 3.0.3 on 2020-11-18 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TBApp', '0003_auto_20201117_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]