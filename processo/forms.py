from django import forms

from .models import *


class ProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo
        fields = ('numero_processo', 'protocolo_processo',
                  'nome_parte_processo', 'assunto_processo',
                  'data_abertura_processo', 'numero_caixa_processo',
                  'divisao_processo', 'tipo_processo', 'arquivo_processo')

