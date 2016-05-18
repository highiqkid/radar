# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0009_auto_20150913_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='owner',
            field=models.OneToOneField(related_name='current_filter', to='radar_access.Profile'),
        ),
    ]
