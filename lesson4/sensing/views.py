from django.shortcuts import render
from myapp.models import Room, Door
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import RoomSerializer, DoorSerializer
import requests
import json

# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

def home(request):
    roomstate = 'no'
    r = requests.get('http://127.0.0.1:8000/room/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    roomstate = output['name']

    doorstate = 'closed'
    r = requests.get('http://127.0.0.1:8000/door/1/', auth=('pi', 'raspberry'))
    result = r.text
    output = json.loads(result)
    doorstate = output['name']

    return render(request, 'myapp/index.html',
                            {'roomstate':roomstate, 'doorstate':doorstate})
