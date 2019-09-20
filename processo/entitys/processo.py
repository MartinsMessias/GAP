class Processo:

    def __init__(self, numero_processo, protocolo_processo, nome_parte_processo, assunto_processo,
                 data_abertura_processo, numero_caixa_processo, divisao_processo, tipo_processo, arquivo_processo):
        self.__numero_proc = numero_processo
        self.__protocolo_proc = protocolo_processo
        self.__nome_parte_proc = nome_parte_processo
        self.__assunto_proc = assunto_processo
        self.__data_abertura_proc = data_abertura_processo
        self.__numero_caixa_proc = numero_caixa_processo
        self.__divisao_proc = divisao_processo
        self.__tipo_processo = tipo_processo
        self.__arquivo_processo = arquivo_processo

    # ----
    @property
    def numero_processo(self):
        return self.__numero_proc

    @numero_processo.setter
    def numero_processo(self, numero_proc):
        self.__numero_proc = numero_proc

    # ----
    @property
    def protocolo_processo(self):
        return self.__protocolo_proc

    @protocolo_processo.setter
    def protocolo_processo(self, protocolo):
        self.__protocolo_proc = protocolo

    # ----
    @property
    def nome_parte_processo(self):
        return self.__nome_parte_proc

    @nome_parte_processo.setter
    def nome_parte_processo(self, par):
        self.__nome_parte_proc = par

    # ----
    @property
    def assunto_processo(self):
        return self.__assunto_proc

    @assunto_processo.setter
    def assunto_processo(self, assunto):
        self.__assunto_proc = assunto

    # ----
    @property
    def data_abertura_processo(self):
        return self.__data_abertura_proc

    @data_abertura_processo.setter
    def data_abertura_processo(self, data):
        self.__data_abertura_proc = data

    # ----
    @property
    def numero_caixa_processo(self):
        return self.__numero_caixa_proc

    @numero_caixa_processo.setter
    def caixa(self, caixap):
        self.__numero_caixa_proc = caixap

    # ----
    @property
    def divisao_processo(self):
        return self.__divisao_proc

    @divisao_processo.setter
    def divisao_processo(self, divisao):
        self.__divisao_proc = divisao

    # ----
    @property
    def tipo_processo(self):
        return self.__tipo_processo

    @tipo_processo.setter
    def tipo_processo(self, tipo):
        self.__tipo_processo = tipo

    # ----
    @property
    def arquivo_processo(self):
        return self.__arquivo_processo

    @arquivo_processo.setter
    def arquivo_processo(self, arq):
        self.__arquivo_processo = arq


# ------------------
class TipoProcesso:

    def __init__(self, nome_tipo):
        self.__nome_tipo = nome_tipo

    @property
    def nome_tipo_processo(self):
        return self.__nome_tipo

    @nome_tipo_processo.setter
    def nome_tipo_processo(self, nometipo):
        self.__nome_tipo = nometipo


# -----------------
class DivisaoProcesso:

    def __init__(self, divisao):
        self.__nome_divisao = divisao

    @property
    def nome_divisao(self):
        return self.__nome_divisao

    @nome_divisao.setter
    def nome_divisao(self, new_nome_divisao):
        self.__nome_divisao = new_nome_divisao
