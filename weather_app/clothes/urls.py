from django.urls import path
from django.conf.urls import url, include
from .views import JeansCreateView, ShortsCreateView, KhakisCreateView

urlpatterns = [
    url(r'^jeans-create/$', JeansCreateView.as_view(), name='jeans_create_view'),
    url(r'^shorts-create/$', ShortsCreateView.as_view(), name='shorts_create_view'),
    url(r'^khakis-create/$', KhakisCreateView.as_view(), name='khakis_create_view'),
]
