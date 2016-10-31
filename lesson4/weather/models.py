from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LocationData(models.Model):
    location = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    def __unicode__(self):
        return self.location

class Dt(models.Model):
    name = models.CharField(max_length=30)

class Tmp(models.Model):
    name = models.CharField(max_length=50)

class Hmd(models.Model):
    name = models.CharField(max_length=50)
