from myapp.models import Dt, Tmp, Hmd
from rest_framework import serializers

class DtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dt
        fields = ('url', 'name')

class TmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tmp
        fields = ('url', 'name')

class HmdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hmd
        fields = ('url', 'name')
