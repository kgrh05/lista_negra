# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Lista_Negra(models.Model):
	msisdn = models.CharField(max_length=12)
	fecha_ingreso = models.DateTimeField()
	razon_ingreso = models.CharField(max_length=320)
	operadora = models.CharField(max_length=25)

	def __str__(self):
		return self.msisdn
