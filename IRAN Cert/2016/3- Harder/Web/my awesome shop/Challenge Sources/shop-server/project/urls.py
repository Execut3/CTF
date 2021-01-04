from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^index$', 'app.views.index', name='index'),
                       url(r'^$', 'app.views.index'),
                       url(r'^login$', 'app.views.login', name='login'),
                       url(r'^logout$', 'app.views.log_out', name='logout'),
                       url(r'^register$', 'app.views.register', name='register'),
                       url(r'^change-alias$', 'app.views.change_alias', name='change_alias'),

                       url(r'^shop/', include('shop.urls')),
                       url(r'^comments/', include('comments.urls')),
                       )
