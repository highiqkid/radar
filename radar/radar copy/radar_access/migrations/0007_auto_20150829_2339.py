# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0006_startupraw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='angellist_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='competitors',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='money_raised',
            field=models.BigIntegerField(default=0, blank=True),
        ),
    ]
