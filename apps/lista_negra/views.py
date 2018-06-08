import json

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Lista_Negra
from .serializers import Lista_Negra_Serializer


class Lista_Negra_View(viewsets.ModelViewSet):
	queryset = Lista_Negra.objects.all()
	serializer_class = Lista_Negra_Serializer







	