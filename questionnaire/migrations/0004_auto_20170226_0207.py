# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 02:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20170226_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 26, 2, 7, 8, 320630, tzinfo=utc), verbose_name='Time completed'),
        ),
    ]
