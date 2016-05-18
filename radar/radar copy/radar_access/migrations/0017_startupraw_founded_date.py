# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0016_auto_20151001_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='startupraw',
            name='founded_date',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
