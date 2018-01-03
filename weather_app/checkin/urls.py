from django.urls import path
from django.conf.urls import url, include
from .views import ActualFormView

urlpatterns = [
    url(r'^actualform/$', ActualFormView.as_view(), name='actual_form_view'),

]
