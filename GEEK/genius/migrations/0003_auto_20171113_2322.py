# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 23:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('genius', '0002_auto_20171113_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_geek',
            name='date_creation',
        ),
        migrations.AddField(
            model_name='user_geek',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 13, 23, 22, 30, 531462, tzinfo=utc), verbose_name='Date de cr\xe9ation'),
        ),
    ]