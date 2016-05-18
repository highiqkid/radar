# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0003_auto_20150820_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='is_my_company',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='startup',
            name='is_prefiltered',
            field=models.BooleanField(default=True),
        ),
    ]
