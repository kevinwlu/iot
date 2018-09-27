from django.shortcuts import render
from myapp.models import State
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import StateSerializer
import requests
import json

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

def home(request):
    currentstate = 'empty'
    r = requests.get('http://127.0.0.1:8000/state/1/',
                    auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    currentstate = output['name']
    if currentstate == 'empty':
        occupiedCount = 0
        emptyCount = 1
    else:
        occupiedCount = 1
        emptyCount = 0

    return render(request, 'myapp/index.html',
                            {'currentstate': currentstate,
                            'occupiedCount': occupiedCount,
                            'emptyCount': emptyCount})
