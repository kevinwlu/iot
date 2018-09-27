from django.shortcuts import render
from myapp.models import LocationData, Dt, Tmp, Hmd
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import DtSerializer, TmpSerializer, HmdSerializer
import requests
import json

# Create your views here.
class DtViewSet(viewsets.ModelViewSet):
    queryset = Dt.objects.all()
    serializer_class = DtSerializer

class TmpViewSet(viewsets.ModelViewSet):
    queryset = Tmp.objects.all()
    serializer_class = TmpSerializer

class HmdViewSet(viewsets.ModelViewSet):
    queryset = Hmd.objects.all()
    serializer_class = HmdSerializer

def home(request):
    locData = LocationData.objects.order_by('-id')[0]
    lat = locData.latitude
    lon = locData.longitude

    dtstate = '2018-10-01T14:00:00-05:00'
    r = requests.get('http://127.0.0.1:8000/dt/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    dtstate = output['name']

    tmpstate = '20'
    r = requests.get('http://127.0.0.1:8000/tmp/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    tmpstate = output['name']

    hmdstate = '50'
    r = requests.get('http://127.0.0.1:8000/hmd/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    hmdstate = output['name']

    return render(request, 'myapp/index.html',
    {'lat': lat, 'lon': lon, 'dtstate':dtstate, 'tmpstate':tmpstate, 'hmdstate':hmdstate})
