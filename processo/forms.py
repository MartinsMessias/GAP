from django import forms

from .models import *


class ProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo
        fields = ('numero_processo', 'protocolo_processo',
                  'nome_parte_processo', 'assunto_processo',
                  'data_abertura_processo', 'numero_caixa_processo',
                  'divisao_processo', 'tipo_processo', 'arquivo_processo')

        def _init_(self, *args, **kwargs):
            for l in self.base_fields:
                self.base_fields[l].widget.attrs['class'] = '"form-control"'

            super(ProcessoForm, self)._init_(*args, **kwargs)
