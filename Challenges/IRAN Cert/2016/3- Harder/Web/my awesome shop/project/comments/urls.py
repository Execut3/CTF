from django.conf.urls import include, url, patterns
from views import *


urlpatterns = patterns('',
                       url(r'^new$', 'comments.views.create_new', name='create_new_comment'),
                       url(r'^view$', 'comments.views.view', name='view_comments'),
                       url(r'^flush$', 'comments.views.flush', name='flush_comments'),
                       )
