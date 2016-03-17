from django.db import models

class TemperatureData(models.Model):
    timestamp = models.CharField(max_length=30)
    temperature = models.CharField(max_length=5)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    def __unicode__(self):
        return self.timestamp
