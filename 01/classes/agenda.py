class Agenda:

    def __init__(self):
        self.__proprietario = ''
        self.__ano = ''
        self.tarefas = []

        
    def get_proprietario(self):
        return self.__proprietario

    def set_proprietario(self, proprietario):
        self.__proprietario = proprietario

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    

