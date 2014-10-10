# -*- coding: utf-8 -*-

import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.utils import timezone
from django.template import RequestContext
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django import template

from askapp.models import User, Question, Answer, QuestionView, Tag, Bookmark, QVote


register = template.Library()
from askapp.forms import RegisterForm, AddQuestionForm, AddAnswerForm, ValidAnswerForm


def tag_list(request):
    tag_list = Tag.objects.all()
    size = Tag.objects.annotate(count=Count('questions')).values_list('count', flat=True)

    return render_to_response('tag_list.html', {
        'size': size,
        'tag_list': tag_list,
    }, context_instance=RequestContext(request))


def main(request):
    tag_list = Tag.objects.all()[:60]
    size = Tag.objects.annotate(count=Count('questions')).values_list('count', flat=True)
    knowing_users = User.objects.annotate(a_count=Count('answer', distinct=True)).annotate(
        q_count=Count('question', distinct=True)).values_list('a_count', 'q_count', 'username', 'first_name',
                                                              'last_name', 'pk').order_by('-a_count')[:4]
    curious_users = User.objects.annotate(q_count=Count('question', distinct=True)).annotate(
        a_count=Count('answer', distinct=True)).values_list('q_count', 'a_count', 'username', 'first_name', 'last_name',
                                                            'pk').order_by('-q_count')[:4]

    return render_to_response('main.html', {
        'size': size,
        'tag_list': tag_list,
        'knowing_users': knowing_users,
        'curious_users': curious_users,
    }, context_instance=RequestContext(request))


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    asked_num = Question.objects.filter(author__username=user.username).count()
    questions = Question.objects.filter(author__username=user.username)[:5]
    answ_num = Answer.objects.filter(author__username=user.username).count()
    answers = Answer.objects.filter(author__username=user.username).values('question__pk', 'question__head',
                                                                           'question__content', ).distinct()[:5]
    taglist = Tag.objects.filter(questions__author__id=user_id)[:20]
    size = Tag.objects.filter(questions__author__id=user_id).annotate(count=Count('questions')).values_list('count',
                                                                                                            flat=True)[
           :20]
    # tslist = zip(taglist, sizelist)
    bm_num = Bookmark.objects.filter(user_id=user_id).count()
    bookmarks = Bookmark.objects.filter(user_id=user_id)[:5]

    return render_to_response('user.html', {
        'pageUser': user,
        'asked_num': asked_num,
        'questions': questions,
        'answ_num': answ_num,
        'answers': answers,
        'size': size,
        'tag_list': taglist,
        'bm_num': bm_num,
        'bookmarks': bookmarks,
    }, context_instance=RequestContext(request))


def user_q(request, user_id):
    pageUser = get_object_or_404(User, pk=user_id)
    asked_num = Question.objects.filter(author__username=pageUser.username).count()
    taglist = Tag.objects.filter(questions__author__id=user_id).values('questions__tags__name',
                                                                       'questions__tags__pk').distinct()[:20]
    sizelist = Tag.objects.filter(questions__author__id=user_id).annotate(count=Count('questions')).values_list('count',
                                                                                                                flat=True)[
               :20]
    tslist = zip(taglist, sizelist)

    question_list = Question.objects.filter(author__username=pageUser.username).order_by("-date")
    paginator = Paginator(question_list, 30)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'user_q.html', {
        'questions': questions,
        'pageUser': pageUser,
        'asked_num': asked_num,
        'tslist': tslist
    }, context_instance=RequestContext(request))


def user_bm(request, user_id):
    pageUser = get_object_or_404(User, pk=user_id)
    answ_num = Answer.objects.filter(author__username=pageUser.username).count()
    taglist = Tag.objects.filter(questions__author__id=user_id).values('questions__tags__name', 'questions__tags__pk').distinct()[:20]
    sizelist = Tag.objects.filter(questions__author__id=user_id).annotate(count=Count('questions')).values_list('count',flat=True)[:20]
    tslist = zip(taglist, sizelist)

    bookmark_list = Bookmark.objects.filter(user=User.objects.get(pk=user_id))
    bm_num = Bookmark.objects.filter(user=User.objects.get(pk=user_id)).count()

    paginator = Paginator(bookmark_list, 30)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'user_bm.html', {
        'pageUser': pageUser,
        'answ_num': answ_num,
        'questions': questions,
        'bookmark_list': bookmark_list,
        'tslist': tslist,
        'bm_num': bm_num
    })


