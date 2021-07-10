from myapp.models import Dt, Mem, Cpu
from rest_framework import serializers

class DtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dt
        fields = ('url', 'name')

class MemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mem
        fields = ('url', 'name')

class CpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cpu
        fields = ('url', 'name')
