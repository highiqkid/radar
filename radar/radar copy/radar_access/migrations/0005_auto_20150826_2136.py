# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0004_auto_20150820_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='angellist_id',
            field=models.IntegerField(default=-1, blank=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='angellist_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='angellist_url',
            field=models.URLField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='cbase_uuid',
            field=models.CharField(max_length=33, blank=True),
        ),
    ]
