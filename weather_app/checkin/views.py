from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, FormView
from .models import Checkin, Clothes
from .forms import ClothesForm

# class ActualFormView(FormView):
#     form_class = ActualForm
#
#     def form_valid(self, form):
#         return super(ActualFormView, self).form_valid(form)

class ClothesCreateView(CreateView):
    form_class = ClothesForm
    template_name = 'checkin/clothes_create_view.html'
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.checkin = self.request.user.checkin_set.all().last()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('test_location_view')
