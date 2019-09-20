import os

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import *

from GProcessos import settings
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
    dados = Processo.objects.all().order_by('criacao_registro')

    if not dados:
        messages.info(request, 'Nenhum processo foi encontrado!')
        return render(request, 'processo/index.html')

    return render(request, 'processo/index.html', {'dados': dados})


@login_required
def divisao(request):
    dados = Divisao.objects.all()

    if not dados:
        messages.info(request, 'Nenhuma divisão foi encontrada!')
        return render(request, 'processo/divisoes.html')

    return render(request, 'processo/divisoes.html', {'dados': dados})


@login_required
def cadastrar(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST, request.FILES)

        if not form.is_valid():
            messages.warning(request, 'Houve um erro!')
            return render(request, 'processo/cadastrar.html', {'form': form})

        nume_proc = form.cleaned_data['numero_processo']
        prot_proc = form.cleaned_data['protocolo_processo']
        part_proc = form.cleaned_data['nome_parte_processo']
        assu_proc = form.cleaned_data['assunto_processo']
        aber_proc = form.cleaned_data['data_abertura_processo']
        caix_proc = form.cleaned_data['numero_caixa_processo']
        divi_proc = form.cleaned_data['divisao_processo']
        tipo_proc = form.cleaned_data['tipo_processo']
        arqu_proc = form.cleaned_data['arquivo_processo']

        if proc_services.verificar_exist_numproc(nume_proc=nume_proc):
            messages.warning(request, 'Já existe um processo com esse número!')
            return render(request, 'processo/cadastrar.html', {'form': form})

        if proc_services.verificar_exist_numprot(nume_prot=prot_proc):
            messages.warning(request, 'Já existe um processo com esse protocolo!')
            return render(request, 'processo/cadastrar.html', {'form': form})

        novo_processo = processo.Processo(numero_processo=nume_proc, protocolo_processo=prot_proc,
                                          nome_parte_processo=part_proc, assunto_processo=assu_proc,
                                          data_abertura_processo=aber_proc, numero_caixa_processo=caix_proc,
                                          divisao_processo=divi_proc, tipo_processo=tipo_proc,
                                          arquivo_processo=arqu_proc)

        proc_services.cadastrar_processo(novo_processo)
        messages.success(request, 'Processo salvo!')
        return redirect(index)

    else:

        form = ProcessoForm()
        return render(request, 'processo/cadastrar.html', {'form': form})


@login_required
def excluir(request, id):
    proc_services.remover_processo(proc_services.busca_processo(id))
    messages.info(request, 'Processo removido!')
    return redirect(index)


@login_required
def editar(request, id):
    processo_ant = proc_services.busca_processo(id)
    form = ProcessoForm(request.POST or None, request.FILES or None, instance=processo_ant)

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
                                          divisao_processo=divi_proc, tipo_processo=tipo_proc,
                                          arquivo_processo=arqu_proc)

        proc_services.editar_processo(processo_ant, new=novo_processo)
        messages.info(request, 'Alterações salvas!')
        return redirect(index)

    return render(request, 'processo/editar.html', {'form': form})


@login_required
def editar_divisao(request, id):
    div_ant = proc_services.busca_div(id)
    form = DivisaoForm(request.POST or None, request.FILES or None, instance=div_ant)

    if form.is_valid():
        nome_divisao = form.cleaned_data['nome_divisao']

        nova_div = processo.DivisaoProcesso(divisao=nome_divisao)

        proc_services.editar_divisao(div_ant, new=nova_div)
        messages.info(request, 'Alterações salvas!')
        return redirect(divisao)
    return render(request, 'processo/editar_div.html', {'form': form})


@login_required
def excluir_div(request, id):
    if proc_services.verificar_exist_pro_div(proc_services.busca_div(id)):
        messages.warning(request, 'Você não pode remover essa divisão! Ela contém processos cadastrados!')
        return redirect(divisao)
    proc_services.remover_divisao(proc_services.busca_div(id))
    messages.info(request, 'Divisão removida!')
    return redirect(divisao)


@login_required
def cadastrar_div(request):
    if request.method == 'POST':
        form = DivisaoForm(request.POST, request.FILES)

        if not form.is_valid():
            messages.warning(request, 'Houve um erro!')
            return render(request, 'processo/editar_div.html', {'form': form})

        nome_divisao = form.cleaned_data['nome_divisao']

        if proc_services.verificar_exist_div(div=nome_divisao):
            messages.warning(request, 'Já existe uma divisão com esse nome!')
            return render(request, 'processo/cadastrar_div.html', {'form': form})

        nova_div = processo.DivisaoProcesso(nome_divisao=nome_divisao)
        proc_services.cadastrar_processo(nova_div)
        messages.success(request, 'Divisão salva!')
        return redirect(index)

    else:
        form = DivisaoForm()
        return render(request, 'processo/editar_div.html', {'form': form})