def user_list(request):
    user_list = User.objects.all().order_by("-date_joined").annotate(a_count=Count('answer')).annotate(
        q_count=Count('question')).values_list('a_count', 'q_count', 'username', 'first_name', 'last_name', 'pk')

    paginator = Paginator(user_list, 32)
    page = request.GET.get('page')

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'user_list.html', {
        'users': users
    })


def add_question(request):
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            q = Question.objects.create(
                head=request.POST.get("head"),
                content=request.POST.get("content"),
                author=User.objects.get(id=request.user.id),
                date=timezone.now(),
            )

            print (form.cleaned_data.get('tags'))
            for tag in form.cleaned_data.get('tags'):
                q.tags.add(tag)
            q.save()

            return HttpResponseRedirect("/questions/")
    else:
        form = AddQuestionForm()
    return render(request, 'add_question.html', {
        'form': form,
    })


def question_list(request):
    question_list = Question.objects.all().order_by("-date")
    paginator = Paginator(question_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'question_list.html', {
        'questions': questions,
    })


def tag(request, tag_id):
    tagObj = get_object_or_404(Tag, pk=tag_id)
    tag_list = Tag.objects.all()
    question_list = Question.objects.filter(tags__pk=tag_id).order_by("-date")
    size = Question.objects.filter(tags__pk=tag_id).count()

    return render_to_response('tag.html', {
        'tag': tagObj,
        'tag_list': tag_list,
        'question_list': question_list,
        'size': size,
    }, context_instance=RequestContext(request))


