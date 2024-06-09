class Comp2:
  ffBit     = 0
  regBit1   = 0
  regBit2   = 0
  def FlipFlop(self, a):
    vAux = self.ffBit
    self.ffBit = a
    return vAux

  def Register(self,i,load):
    vAux = self.regBit1
    self.regBit2 = i
    if(load == 1):
      self.regBit1 = self.regBit2
    return vAux
  