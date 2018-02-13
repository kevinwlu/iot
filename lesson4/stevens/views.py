from django.shortcuts import render
from myapp.models import TemperatureData
from django.template import RequestContext

# Create your views here.
def home(request):
    tempData = TemperatureData.objects.order_by('-id')[0]
    date_time = tempData.date_time
    temperature = tempData.temperature
    lat = tempData.latitude
    lon = tempData.longitude

    return render(request, 'myapp/index.html', {'date_time': date_time,
    'temperature': temperature, 'lat': lat, 'lon': lon})
