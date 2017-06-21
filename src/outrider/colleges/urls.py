from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

import colleges.views

urlpatterns = [
    url(r'^search/$', colleges.views.college_search, name="college_search"),
    url(r'^(?P<slug>[^/]+)/$', colleges.views.college_detail, name="college_detail"),
]

