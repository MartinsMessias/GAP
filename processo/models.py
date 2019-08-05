from django.db import models

# Create your models here.
class Divisao(models.Model):
    nome_divisao = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.nome_divisao


class TipoDeProcesso(models.Model):
    nome_tipo = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.nome_tipo

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'processos/{0}/{1}/{2}'.format(instance.divisao_processo, instance.tipo_processo, filename)

class Processo(models.Model):
    numero_processo = models.CharField(max_length=100, blank=False, null=False)
    protocolo_processo = models.CharField(max_length=100, blank=False, null=False)
    nome_parte_processo = models.CharField(max_length=100, blank=False, null=False)
    assunto_processo = models.CharField(max_length=250, blank=False, null=False)
    data_abertura_processo = models.DateField(blank=False, null=False)
    numero_caixa_processo = models.IntegerField()
    divisao_processo = models.ForeignKey(Divisao, on_delete=models.CASCADE)
    tipo_processo = models.ForeignKey(TipoDeProcesso, on_delete=models.CASCADE)
    arquivo_processo = models.FileField(upload_to=user_directory_path, default='sem_arquivo')
    criacao_registro = models.DateField(auto_now_add=True)
    modificacao_registro = models.DateField(auto_now=True)

    def __str__(self):
        return self.assunto_processo