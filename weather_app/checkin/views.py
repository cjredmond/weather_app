from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, FormView
from .models import Checkin, Top, Bottom, Shoes
from .forms import TopForm, BottomForm, ShoesForm, ActualForm

class TopCreateView(CreateView):
    model = Top
    fields = ['tank', 't_shirt', 'long_sleeve_shirt', 'sweater', 'jacket']
    def get_success_url(self):
        return reverse('test_location_view')
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.checkin = self.request.user.checkin_set.all().last()
        return super().form_valid(form)

class BottomCreateView(CreateView):
    model = Top
    fields = ['shorts', 'jeans', 'khakis']
    def get_success_url(self):
        return reverse('test_location_view')
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.checkin = self.request.user.checkin_set.all().last()
        return super().form_valid(form)

class ShoesCreateView(CreateView):
    model = Top
    fields = ['sneakers', 'boots', 'flip_flops']
    def get_success_url(self):
        return reverse('test_location_view')
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.checkin = self.request.user.checkin_set.all().last()
        return super().form_valid(form)

class ActualFormView(FormView):
    form_class = ActualForm

    def form_valid(self, form):
        return super(ActualFormView, self).form_valid(form)
