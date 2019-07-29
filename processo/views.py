from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

@login_required
def accounts(request):
    return HttpResponse(404)

@login_required
def login(request):
    return render(request, 'registration/login.html')

@login_required
def index(request):
    return render(request, 'processo/index.html')

@login_required
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

@login_required
def exibir(request, id):
    obj = get_object_or_404(Processo, pk=id)
    return render(request, 'processo/exibir.html', {'form': obj})

@login_required
def excluir(request, id):
    obj = get_object_or_404(Processo, pk=id)
    obj.delete()
    messages.info(request, 'Processo removido!')
    return redirect(listar)

@login_required
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

@login_required
def listar(request):
    dados = Processo.objects.all()
    if dados:
        return render(request, 'processo/listar.html', {'dados':dados})

    else:
        messages.info(request, 'Sem dados para mostrar!')
        return render(request, 'processo/listar.html')

@login_required
def buscar(request):
    return render(request, 'processo/buscar.html')


@login_required
def config(request):
    return render(request, 'processo/config.html')