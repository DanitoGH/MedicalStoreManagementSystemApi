# Generated by Django 3.1 on 2020-09-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createorder',
            name='status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]