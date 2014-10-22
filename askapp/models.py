from django.db import models
from django.contrib.auth.models import User
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=35)

    def __unicode__(self):
        return '%s' % self.name


class Question(models.Model):
    head = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User)
    date = models.DateTimeField(db_index=True, default=datetime.datetime.now())
    tags = models.ManyToManyField(Tag, related_name='questions', null=True, blank=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s, Author: %s, Date: %s' % (self.head, self.author, self.date)


class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    date = models.DateTimeField(db_index=True, default=datetime.datetime.now())
    validity = models.BooleanField(db_index=True, default=False)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s, Author: %s, Date: %s' % (self.content, self.author, self.date)


class QuestionView(models.Model):
    question = models.ForeignKey(Question)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.question, self.ip, self.session, self.created)


class Bookmark(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return '%s, %s' % (self.question.head, self.user)


class QVote(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    vote = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s, %s' % (self.question.head, self.user)


class AVote(models.Model):
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(User)
    vote = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s, %s' % (self.answer, self.user)
