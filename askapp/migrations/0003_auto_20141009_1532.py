# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0002_auto_20141009_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 15, 32, 24, 751988), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 15, 32, 24, 750527), db_index=True),
        ),
        migrations.AlterField(
            model_name='questionview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 15, 32, 24, 752627)),
        ),
    ]
