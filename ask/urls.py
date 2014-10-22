from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf import settings

from askapp import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url('^$', views.main, name='main'),

    url('^users/$', views.users_list, name='users_list'),

    url(r'^questions/$', views.questions_list, name='questions_list'),
    url(r'^questions/add/$', views.add_question, name='add_question'),

    url(r'^user/(?P<user_id>\d+)/$', views.user_page, name='user_page'),
    url(r'^user/(?P<user_id>\d+)/q/$', views.user_question_list, name='user_question_list'),
    url(r'^user/(?P<user_id>\d+)/bm/$', views.user_bookmarks, name='user_bookmarks'),

    url(r'^question/(?P<question_id>\d+)/$', views.question_page, name='question_page',),
    #url(r'^question/(?P<question_id>\d+)/vl/$', views.question_vl, name='question_vl',),
    url(r'^question/(?P<question_id>\d+)/a/$', views.add_answer, name='add_answer',),

    url(r'^question/(?P<question_id>\d+)/bm/$', views.bookmark_question, name='bookmark_question',),
    url(r'^question/(?P<question_id>\d+)/vote/(?P<action>up|down)/$', views.vote_for_question, name='vote_for_question',),

    url(r'^tag/(?P<tag_id>\d+)/$', views.tag_page, name='tag_page'),
    url(r'^tags/$', views.tag_list, name='tag_list'),

    url(r'^account/login/$', login),
    url(r'^account/logout/$', logout,
        {'next_page': '/'}),
    url(r'^account/register/$', views.register, name='register'),

    # static
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT + '/js'}),

    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT + '/css'}),

    (r'^img/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT + '/img'}),

    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT + '/fonts'}),
)
