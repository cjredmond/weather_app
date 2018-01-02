from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from weather_api.views import TestLocationView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('user_authentication.urls')),
    url(r'^', include('weather_api.urls')),
    # url(r'^test/$', TestLocationView.as_view(), name = 'test')
]
