from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', 'app.views.index'),
    url(r'^$', 'app.views.index'),
    url(r'^login$', 'app.views.login'),
    url(r'^logout$', 'app.views.log_out'),
    url(r'^register$', 'app.views.register'),

    url(r'^challenge-0', 'challenge_simple_post_10pt.views.index'),
    url(r'^challenge-1', 'challenge_prime_sum_30pt.views.index'),
    url(r'^challenge-2', 'challenge_easy_math_50pt.views.index'),
)