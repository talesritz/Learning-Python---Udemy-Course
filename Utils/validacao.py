#validador INT
def leiaInt(msg):

  tmp = str(input(msg))
  while tmp.isnumeric() == False:
    print('\033[31mOpção Inválida\033[m')
    tmp = str(input(msg))
  
  return int(tmp)


#Validador STR
def leiaStr(msg):

  tmp = str(input(msg))
  while ''.join(tmp.split()).isalpha() == False:
    print('\033[31mOpção Inválida\033[m')
    tmp = str(input(msg))

  return tmp


def sair(msg):
  print(f'\n\033[1mSaindo de {msg}...\033[m')