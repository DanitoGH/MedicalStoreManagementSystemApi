# Generated by Django 3.1 on 2020-10-22 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0010_auto_20201022_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createorder',
            options={'ordering': ['-date_ordered']},
        ),
    ]
