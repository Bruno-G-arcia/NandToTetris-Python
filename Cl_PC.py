from Cl_Comp1 import Component1

class Pc():
  nB = 16
  regBit1 = [0] * 16

  def __init__(self, nB):
    self.nB = nB

  def Run(self,i,load,inc,reset):
    vAux = self.regBit1
    leI = len(i)
    one = [0] * leI
    one[leI - 1] = 1
    if(reset == 1):
      self.regBit1 = [0] * self.nB
    elif(load == 1):
      self.regBit1 = i
    elif(inc == 1):
      comp1 = Component1()
      self.regBit1 = comp1.NBitAdder(self.regBit1, one)
    
    return vAux  
