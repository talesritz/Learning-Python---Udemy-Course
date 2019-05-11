from utils import formatacao, validacao, Projeto, Tarefa

formatacao.cabecalho('Udemy - Projetos com Tarefas')

worksheet = list()

while True:

  print('''
  [1] - Cadastrar Projeto
  [2] - Apagar Projeto
  [3] - Mostrar Projetos
  [4] - Sair  
  ''', end='')
  opcao = validacao.leiaInt('Escolha uma opção: ')
  print()


  #[1] - Cadastrar Projeto 
  if opcao == 1:
    tmp = Projeto.cadastrar()
    worksheet.append(tmp)


  #[2] - Apagar projeto
  elif opcao == 2:
    worksheet = Projeto.apagar(worksheet)


  #[3] - Mostrar Projetos
  elif opcao == 3:
    if Projeto.mostrarProjetos(worksheet, ' Mostrar Projetos '):
      
      #Verifica se o usuário deseja manipular o projeto ou voltar ao menu principal
      while True:
        print('''
        [1] - Manipular Projeto
        [2] - Voltar
        ''')
        opcao = validacao.leiaInt('Escolha uma opção: ')
        
        #Manipular Projeto, entra nas funções de Tarefa
        if opcao == 1:
          opproj = validacao.leiaInt('Qual Projeto: ')          
           
          #Executa as rotinas/funções do objeto Tarefa 
          while True: 
            print('\n\033[33m{:-^40}' .format(f' \033[33mProjeto {worksheet[opproj-1].nome} '))
            print('''\033[m
            [1] - Cadastrar Tarefa
            [2] - Concluir Tarefa
            [3] - Visualizar Tarefas
            [4] - Voltar
            ''') 
            opcao = validacao.leiaInt('Escolha uma opção: ')
            

            #Cadastrar Tarefa
            if opcao == 1:
              tmp = Tarefa.cadastrar()
              worksheet[opproj-1].tarefas.append(tmp)
            

            #Concluir Tarefa
            elif opcao == 2:
              Tarefa.concluir(worksheet[opproj-1].tarefas)
            

            #Mostrar lista de Tarefas
            elif opcao == 3:
              Tarefa.mostraLista(worksheet[opproj-1].tarefas)


            #Voltar ao menu Projetos
            elif opcao == 4:
              print('\033[31m--> Voltando a lista de Projetos <--\033[m\n')
              Projeto.mostrarProjetos(worksheet, ' Mostrar Projetos ')
              break
            
            else:
              print('\033[31mOpção Inválida\033[m')
          

        #Volta ao menu principal  
        elif opcao == 2:
          print('\033[31m--> Voltando ao menu Principal <--\033[m\n')
          formatacao.cabecalho('Udemy - Projetos com Tarefas')
          break
    
     
  #[4] - Sair
  elif opcao == 4:
    validacao.sair(' Projetos ')
    break
          
          
  else:
    print('\033[31mOpção Inválida\033[m')

  print()
