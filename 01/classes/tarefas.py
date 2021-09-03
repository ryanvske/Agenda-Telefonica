class Tarefas:

    def __init__(self):
        self.__descricao = ''
        self.__data = ''
        self.tarefas = []
    
    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_data(self):
        return self.__descricao

    def set_data(self, data):
        self.__data = data
    
    def criar_tarefa(self,tarefa):
        print('Criando tarefa...')
        descricao = input('Descrição da tarefa>')
        data = input('Data>')
        nova_tarefa = (descricao,data)
        self.tarefas.append(nova_tarefa)
        print()

    def excluir_tarefa(self, indice):
        print()
        print('Excluindo tarefas...')
        self.tarefas.clear()
