from utils import validacao
from datetime import datetime

class Projeto:
  def __init__(self, nome):
    self.nome = nome
    self.tarefas = list()
    self.status = False
    self.criacao = datetime.now()

  def __str__(self):
    return f'Descrição: {self.nome} \nTarefas: {self.tarefas} \nStatus: {self.status} \nCriação: {self.criacao}'
  

#Cadastra um obj do tipo Projeto
def cadastrar():
  print('{:-^40}' .format(' Cadastrar '))
  tmp = Projeto(validacao.leiaStr('Descrição: '))
  
  print('\n\033[32mCADASTRO EFETUADO')
  mostrarItem(tmp)

  return tmp
  

#Mostra apenas os nomes dos Projetos que estão cadastrados dentro da lista
def mostrarProjetos(lista, menu = ''): 
  print('{:-^40}' .format(f'{menu}'))

  if len(lista) == 0:
    print('\033[33mNÃO HÁ REGISTROS\033[m\n')
    return False
  else:
    for count in range(0, len(lista)):
      print(f'{count+1} - {lista[count].nome}')
    print()
    return True

  
# Print formatado do objeto Projeto
def mostrarItem(obj): 
  nome = obj.nome
  if obj.tarefas == []:
    tarefas = 'Vazio'
  else:
    for count in range(0, len(obj.tarefas)):
      tarefas += obj.tarefas[count]

      if count+1 == len(obj.tarefas):
        tarefas += '.'
      else:
        tarefas += ', '
  
  status = obj.status
  criacao = obj.criacao

  print(f'Descrição: {nome} \nTarefas: {tarefas} \nStatus: {status} \nCriação: {criacao}\033[m')

#Apaga objeto Projeto de dentro da lista principal utilizando a função del de list()
def apagar(lista): 
  mostrarProjetos(lista, 'Apagar Projeto')
  opcao = validacao.leiaInt('Qual Projeto: ')
   

  print('\n\033[31mPROJETO APAGADO')
  mostrarItem(lista[opcao-1]) 
  del lista[opcao-1]
  
  return lista
