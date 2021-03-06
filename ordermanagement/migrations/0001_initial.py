# Generated by Django 3.1 on 2020-09-12 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stockmanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=6)),
                ('urgency_level', models.CharField(default='normal', max_length=30)),
                ('date_ordered', models.DateTimeField(auto_now_add=True, verbose_name='date ordered')),
                ('status', models.CharField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stockmanagement.addstockitem')),
            ],
        ),
    ]
