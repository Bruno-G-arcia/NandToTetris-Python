from Cl_comp2 import Comp2

class Ram():
  nR = 4
  nB = 16
  rL = []
  #NR = qtde de registros
  #nB = qtde de bits dos registros

  def __init__(self, nR,nB):
    self.nR = nR
    self.nB = nB
    for i in range(nR):
      self.rL[i] = Comp2()

  def binaToInteger(self, binary):
    number = 0
    for b in binary:
      number = (2 * number) + b
    return number

  def Run(self,i,add,load):
    DAdd = self.binaToInteger(add)
    reg = self.rL[DAdd]
    return reg.Register(i,load)
