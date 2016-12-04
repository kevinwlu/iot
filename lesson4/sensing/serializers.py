from myapp.models import Room, Door
from rest_framework import serializers

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'name')

class DoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Door
        fields = ('url', 'name')
