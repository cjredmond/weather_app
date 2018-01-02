from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    

]
