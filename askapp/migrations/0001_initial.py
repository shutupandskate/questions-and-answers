# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 9, 17, 9, 40, 37, 674844), db_index=True)),
                ('validity', models.BooleanField(default=False, db_index=True)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.IntegerField(default=0)),
                ('answer', models.ForeignKey(to='askapp.Answer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 9, 17, 9, 40, 37, 673428), db_index=True)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=40)),
                ('session', models.CharField(max_length=40)),
                ('created', models.DateTimeField(default=datetime.datetime(2014, 9, 17, 9, 40, 37, 675474))),
                ('question', models.ForeignKey(to='askapp.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='askapp.Question')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('description', models.CharField(max_length=250, blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 9, 17, 9, 40, 37, 672909))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=140)),
                ('gender', models.CharField(max_length=140)),
                ('profile_picture', models.ImageField(upload_to=b'thumbpath', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name=b'questions', null=True, to='askapp.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='question',
            field=models.ForeignKey(to='askapp.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='askapp.Question'),
            preserve_default=True,
        ),
    ]
