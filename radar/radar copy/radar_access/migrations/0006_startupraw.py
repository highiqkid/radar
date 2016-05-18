# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0005_auto_20150826_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartupRaw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=700)),
                ('permalink', models.CharField(max_length=700)),
                ('homepage_url', models.TextField(blank=True)),
                ('category_list', models.TextField(blank=True)),
                ('market', models.CharField(max_length=700, blank=True)),
                ('funding', models.BigIntegerField(blank=True)),
                ('status', models.CharField(max_length=32, blank=True)),
                ('country', models.CharField(max_length=32, blank=True)),
                ('region', models.CharField(max_length=700, blank=True)),
                ('city', models.CharField(max_length=700, blank=True)),
                ('description', models.TextField(blank=True)),
                ('domain', models.TextField(blank=True)),
                ('image_url', models.TextField(blank=True)),
                ('facebook_url', models.TextField(blank=True)),
                ('twitter_url', models.TextField(blank=True)),
                ('linkedin_url', models.TextField(blank=True)),
                ('cbase_uuid', models.CharField(max_length=40, blank=True)),
                ('angellist_id', models.IntegerField(blank=True)),
                ('angellist_url', models.TextField(blank=True)),
                ('angellist_name', models.CharField(max_length=700, blank=True)),
                ('founders', models.TextField()),
                ('competitors', models.TextField()),
            ],
        ),
    ]
