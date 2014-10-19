from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf import settings

from askapp import views

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url('^$', views.main, name='main'),

    url('^users/$', views.user_list, name='user_list'),

    url(r'^questions/$', views.question_list, name='question_list'),
    url(r'^questions/add/$', views.add_question, name='add_question'),

    url(r'^user/(?P<user_id>\d+)/$', views.user, name='user'),
    url(r'^user/(?P<user_id>\d+)/q/$', views.user_q, name='user_q'),
    url(r'^user/(?P<user_id>\d+)/bm/$', views.user_bm, name='user_bm'),

    url(r'^question/(?P<question_id>\d+)/$', views.question, name='question',),
    url(r'^question/(?P<question_id>\d+)/vl/$', views.question_vl, name='question_vl',),
    url(r'^question/(?P<question_id>\d+)/a/$', views.question_a, name='question_a',),
    url(r'^question/(?P<question_id>\d+)/bm/$', views.question_bm, name='question_bm',),
    url(r'^question/(?P<question_id>\d+)/up/$', views.question_up, name='question_up',),
    url(r'^question/(?P<question_id>\d+)/down/$', views.question_down, name='question_down',),

    url(r'^answer/(?P<answer_id>\d+)/up/$', views.answer_up, name='answer_up',),
    url(r'^answer/(?P<answer_id>\d+)/down/$', views.answer_down, name='answer_down',),

    url(r'^tag/(?P<tag_id>\d+)/$', views.tag, name='tag'),
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
