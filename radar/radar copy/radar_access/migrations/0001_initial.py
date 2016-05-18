# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permalink', models.CharField(unique=True, max_length=100)),
                ('last_updated', models.IntegerField(default=0, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField()),
                ('status', models.CharField(max_length=50, choices=[(b'operating', b'operating'), (b'acquired', b'acquired'), (b'closed', b'closed')])),
                ('funding_rounds', models.IntegerField()),
                ('categories', models.CharField(max_length=200)),
                ('market', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('state_code', models.CharField(max_length=4, blank=True)),
                ('country_code', models.CharField(max_length=6)),
                ('money_raised', models.IntegerField(default=0, blank=True)),
                ('last_funding', models.IntegerField(default=0, blank=True)),
                ('first_funding', models.IntegerField(default=0, blank=True)),
                ('founded_date', models.IntegerField(default=0, blank=True)),
                ('logo', models.URLField(max_length=300, blank=True)),
                ('short_description', models.CharField(max_length=140, blank=True)),
                ('description', models.CharField(max_length=500, blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('num_employees_min', models.IntegerField(default=0, blank=True)),
                ('num_employees_max', models.IntegerField(default=0, blank=True)),
                ('team', models.CharField(max_length=300, blank=True)),
                ('investors', models.CharField(max_length=300, blank=True)),
                ('press_mentions', models.CharField(max_length=150, blank=True)),
                ('competitors', models.CharField(max_length=100, blank=True)),
                ('num_employees', models.IntegerField(default=0, blank=True)),
                ('revenue', models.CharField(max_length=30, blank=True)),
                ('growth_percent', models.IntegerField(default=0, blank=True)),
                ('is_inc5000', models.BooleanField(default=False)),
            ],
        ),
    ]
