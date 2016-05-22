# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_last_name', models.CharField(max_length=50)),
                ('employee_number', models.DecimalField(max_digits=6, decimal_places=0)),
                ('employee_department', models.CharField(max_length=60, null=True, blank=True)),
                ('employee_work_hours', models.IntegerField()),
                ('employee_wages', models.DecimalField(max_digits=8, decimal_places=2)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('user_profile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
