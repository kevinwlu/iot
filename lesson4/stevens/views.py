# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from myapp.models import TemperatureData
from django.template import RequestContext

# Create your views here.
def home(request):
    tempData = TemperatureData.objects.order_by('-id')[0]
    timestamp = tempData.timestamp
    temperature = tempData.temperature
    lat = tempData.lat
    lon = tempData.lon

    return render(request, 'myapp/index.html', {'timestamp': timestamp,
    'temperature': temperature, 'lat': lat, 'lon': lon})
