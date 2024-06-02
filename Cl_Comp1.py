from Cl_Gate import Gate

class Component1():
  def HalfAdder(self, a, b):
    gate = Gate()
    return[gate.Xor(a,b), gate.And(a,b)]
  
  def FullAdder(self, a, b, c):
    gate = Gate()
    x1 = gate.Xor(a,b)
    a1 = gate.And(a,b)
    x2 = gate.Xor(x1,c)
    a2 = gate.And(x1, c)
    o1 = gate.Or(a1, a2)
    return([x2,o1])
  
  def NBitAdder(self, al, bl):
    result = [0] * len(al)
    c = 0
    for i in range(len(al) - 1, -1, -1):
      sum = self.FullAdder(al[i],bl[i],c)
      result[i] = sum[0]
      c = sum[1]
    return result
  
  def Negative(self, al):
    gate = Gate()
    leAl = len(al)
    add  = [0] * leAl
    add[leAl - 1] = 1 
    al = gate.NotBus(al)
    al = self.NBitAdder(al,add)
    return al
      