# Generated by Django 3.1 on 2020-10-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanagement', '0010_auto_20200930_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='quantity',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
