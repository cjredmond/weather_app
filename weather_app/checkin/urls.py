from django.urls import path
from django.conf.urls import url, include
from .views import ClothesCreateView

urlpatterns = [
    url(r'^clothes-create/$', ClothesCreateView.as_view(), name='clothes_create_view'),
]
