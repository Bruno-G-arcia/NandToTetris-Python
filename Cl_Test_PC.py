from Cl_PC import Pc

class TestsPc():
  def TestPc(self):
    pc   = Pc(16)
    i    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    ept  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    comp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    r = pc.Run(i,1,0,0)
    r = pc.Run(ept,0,1,0)
    print(f'load : {r == i}')
    r = pc.Run(ept,0,0,1)
    print(f'inc  : {r == comp}')
    r = pc.Run(ept,0,0,0)
    print(f'reset: {r == ept}')