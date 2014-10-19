# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0005_auto_20141009_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 20, 18, 53, 463637), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 20, 18, 53, 462320), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='head',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questionview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 20, 18, 53, 464444)),
        ),
    ]
