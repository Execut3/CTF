# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^register$', register_view, name='register'),

    url(r'^$', index, name='root'),
    url(r'^index$', index, name='index'),

    url(r'^flag$', flag_view, name='flag'),

    url(r'^profile/(?P<pk>\d*)$', profile, name='profile'),
    url(r'^profile/edit$', profile_edit, name='profile_edit'),
    url(r'^avatar$', change_avatar, name='change_avatar'),
]
