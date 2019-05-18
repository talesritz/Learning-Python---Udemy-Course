from datetime import datetime
from utils import validacao

class Tarefa:

  def __init__(self, descricao, vencimento=False):
    self.descricao = descricao
    self.feito = False
    self.criacao = datetime.now()
    self.vencimento = vencimento 
  
  def __str__(self):
    return f'1;32mDescrição: {self.descricao} \nStatus: {self.feito} \nCriação: {self.criacao}'


#Conclui a tarefa cadastrada na lista da casa
def concluir(lista):
    
  print('{:-^40}' .format(' Concluir '))
  if len(lista) == 0:
    print('{:^40}' .format('\033[33mNão há dados a serem exibidos\033[m'))
  else:
    print('')
    for count in range(0, len(lista)):
      print(f'{count+1} - {lista[count].descricao}')
        
    opcao = validacao.leiaInt('Selecione uma opção: ')
    lista[opcao-1].feito = True 

  print('-'*40)   
  return lista


#cadastra uma nova tarefa e retorna o obj Tarefa
def cadastrar():

  print('{:-^40}' .format(' Cadastrar '))
  tmp = Tarefa(validacao.leiaStr('Descrição '))
  print('-'*40)
  
  mostraItem(tmp) 

  return tmp

#Mostra a lista completa dos itens presentas na lista de tarefas
def mostraLista(lista):
  print('{:-^40}' .format(' Mostrar '))
  print()
  if len(lista) == 0:
    print('\033[1;33mNão há dados a serem exibidos\033[m')
  else:
    for count in range(0, len(lista)):
      if lista[count].feito:
        print('\033[32m', end='')
      else:
        print('\033[31m', end='')
     
      print('{:-^40}' .format(f' Tarefa {count+1} '))
       
      print(f'Descrição: {lista[count].descricao} \nStatus: {lista[count].feito} \nCriação: {lista[count].criacao} \n')
      print('\033[m', end='')

  

#mostra Item individual, usado para confirmar que o obj foi cadastrado com sucesso na função cadastrar()
def mostraItem(obj):
  print('\033[32m{:-^40}' .format(' \033[32mCadastrado com sucesso '))
   
  print(f'Descrição: {obj.descricao} \n\033[31mStatus: {obj.feito} \n\033[32mCriação: {obj.criacao}')
  print('\033[m')
