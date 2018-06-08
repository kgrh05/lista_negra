from rest_framework import serializers 
from .models import Lista_Negra


class Lista_Negra_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Lista_Negra
		fields = ('id', 'msisdn', 'fecha_ingreso', 'razon_ingreso', 'operadora')

