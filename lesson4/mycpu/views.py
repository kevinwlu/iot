from django.shortcuts import render
from myapp.models import LocationData, Dt, Mem, Cpu
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import DtSerializer, MemSerializer, CpuSerializer
import requests
import json

# Create your views here.
class DtViewSet(viewsets.ModelViewSet):
    queryset = Dt.objects.all()
    serializer_class = DtSerializer

class MemViewSet(viewsets.ModelViewSet):
    queryset = Mem.objects.all()
    serializer_class = MemSerializer

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

def home(request):
    locData = LocationData.objects.order_by('-id')[0]
    lat = locData.latitude
    lon = locData.longitude

    dtstate = '2021'
    r = requests.get('http://127.0.0.1:8000/dt/1/', auth=('admin', 'admin'))
    result = r.text
    output = json.loads(result)
    dtstate = output['name']

    memstate = '20'
    r = requests.get('http://127.0.0.1:8000/mem/1/', auth=('admin', 'admin'))
    result = r.text
    output = json.loads(result)
    memstate = output['name']

    cpustate = '20'
    r = requests.get('http://127.0.0.1:8000/cpu/1/', auth=('admin', 'admin'))
    result = r.text
    output = json.loads(result)
    cpustate = output['name']

    return render(request, 'myapp/index.html',
    {'lat': lat, 'lon': lon, 'dtstate':dtstate, 'memstate':memstate, 'cpustate':cpustate})
