# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=50)
