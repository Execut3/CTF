from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index'),
    url(r'^index$', 'app.views.index'),
)
