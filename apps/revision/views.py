# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from forms import revisionForm
from models import revisar

# Create your views here.

def index(request):
	return render(request, 'revision/index.html')


def revision_view(request):
	if request.method == 'POST':
		form = revisionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('revision:index')
	else: 
		form = revisionForm()

	return render(request, 'revision/formulario.html', {'form': form})


def lista_revision(request):
	revisar1 = revisar.objects.all().order_by('id')
	contexto = {'lista_revisar': revisar1}
	return render(request, 'revision/lista_revision.html', contexto)


def editar_revision(request, id_revisar):
	revisar1 = revisar.objects.get(id=id_revisar)
	if request.method == 'GET':
		form = revisionForm(instance=revisar1)
	else:
		form = revisionForm(request.POST, instance=revisar1)
		if form.is_valid():
			form.save()
		return redirect('revision:revision_lista')
	return render(request, 'revision/formulario.html', {'form':form})

def eliminar_revision(request, id_revisar):
	revisar1 = revisar.objects.get(id=id_revisar)
	contexto = {'lista_eliminar': revisar1}
	if request.method == 'POST':
		revisar1.delete()
		return redirect('revision:revision_lista')
	return render(request, 'revision/eliminar_revision.html', contexto)

