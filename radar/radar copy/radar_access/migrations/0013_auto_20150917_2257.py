# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radar_access', '0012_note_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(related_name='notes', to='radar_access.Profile'),
        ),
    ]
