from Cl_comp2 import Comp2

class Comp2Tests():

  def TestFlipFlop(self):
    comp2 = Comp2()
    vl    = [1,1,1,0,1,1,0,1,1,1]
    r     = [0,0,0,0,0,0,0,0,0,0]
    comp  = [0,1,1,1,0,1,1,0,1,1]

    for i in range(len(vl)):
      r[i] = comp2.FlipFlop(vl[i])

    print(r == comp)
    print("--")
  
  def TestRegister(self):
    comp2 = Comp2()
    vl    = [1,0,0,0,0]
    load  = [1,0,0,1,0]
    r     = [0,0,0,0,0]
    comp  = [0,1,1,1,0]

    for i in range(len(vl)):
      r[i] = comp2.Register(vl[i],load[i])

    print(r == comp)
    print("--")