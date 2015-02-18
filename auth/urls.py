from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^accounts/', include('allauth.urls')),
)
