# Generated by Django 3.1 on 2020-09-12 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientsmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_created',
        ),
    ]
