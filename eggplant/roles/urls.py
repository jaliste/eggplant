from django.conf.urls import patterns, url

from . import models
from . import views


urlpatterns = [
    url(r'^(?P<role>\w+)/$', views.role, name="role"),
]
