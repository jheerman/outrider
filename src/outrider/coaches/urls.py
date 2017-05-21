from django.conf.urls import url

from . import views

app_name="coaches"
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^foo', views.foo, name='foo'),
]

