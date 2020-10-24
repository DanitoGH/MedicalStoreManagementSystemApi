# Generated by Django 3.1 on 2020-09-21 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import operationsadminprofile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationsAdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=60)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to=operationsadminprofile.models.upload_location)),
                ('status', models.CharField(default='active', max_length=30)),
                ('user', models.OneToOneField(default='null', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
