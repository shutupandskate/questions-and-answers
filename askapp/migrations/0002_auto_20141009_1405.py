# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 14, 5, 55, 501141), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 14, 5, 55, 499626), db_index=True),
        ),
        migrations.AlterField(
            model_name='questionview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 9, 14, 5, 55, 501819)),
        ),
    ]
