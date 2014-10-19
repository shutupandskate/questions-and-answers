# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0006_auto_20141009_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 20, 29, 37, 446051), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 20, 29, 37, 444595), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='head',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questionview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 20, 29, 37, 446848)),
        ),
    ]