def question_a(request, question_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if request.POST.get('content'):
                a = Answer.objects.create(
                    content=request.POST.get("content"),
                    question=Question.objects.get(id=question_id),
                    author=request.user,
                    date=timezone.now(),
                    validity=False,
                )
    return HttpResponse("")


def question_bm(request, question_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            try:
                Bookmark.objects.get(question=question_id, user=request.user).delete()

            except Bookmark.DoesNotExist:

                b = Bookmark(
                    question=Question.objects.get(id=question_id),
                    user=User.objects.get(pk=request.user.pk),
                )
                b.save()

        return HttpResponse("")


def question_vl(request, question_id):
    questionObj = get_object_or_404(Question, pk=question_id)

    if request.user == questionObj.author:
        if request.method == 'POST':
            if request.POST.get('a_id'):
                a = Answer.objects.get(pk=request.POST.get('a_id'))
                if not a.validity:
                    a.validity = True
                else:
                    a.validity = False
                a.save()
        return HttpResponse("")


def question_up(request, question_id):
    if request.method == 'POST':
        try:
            like = QVote.objects.get(question=Question.objects.get(pk=question_id),
                                     user=User.objects.get(pk=request.user.pk), vote=1)
            like_num = QVote.objects.filter(question=Question.objects.get(pk=question_id),
                                            user=User.objects.get(pk=request.user.pk), vote=1).count()
        except QVote.DoesNotExist:
            like_num = 0
        try:
            dislike = QVote.objects.get(question=Question.objects.get(pk=question_id),
                                        user=User.objects.get(pk=request.user.pk), vote=-1)
            dislike_num = QVote.objects.filter(question=Question.objects.get(pk=question_id),
                                               user=User.objects.get(pk=request.user.pk), vote=-1).count()
        except QVote.DoesNotExist:
            dislike_num = 0

        p = Question.objects.get(pk=question_id)

        if dislike_num > 0:  # vote again if dislike exist
            dislike.delete()
            QVote.objects.create(question=Question.objects.get(pk=question_id),
                                 user=User.objects.get(pk=request.user.pk), vote=1)
            p.votes += 2
            p.save()

        else:  # vote if dislike didn't exist before
            if like_num > 0:  # delete like if exists
                like.delete()
                p.vote -= 1
                p.save()

            else:  # add like if it not exists
                QVote.objects.create(question=Question.objects.get(pk=question_id),
                                     user=User.objects.get(pk=request.user.pk), vote=1)
                p.votes += 1
                p.save()

    return HttpResponse("")


def answer_up(request, answer_id):
    return HttpResponse("up")


def answer_down(request, answer_id):
    return HttpResponse("down")


def question_down(request, question_id):
    if request.method == 'POST':
        try:
            like = QVote.objects.get(
                question=Question.objects.get(pk=question_id),
                user=User.objects.get(pk=request.user.pk),
                vote=1
            )
            like_num = QVote.objects.filter(
                question=Question.objects.get(pk=question_id),
                user=User.objects.get(pk=request.user.pk),
                vote=1
            ).count()
        except QVote.DoesNotExist:
            like_num = 0
        try:
            dislike = QVote.objects.get(
                question=Question.objects.get(pk=question_id),
                user=User.objects.get(pk=request.user.pk),
                vote=-1
            )
            dislike_num = QVote.objects.filter(
                question=Question.objects.get(pk=question_id),
                user=User.objects.get(pk=request.user.pk),
                vote=-1
            ).count()
        except QVote.DoesNotExist:
            dislike_num = 0

        p = Question.objects.get(pk=question_id)

        if like_num > 0:  # if like exists then vote again
            like.delete()
            QVote.objects.create(
                question=Question.objects.get(pk=question_id),
                user=User.objects.get(pk=request.user.pk),
                vote=-1
            )
            p.votes -= 2
            p.save()
        else:  # vote if like didn't exist
            if dislike_num > 0:  # remove dislike
                dislike.delete()
                p.votes += 1
                p.save()
            else:
                QVote.objects.create(
                    question=Question.objects.get(pk=question_id),
                    user=User.objects.get(pk=request.user.pk),
                    vote=-1
                )
                p.votes -= 1
                p.save()

    return HttpResponse("")


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # ## VIEWS
    if not QuestionView.objects.filter(question=question, session=request.session.session_key):
        view = QuestionView(
            question=question,
            ip=request.META['REMOTE_ADDR'],
            created=datetime.datetime.now(),
            session=request.session.session_key
        )
        view.save()

    answer_list = Answer.objects.filter(question__pk=question.pk).order_by("-validity", "date")
    paginator = Paginator(answer_list, 10)
    page = request.GET.get('page')
    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        answers = paginator.page(1)
    except EmptyPage:
        answers = paginator.page(paginator.num_pages)
    ans_num = Answer.objects.filter(question__pk=question.pk).count()
    views = QuestionView.objects.filter(question=question).count()
    bm_num = Bookmark.objects.filter(question__pk=question.pk).count()

    if request.user.is_authenticated():
        try:
            bm = Bookmark.objects.get(question=question_id, user=User.objects.get(pk=request.user.pk))
        except Bookmark.DoesNotExist:
            bm = 0
    else:
        bm = 0

    if request.user.is_authenticated():
        try:
            user_vote = QVote.objects.get(question=question_id, user=User.objects.get(pk=request.user.pk)).vote
        except QVote.DoesNotExist:
            user_vote = 0
    else:
        user_vote = 0

    return render(request, 'question.html', {
        'user': request.user,
        'question': question,
        'answers': answers,
        'answer_list': answer_list,
        'form_add': AddAnswerForm(),
        'form_valid': ValidAnswerForm(),
        'ans_num': ans_num,
        'bm_num': bm_num,
        'views': views,
        'bm': bm,
        'user_vote': user_vote,
    }, context_instance=RequestContext(request))


def register(request):
    my_error = "The user with this name or email already exists. Please, choose something else."
    my_error2 = "Don't leave empty fields."
    if request.method == 'POST':
        if RegisterForm(request.POST).is_valid():
            u = User.objects.create_user(
                email=request.POST.get("email"),
                username=request.POST.get("username"),
                password=request.POST.get("password"),
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
            )

            try:
                u.save()
            except (ValueError, TypeError, IntegrityError):
                return render(request, "register.html", {'my_error': my_error, })
            return HttpResponseRedirect('/account/login')
        else:
            return render(request, "register.html", {'my_error2': my_error2, })
    return render(request, "register.html", {})
