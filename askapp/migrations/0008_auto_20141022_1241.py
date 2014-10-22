# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0007_auto_20141009_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='votes',
            new_name='down_votes',
        ),
        migrations.AddField(
            model_name='question',
            name='up_votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 22, 12, 41, 40, 111727), db_index=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 22, 12, 41, 40, 110338), db_index=True),
        ),
        migrations.AlterField(
            model_name='questionview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 22, 12, 41, 40, 112533)),
        ),
    ]
