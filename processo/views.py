from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .entitys import processo
from .services import proc_services


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
            nume_proc = form.cleaned_data['numero_processo']
            prot_proc = form.cleaned_data['protocolo_processo']
            part_proc = form.cleaned_data['nome_parte_processo']
            assu_proc = form.cleaned_data['assunto_processo']
            aber_proc = form.cleaned_data['data_abertura_processo']
            caix_proc = form.cleaned_data['numero_caixa_processo']
            divi_proc = form.cleaned_data['divisao_processo']
            tipo_proc = form.cleaned_data['tipo_processo']
            arqu_proc = form.cleaned_data['arquivo_processo']

            novo_processo = processo.Processo(numero_processo=nume_proc, protocolo_processo=prot_proc,
                                              nome_parte_processo=part_proc, assunto_processo=assu_proc,
                                              data_abertura_processo=aber_proc, numero_caixa_processo=caix_proc,
                                              divisao_processo=divi_proc, tipo_processo=tipo_proc, arquivo_processo=arqu_proc)

            proc_services.cadastrar_processo(novo_processo)
            # form.save()
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
        return render(request, 'processo/listar.html', {'dados': dados})

    else:
        messages.info(request, 'Sem dados para mostrar!')
        return render(request, 'processo/listar.html')


@login_required
def buscar(request):
    return render(request, 'processo/buscar.html')


@login_required
def config(request):
    return render(request, 'processo/config.html')
