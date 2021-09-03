class Contato:

    def __init__(self):
        self.__nome = ''
        self.__numero = ''
        self.contatos = []
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero
        
    def cadastrar_contato(self,contato):
        print('Cadastrando contato...')
        nome = input('Nome>')
        numero = input('Numero>')
        novo_contato = (nome,numero)
        self.contatos.append(novo_contato)
        print()

    def excluir_contato(self):
        print()
        print('Excluindo contato...')
        self.contatos.clear()
