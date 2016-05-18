# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='categories',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='startup',
            name='website',
            field=models.URLField(max_length=300),
        ),
    ]
