from myapp.models import Dt, Tmp, Cpu
from rest_framework import serializers

class DtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dt
        fields = ('url', 'name')

class TmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tmp
        fields = ('url', 'name')

class CpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cpu
        fields = ('url', 'name')
