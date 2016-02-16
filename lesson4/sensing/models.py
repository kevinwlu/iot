# Django model for room and door REST services - models.py

from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)

class Door(models.Model):
    name = models.CharField(max_length=50)
