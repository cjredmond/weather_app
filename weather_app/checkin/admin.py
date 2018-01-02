from django.contrib import admin
from .models import Checkin, Top, Bottom, Shoes

admin.site.register([Checkin, Top, Bottom, Shoes])
