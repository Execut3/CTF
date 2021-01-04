from django.conf.urls import include, url, patterns
from views import *


urlpatterns = patterns('',
                       url(r'^$', 'shop.views.index', name='shop_index'),
                       )
