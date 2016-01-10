from django.shortcuts import render_to_response
from myapp.models import TemperatureData
from django.template import RequestContext

def home(request):
    tempData = TemperatureData.objects.order_by('-id')[0]
    timestamp = tempData.timestamp
    temperature = tempData.temperature
    lat = tempData.lat
    lon = tempData.lon

    return render_to_response('myapp/index.html', {'timestamp': timestamp,
    'temperature': temperature,
    'lat': lat, 'lon': lon}, context_instance=RequestContext(request))