# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0014_auto_20151001_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='location_city',
            field=models.CharField(max_length=400),
        ),
    ]
