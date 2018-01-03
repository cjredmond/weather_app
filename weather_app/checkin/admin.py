from django.contrib import admin
from .models import Checkin, Clothes

admin.site.register([Checkin, Clothes])
