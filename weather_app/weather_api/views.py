from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.gis.geoip2 import GeoIP2
import geoip2.webservice

import requests, json
from datetime import datetime

from checkin.models import Checkin, Clothes
from checkin.forms import ClothesForm


def weather_compare_tommorow(temp):
    pass

def five_day_forecast(zip_code):
    ls = []
    base_api_url = 'http://api.openweathermap.org/data/2.5/forecast?zip={}&APPID=5c255f05d7304e6c3f8ab54d953f5e5b'
    req = requests.get(base_api_url.format(zip_code))
    data = json.loads(req.text)
    for x in data['list']:
        date = x['dt_txt'].split(' ')
        if datetime.now().date().strftime('%Y-%m-%d') == x['dt_txt'].split(' ')[0]:
            pass
        else:
            if date[1] == '18:00:00':
                ls.append(
                    {'date': x['dt_txt'].split(' ')[0],
                     'weather': x['weather'][0]['description'],
                     'temp': int(x['main']['temp'] * 9/5 - 459.67)}
                )
                print(x['main']['temp'])
                print(int(x['main']['temp'] * 9/5 - 459.67))
                # print('\n\n')

    return ls

def predict_clothes():
    x = Clothes.objects.last()


#print(five_day_forecast())

# def get_user_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

class TestLocationView(TemplateView):
    template_name = 'test_location_view.html'

    def initiate_data(self):
        g = GeoIP2()
        ip_address = g.city('96.37.241.230')
        zip_code = ip_address['postal_code']

        base_api_url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&APPID=5c255f05d7304e6c3f8ab54d953f5e5b'
        req = requests.get(base_api_url.format(zip_code))
        data = json.loads(req.text)

        temp = int(data['main']['temp'] * 9/5 - 459.67)
        desc = data['weather'][0]['description']

        user_checkins = Checkin.objects.filter(user=self.request.user).order_by('-date')

        if not user_checkins.filter(date=datetime.now().date()):
            Checkin.objects.create(user=self.request.user,temp=temp,desc=desc)

        five_day_forecast_data = five_day_forecast(29601)
        return [temp, desc, user_checkins, five_day_forecast_data]

    def get_context_data(self):
        context = super().get_context_data()
        # c = geoip2.webservice.Client(0,'l')
        # response = c.city('96.37.241.230')
        data_list = self.initiate_data()

        context['checkin_today'] = data_list[2].first()
        context['clothes_form'] = ClothesForm
        context['date'] = datetime.now().date()
        context['temp'] = data_list[0]
        context['desc'] = data_list[1]
        context['checkins_archive'] = data_list[2].exclude(date=datetime.now().date())
        context['five_day_forecast_data'] = data_list[3]

        return context
