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
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('user_profile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('art_name', models.CharField(max_length=50)),
                ('art_photo', models.ImageField(null=True, upload_to=b'art_gallery/', blank=True)),
                ('description', models.TextField(max_length=200)),
                ('art_type', models.CharField(max_length=50, null=True, blank=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(to='quiz2_home.Artist')),
            ],
        ),
    ]
