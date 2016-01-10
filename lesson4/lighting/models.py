# Django model for mode and state REST services - models.py

from django.db import models

class Mode(models.Model):
    name = models.CharField(max_length=50)

class State(models.Model):
    name = models.CharField(max_length=50)
