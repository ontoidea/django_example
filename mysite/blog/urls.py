from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^(?P<post_id>\d+)/$', views.content, name="content"),
    url(r'^write/$', views.write, name="write"),
)