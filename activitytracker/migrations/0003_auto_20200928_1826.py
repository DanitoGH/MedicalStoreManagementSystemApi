# Generated by Django 3.1 on 2020-09-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitytracker', '0002_activitytracker_bg_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitytracker',
            name='bg_color',
        ),
        migrations.AddField(
            model_name='activitytracker',
            name='activity_type',
            field=models.CharField(default='Login', max_length=16),
        ),
    ]
