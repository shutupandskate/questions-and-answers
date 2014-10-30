import random
from random import randrange
from datetime import timedelta, datetime

from django.core.management.base import BaseCommand
from random_words import RandomWords
from random_words import RandomEmails
from random_words import LoremIpsum
from random_words import RandomNicknames

from askapp.models import User, Question, Answer, QuestionView, Tag, Bookmark


tags = ['c#', 'java', 'android', 'javascript', 'c++', 'iphone', 'asp.net', 'jquery',
        'mysql', 'html', 'css', 'python', 'sql-server', 'c', 'ruby', 'regex', 'sql',
        'database', 'django', 'unix', 'linux', 'arrays', 'json', 'eclipse', 'ruby-on-rails',
        'ajax', 'objective-c', 'visual-studio', 'osx', 'wordpress', 'forms', 'query',
        'web-service', 'oracle', 'perl', 'git', 'apache', 'frameworks', 'node.js', 'qt',
        'delphi', 'ie', 'sockets', 'http', 'google-maps', 'postgresql', 'email', 'templates']
user_ids = []
question_ids = []
tag_ids = []

d1 = datetime.strptime('1/1/2008 1:00 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/12/2014 1:00 AM', '%m/%d/%Y %I:%M %p')


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


class Command(BaseCommand):
    for tag in tags:  # creating independent tags
        t = Tag(name=tag)
        t.save()
        tag_ids.append(t.pk)

    for i in range(40):  # creating users
        u = User(
            username=RandomWords().random_word() + str(random.randint(0, 99999)),
            first_name=RandomNicknames().random_nick(gender='m'),
            last_name=RandomNicknames().random_nick(gender='m'),
            email=RandomEmails().randomMail(),
            date_joined=random_date(d1, d2),
            password=RandomWords().random_word()
        )
        u.save()
        user_ids.append(u.pk)

    for i in range(500):  # create questions
        q = Question(
            head=LoremIpsum().get_sentence(),
            content=LoremIpsum().get_sentences(5),
            author_id=random.choice(user_ids),
            date=random_date(d1, d2),
            up_votes=random.randint(0, 50),
            down_votes=random.randint(0, 50),
        )
        q.save()
        question_ids.append(q.pk)
        tags = random.sample(tag_ids, 4)
        for tag in tags:
            q.tags.add(tag)

    for i in range(1800):  # creating answers
        a = Answer(
            content=LoremIpsum().get_sentences(3),
            question_id=random.choice(question_ids),
            author_id=random.choice(user_ids),
            date=random_date(d1, d2),
            validity=random.choice([-1, 1]),
            votes=random.randint(-50, 50),
        )
        a.save()

    for i in range(3000):  # views faker
        q = QuestionView(
            session=str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)) + '.' + str(
                random.randint(1, 255)) + '.' + str(random.randint(1, 255)),
            ip=str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)) + '.' + str(
                random.randint(1, 255)) + '.' + str(random.randint(1, 255)),
            question=Question.objects.get(id=random.choice(question_ids)),
            created=random_date(d1, d2)
        )
        q.save()

    for i in range(120):
        b = Bookmark(
            question=Question.objects.get(id=random.choice(question_ids)),
            user=User.objects.get(id=random.choice(user_ids)),
        )
        b.save()