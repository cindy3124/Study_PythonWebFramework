# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    #字符串的匹配
    url(r'^$', 'django_demo.views.home', name='home'),

    #以下2个都是子应用的匹配
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
