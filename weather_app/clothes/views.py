from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Jeans, Shorts, Khakis

class JeansCreateView(CreateView):
    model = Jeans
    fields = []
    def get_success_url(self):
        return '/'
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.checkin = self.request.user.checkin_set.all().last()
        instance.user = self.request.user
        return super().form_valid(form)

class ShortsCreateView(CreateView):
    model = Shorts
    fields = []
    def get_success_url(self):
        return '/'
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.checkin = self.request.user.checkin_set.all().last()
        instance.user = self.request.user
        return super().form_valid(form)

class KhakisCreateView(CreateView):
    model = Khakis
    fields = []
    def get_success_url(self):
        return '/'
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.checkin = self.request.user.checkin_set.all().last()
        instance.user = self.request.user
        return super().form_valid(form)
