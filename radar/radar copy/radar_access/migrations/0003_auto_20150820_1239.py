# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0002_auto_20150820_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='description',
            field=models.CharField(max_length=1500, blank=True),
        ),
    ]
