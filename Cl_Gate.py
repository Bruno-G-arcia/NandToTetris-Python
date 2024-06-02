class Gate():

  def binaToInteger(self, binary):
    number = 0
    for b in binary:
      number = (2 * number) + b
    return number

  def And(self, a, b):
    return a & b
  
  def AndBus(sef, al:list, bl:list):
    result = []
    if(len(al) == len(bl)):
      for i in range(len(al)):
        result.append(al[i] & bl[i])
    return result

  def Or(self, a, b):
    return a | b
  
  def OrBus(self, al:list, bl:list):
    result = []
    if(len(al) == len(bl)):
      for i in range(len(al)):
        result.append(al[i] | bl[i])
    return result

  def OrWay(self, al:list):
    for a in al:
      if (a == 1):
        return 1
    return 0

  def Not(self, a):
    return int(not a)
  
  def NotBus(self, al:list):
    result = []
    for a in al:
      result.append(int(not a))
    return result
  
  def Nand(self, a,b):
    return int(not(a & b))
  
  def Xor(self, a, b):
    return int(a != b);

  def Mux(self, a, b, sel):
    if (sel ==0):
      return a
    else:
      return b
    
  def Dmux(self, i, sel):
    if(sel == 0):
      return [i,0]
    else:
      return [0,i]
    
  def DmuxNWay(self,  i, sel,n):
    result = [0] * n   
    result[self.binaToInteger(sel)] = i
    return result

  def MuxBus(self, i, sel):
    return i[self.binaToInteger(sel)]
