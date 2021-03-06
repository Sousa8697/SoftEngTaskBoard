# Generated by Django 3.0.3 on 2020-11-18 01:19

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='')),
                ('bio', models.TextField(blank=True, default='')),
                ('user', models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('due_date', models.CharField(max_length=50)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=512)),
                ('section', models.CharField(choices=[('to-do', 'TO-DO'), ('doing', 'DOING'), ('done', 'DONE')], default='to-do', max_length=6)),
                ('accountOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TBApp.Account')),
            ],
        ),
    ]
