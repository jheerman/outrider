from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

import coaches.views

urlpatterns = [
    url(r'^coaches/search', coaches.views.coach_search, name="coach_search"),
]

