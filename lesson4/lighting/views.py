from django.shortcuts import render
from myapp.models import Mode, State
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import ModeSerializer, StateSerializer
import requests
import json

# Create your views here.
class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

def home(request):
    out = ''
    currentmode = 'auto'
    currentstate = 'off'

    if 'on' in request.POST:
        values = {"name": "on"}
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('pi', 'raspberry'))
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'off' in request.POST:
        values = {"name": "off"}
        r = requests.put('http://127.0.0.1:8000/state/1/',
                        data=values, auth=('pi', 'raspberry'))
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'auto' in request.POST:
        values = {"name": "auto"}
        r = requests.put('http://127.0.0.1:8000/mode/1/',
                        data=values, auth=('pi', 'raspberry'))
        result = r.text
        output = json.loads(result)
        out = output['name']
    if 'manual' in request.POST:
        values = {"name": "manual"}
        r = requests.put('http://127.0.0.1:8000/mode/1/',
                        data=values, auth=('pi', 'raspberry'))
        result = r.text
        output = json.loads(result)
        out = output['name']

    r = requests.get('http://127.0.0.1:8000/mode/1/',
                    auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    currentmode = output['name']

    r = requests.get('http://127.0.0.1:8000/state/1/',
                    auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    currentstate = output['name']

    return render(request, 'myapp/index.html', {'name':out,
    'currentmode':currentmode, 'currentstate':currentstate})
