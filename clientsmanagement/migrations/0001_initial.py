# Generated by Django 3.1 on 2020-09-12 01:52

import clientsmanagement.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=60, verbose_name='date created')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to=clientsmanagement.models.upload_location)),
                ('status', models.CharField(default='active', max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('user', models.OneToOneField(default='null', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
