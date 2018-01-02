from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def passthru(request):
    return HttpResponseRedirect(
        reverse('test_location_view') )
