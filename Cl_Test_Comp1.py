from Cl_Comp1 import Component1

class Comp1Tests():
  
  def TestHalfAdder(self):
    comp = Component1()
    print(0,0,0,0, comp.HalfAdder(0,0) == [0,0] )
    print(0,1,1,0, comp.HalfAdder(0,1) == [1,0] )
    print(1,0,1,0, comp.HalfAdder(1,0) == [1,0] )
    print(1,1,0,1, comp.HalfAdder(1,1) == [0,1] )
    print("--")

  def TestFullAdder(self):
    comp = Component1()
    print(0,0,0,0,0, comp.FullAdder(0,0,0) == [0,0] )
    print(0,0,1,1,0, comp.FullAdder(0,0,1) == [1,0] )
    print(0,1,0,1,0, comp.FullAdder(0,1,0) == [1,0] )
    print(0,1,1,0,1, comp.FullAdder(0,1,1) == [0,1] )
    print(1,0,0,1,0, comp.FullAdder(1,0,0) == [1,0] )
    print(1,0,1,0,1, comp.FullAdder(1,0,1) == [0,1] )
    print(1,1,0,0,1, comp.FullAdder(1,1,0) == [0,1] )
    print(1,1,1,1,1, comp.FullAdder(1,1,1) == [1,1] )
    print("--")


  def Test4BitAdder(self):
    comp = Component1()
    a = [1,0,0,1]
    b = [0,1,0,1]
    r = [1,1,1,0]
    print(comp.NBitAdder(a,b) == r)
    print("--")

  def Test16BitAdder(self):
    comp = Component1()
    a = [1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1]
    b = [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1]
    r = [1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0]
    print(comp.NBitAdder(a,b) == r)
    print("--")

  def TestNegative(self):
    comp = Component1()
    print(comp.Negative([0,1,0,0]) == [1,1,0,0])
    print("--")

  def TestInc16(self):
    comp = Component1()
    a = [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1]
    r = [0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0]
    print(comp.Inc(a) == r)
    print("--")