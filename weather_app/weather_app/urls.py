from django.contrib import admin
from django.urls import path
from django.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('user_authentication.urls')),
]
