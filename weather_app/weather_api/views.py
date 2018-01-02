from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.gis.geoip2 import GeoIP2
import geoip2.webservice

# def get_user_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

class TestLocationView(TemplateView):
    template_name = 'test_location_view.html'

    def get_context_data(self):
        context = super().get_context_data()
        # c = geoip2.webservice.Client(0,'l')
        # response = c.city('96.37.241.230')
        g = GeoIP2()
        x = g.city('96.37.241.230')
        print(x)

        return context
