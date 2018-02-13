from django.db import models

# Create your models here.
class LocationData(models.Model):
    location = models.CharField(max_length=30)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    def __str__(self):
        return self.location

class Dt(models.Model):
    name = models.CharField(max_length=30)

class Tmp(models.Model):
    name = models.CharField(max_length=50)

class Hmd(models.Model):
    name = models.CharField(max_length=50)
