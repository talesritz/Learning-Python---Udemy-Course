class Carro: 
  
  #Inicia apenas com a velocidade Máxima  
  def __init__ (self, velmax, velatual = 0, velmin = 0):
    self.velmax = velmax
    self.velatual = velatual
    self.velmin = velmin


  def __str__(self):
    return f'''Velocidade Máxima: {self.velmax} \nDelta Aceleração: 5\nDelta Frenagem: 5    
    '''


  def acelerar(self, delta = 5):
    
    if self.velmax - self.velatual < delta:
      self.velatual = self.velmax
    else:
      self.velatual += delta
      
    return f'Velocidade: {self.velatual} Km/h'  



  def frear(self, delta=5):
 
   if self.velatual - self.velmin < delta:
     self.velatual = self.velmin
   else:
     self.velatual -= delta
    
   return f'Velocidade: {self.velatual} Km/h'  
