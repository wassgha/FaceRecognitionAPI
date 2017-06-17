
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from api import views

urlpatterns = [
    # Examples:

    url(r'^recognize/$', views.recognize),
    url(r'^train/$', views.train),
    url(r'^new/$', views.new),
    url(r'^users/$', views.users),
    url(r'^admin/', admin.site.urls),
]
