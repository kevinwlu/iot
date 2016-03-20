# Django views for REST service and smart parking application - views.py

from myapp.models import State
from rest_framework import viewsets
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.serializers import StateSerializer
import requests
import json

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

def home(request):
    currentstate = 'empty'
    r = requests.get('http://127.0.0.1:8000/state/1/',
                    auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    currentstate = output['name']
    if currentstate == 'empty':
        occupiedCount = 0
        emptyCount = 1
    else:
        occupiedCount = 1
        emptyCount = 0

    return render_to_response('myapp/index.html',
                            {'currentstate': currentstate,
                            'occupiedCount': occupiedCount,
                            'emptyCount': emptyCount},
                            context_instance=RequestContext(request))
