# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0003_auto_20141009_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 15, 52, 26, 748069), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 15, 52, 26, 746428), db_index=True),
        ),
        migrations.AlterField(
            model_name='questionview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 15, 52, 26, 749081)),
        ),
    ]
