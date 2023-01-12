from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin.php$','maze_app.views.Admin'),
    url(r'^admin','maze_app.views.Admin'),
    url(r'^$','maze_app.views.Main'),
    url(r'^main.php$','maze_app.views.Main'),
    url(r'^main$','maze_app.views.Main'),
    url(r'^main/page=(?P<page>.*)$','maze_app.views.MainPage'),
    url(r'^subscribe.php$','maze_app.views.Subscribe'),
    url(r'^session.php$','maze_app.views.Session'),
)
