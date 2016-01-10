# Django model for REST service - models.py

from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)