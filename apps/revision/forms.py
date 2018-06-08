from django import forms
from models import revisar

class revisionForm(forms.ModelForm):

	class Meta:
		model = revisar

		fields = [
			'msisdn',
			'fecha_ingreso',
			'razon_ingreso',
			'operadora',
		]
		labels = {
			'msisdn': 'Msisdn',
			'fecha_ingreso': 'Fecha Ingreso',
			'razon_ingreso': 'Razon Ingreso',
			'operadora': 'Operadora',
		}
		widgets = {
			'msisdn': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_ingreso': forms.DateInput(attrs={'class':'form-control'}),
			'razon_ingreso': forms.TextInput(attrs={'class':'form-control'}),
			'operadora': forms.TextInput(attrs={'class':'form-control'}),
		}