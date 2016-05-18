# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0013_auto_20150917_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='location_city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='filter',
            name='money_raised_max',
            field=models.IntegerField(choices=[(0, b'$0'), (100000, b'$100K'), (500000, b'$500K'), (1000000, b'$1M'), (5000000, b'$5M'), (15000000, b'$15M'), (150000000000, b'$15M+')]),
        ),
        migrations.AlterField(
            model_name='filter',
            name='money_raised_min',
            field=models.IntegerField(choices=[(0, b'$0'), (100000, b'$100K'), (500000, b'$500K'), (1000000, b'$1M'), (5000000, b'$5M'), (15000000, b'$15M'), (150000000000, b'$15M+')]),
        ),
    ]
