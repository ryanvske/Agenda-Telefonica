from classes.agenda import Agenda
from classes.contato import Contato
from classes.tarefas import Tarefas

contato = Contato()
agenda = Agenda()
tarefas = Tarefas()

while True:
    print('      Menu')
    print('1.Cadastrar contato')
    print('2.Listar contatos')
    print('3.Excluir contatos')
    print('4.Criar tarefa')
    print('5.Listar tarefa')
    print('6.Exluir tarefa')
    print('7.Sair')
    print()

    escolha_menu = input('Como deseja proseguir?>')
    executando= True

    if escolha_menu == '7':
        break
    elif escolha_menu == '1':
        contato.cadastrar_contato(contato)
    elif escolha_menu == '2':
        print('contatos ' + str(contato.contatos))
    elif escolha_menu == '3':
        indice = input('Digite o id que você deseja excluir: ')
        contato.excluir_contato(indice)
    elif escolha_menu == '4':
        tarefas.criar_tarefa(tarefas)
    elif escolha_menu == '5':
        print('tarefas ' + str(tarefas.tarefas))
    elif escolha_menu == '6':
        tarefas.excluir_tarefa(tarefas)
        