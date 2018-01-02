from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import TestLocationView

urlpatterns = [
    url(r'^test/$', TestLocationView.as_view(), name='test_location_view'),

]
