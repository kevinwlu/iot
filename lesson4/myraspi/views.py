from django.shortcuts import render
from myapp.models import LocationData, Dt, Tmp, Cpu
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import DtSerializer, TmpSerializer, CpuSerializer
import requests
import json

# Create your views here.
class DtViewSet(viewsets.ModelViewSet):
    queryset = Dt.objects.all()
    serializer_class = DtSerializer

class TmpViewSet(viewsets.ModelViewSet):
    queryset = Tmp.objects.all()
    serializer_class = TmpSerializer

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

def home(request):
    locData = LocationData.objects.order_by('-id')[0]
    lat = locData.latitude
    lon = locData.longitude

    dtstate = '2019-01-06T00:04:00-05:00'
    r = requests.get('http://127.0.0.1:8000/dt/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    dtstate = output['name']

    tmpstate = '20'
    r = requests.get('http://127.0.0.1:8000/tmp/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    tmpstate = output['name']

    cpustate = '50'
    r = requests.get('http://127.0.0.1:8000/cpu/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    cpustate = output['name']

    return render(request, 'myapp/index.html',
    {'lat': lat, 'lon': lon, 'dtstate':dtstate, 'tmpstate':tmpstate, 'cpustate':cpustate})
