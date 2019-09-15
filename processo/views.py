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
    dados = Processo.objects.all()

    if not dados:
        messages.info(request, 'Nenhum processo foi encontrado!')
        return render(request, 'processo/index.html')

    return render(request, 'processo/index.html', {'dados': dados})


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
    form = ProcessoForm(request.POST or None, instance=processo_ant)

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


