from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import passthru

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^passthru/$', passthru, name='passthru')


]
