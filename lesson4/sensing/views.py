# Django views for REST services and home automation application - views.py

from myapp.models import Room, Door
from rest_framework import viewsets
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.serializers import RoomSerializer, DoorSerializer
import requests
import json

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

def home(request):
    roomstate = 'no'
    r = requests.get('http://127.0.0.1:8000/room/1/', auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    roomstate = output['name']

    doorstate = 'closed'
    r = requests.get('http://127.0.0.1:8000/door/1/', auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    doorstate = output['name']

    return render_to_response('myapp/index.html',
                             {'roomstate':roomstate, 'doorstate':doorstate},
                             context_instance=RequestContext(request))
