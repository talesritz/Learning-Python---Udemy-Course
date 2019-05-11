from utils import Veiculos, formatacao

formatacao.cabecalho('Udemy - Desafio Carros POO')


if __name__ == '__main__':
  c1 = Veiculos.Carro(180)
  

  for _ in range(25):
    print(c1.acelerar(8))
     

  print()


  for _ in range(10):
    print(c1.frear(20))
    