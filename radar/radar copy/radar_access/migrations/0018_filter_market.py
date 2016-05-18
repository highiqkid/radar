# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0017_startupraw_founded_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='market',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
