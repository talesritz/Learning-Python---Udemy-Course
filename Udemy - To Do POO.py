from utils import formatacao, validacao, Tarefa


formatacao.cabecalho('Udemy - To Do POO')

casa = list()

while True:

  print('''
  [1] - Cadastrar tarefa
  [2] - Concluir tarefa
  [3] - Mostrar tarefas
  [4] - Sair
  ''', end='')
  opcao = validacao.leiaInt('Escolha uma opção: ')
  print()
  

  if opcao == 1:
    tmp = Tarefa.cadastrar('Descrição: ')
    casa.append(tmp) 
   
  elif opcao == 2:
    Tarefa.concluir(casa)
    
  elif opcao == 3: 
    Tarefa.mostraLista(casa)

  elif opcao == 4:
    validacao.sair()
    break
    
  else:
    print('\033[31mOpção Inválida\033[m')
  
  print()

