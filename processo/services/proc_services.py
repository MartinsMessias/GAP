from ..models import *


def cadastrar_processo(new):
    Processo.objects.create(
        numero_processo=new.numero_processo, protocolo_processo=new.protocolo_processo,
        nome_parte_processo=new.nome_parte_processo, assunto_processo=new.assunto_processo,
        data_abertura_processo=new.data_abertura_processo, numero_caixa_processo=new.numero_caixa_processo,
        divisao_processo=new.divisao_processo, tipo_processo=new.tipo_processo, arquivo_processo=new.arquivo_processo
    )

#
# def listar_arquivos():
#     arquivos = FileUDApp.objects.all()
#     return arquivos
#
#
# def listar_arquivo_id(id):
#     arquivo = FileUDApp.objects.get(id=id)
#     return arquivo
#
#
# def remover_arquivo(arquivo):
#     arquivo.delete()
#
#
# def upload_arquivo(novo):
#     FileUDApp.objects.create(
#         nome_arquivo=novo.nome_arquivo,
#         tipo_arquivo=novo.tipo_arquivo,
#         arquivo=novo.arquivo
#     )
#
#
# def alterar_arquivo(arquivo, novo):
#     arquivo.nome_arquivo = novo.nome_arquivo
#     arquivo.tipo_arquivo = novo.tipo_arquivo
#     arquivo.arquivo = novo.arquivo
#     arquivo.save(force_update=True)
