from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def login(request):
    return render(request, 'processo/login.html')

def index(request):
    return render(request, 'processo/index.html')

def cadastrar(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Processo salvo!')
            return redirect(listar)
        else:
            messages.warning(request, 'Houve um erro!')
            return render(request, 'processo/cadastrar.html', {'form': form})

    else:
        form = ProcessoForm()
        return render(request, 'processo/cadastrar.html', {'form': form})


def exibir(request, id):
    obj = get_object_or_404(Processo, pk=id)
    return render(request, 'processo/exibir.html', {'form': obj})

def excluir(request, id):
    obj = get_object_or_404(Processo, pk=id)
    obj.delete()
    messages.info(request, 'Processo removido!')
    return redirect(listar)

def editar(request, id):
    obj = get_object_or_404(Processo, pk=id)
    form = ProcessoForm(instance=obj)

    if request.method == 'POST':
        form = ProcessoForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações salvas!')
            return HttpResponseRedirect('/listar/')
        else:
            return render(request, 'processo/editar.html', {'form': form, 'obj': obj})
    else:
        return render(request, 'processo/editar.html', {'form': form, 'obj': obj})

def listar(request):
    dados = Processo.objects.all()
    if dados:
        return render(request, 'processo/listar.html', {'dados':dados})

    else:
        messages.info(request, 'Sem dados para mostrar!')
        return render(request, 'processo/listar.html')

def buscar(request):
    return render(request, 'processo/buscar.html')

def config(request):
    return render(request, 'processo/config.html')