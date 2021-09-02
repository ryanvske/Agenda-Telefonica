class Contato:

    def __init__(self):
        self.__nome = ''
        self.__numero = ''

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero
        