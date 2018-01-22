#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<p2>\d+)/(?P<p1>\d+)/(?P<p3>\d+)/',views.detail, name='detail'),
    url(r'^gettest1/$', views.gettest1, name='gettest1'),
    url(r'^gettest2/$', views.gettest2, name='gettest2'),
    url(r'^gettest3/$', views.gettest3, name='gettest3'),
    url(r'^posttest1/$', views.posttest1, name='posttest1'),
    url(r'^posttest2/$', views.posttest2, name='posttest2'),
    url(r'^cookietest/$', views.cookietest, name='cookietest'),
    url(r'^redtest1/$', views.redtest1, name='redtest1'),
    url(r'^redtest2/$', views.redtest2, name='redtest2'),
    url(r'^session1/$', views.session1, name='session1'),
    url(r'^session2/$', views.session2, name='session2'),
    url(r'^session2_handle/$', views.session2_handle, name='session2_handle'),
    url(r'^session3/$', views.session3, name='session3'),
]
