# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class revisar(models.Model):
	msisdn = models.CharField(max_length=12)
	fecha_ingreso = models.DateField()
	razon_ingreso = models.CharField(max_length=320)
	operadora = models.CharField(max_length=25)