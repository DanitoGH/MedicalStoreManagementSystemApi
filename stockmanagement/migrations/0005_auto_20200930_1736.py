# Generated by Django 3.1 on 2020-09-30 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanagement', '0004_auto_20200930_0143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addstockitem',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterUniqueTogether(
            name='addstockitem',
            unique_together={('name', 'quantity')},
        ),
    ]
