# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-14 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.date(1, 1, 1)),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'female'), ('M', 'male')], default='F', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
