from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^vigenere$', 'vigenere_10pt.views.index'),
    url(r'^ascii-art$', 'ascii_art_40pt.views.index'),
)