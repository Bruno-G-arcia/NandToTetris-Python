

from Gate import Gate

class Test:

  def Test2(self, func, exp):
    print(0, 0,func(0,0), func(0,0) == exp[0])
    print(0, 1,func(0,1), func(1,0) == exp[1])
    print(1, 0,func(1,0), func(0,1) == exp[2])
    print(1, 1,func(1,1), func(1,1) == exp[3])
    print("--")

  def Test1(self, func, exp):
    print(0, func(0), func(0) == exp[0])
    print(1, func(1), func(1) == exp[1])
    print("--")

  def TestNand(self):
    gate = Gate()
    print(0, 0, gate.Nand(0,0), gate.Nand(0,0) == 1)
    print(0, 1, gate.Nand(0,1), gate.Nand(0,1) == 1)
    print(1, 0, gate.Nand(1,0), gate.Nand(1,0) == 1)
    print(1, 1, gate.Nand(1,1), gate.Nand(1,1) == 0)
    print("--")

  def TestMux(self):
    gate = Gate()
    print(0,0,0, gate.Mux(0,0,0), gate.Mux(0,0,0) == 0)
    print(0,1,0, gate.Mux(0,1,0), gate.Mux(0,1,0) == 0)
    print(1,0,0, gate.Mux(1,0,0), gate.Mux(1,0,0) == 1)
    print(1,1,0, gate.Mux(1,1,0), gate.Mux(1,1,0) == 1)
    print(0,0,1, gate.Mux(0,0,1), gate.Mux(0,0,1) == 0)
    print(0,1,1, gate.Mux(0,1,1), gate.Mux(0,1,1) == 1)
    print(1,0,1, gate.Mux(1,0,1), gate.Mux(1,0,1) == 0)
    print(1,1,1, gate.Mux(1,1,1), gate.Mux(1,1,1) == 1)
    print("--")

  def TestAnd16(self):
    gate = Gate()
    print(
      gate.AndBus([1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0], 
                  [0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0]) ==
                  [0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0]
    )
    print("--")
    
  def TestNot16(self):
    gate = Gate()
    print(gate.NotBus([1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]) ==
                      [0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0])
    print("--") 

  def TestMux4Way16(self):
    gate = Gate()
    a   = [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]
    b   = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    c   = [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
    d   = [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]

    v = []
    v.append(a)
    v.append(b)
    v.append(c)
    v.append(d)

    print(gate.MuxBus(v, ([0,0])) == a)
    print(gate.MuxBus(v, ([0,1])) == b)
    print(gate.MuxBus(v, ([1,0])) == c)
    print(gate.MuxBus(v, ([1,1])) == d)
    print("--")
  
  def TestOr16(self):
    gate = Gate()
    a   = [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
    b   = [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
    res = [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1]

    print(gate.OrBus(a,b) == res)
    print("--") 
    
  def TestMux16(self):
    gate = Gate()
    a   = [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
    b   = [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

    print(gate.Mux(a,b,0) == a)
    print(gate.Mux(a,b,1) == b)

    print("--")

  def TestOr8Way(self):
    gate = Gate()
    a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    print(gate.OrWay(a) == 1)
    print(gate.OrWay(b) == 0)
    print("--")
  
  def TestMux8Way16(self):
    gate = Gate()
    a   = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    b   = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c   = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    d   = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    e   = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    f   = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    g   = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    h   = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

    v = []
    v.append(a)
    v.append(b)
    v.append(c)
    v.append(d)
    v.append(e)
    v.append(f)
    v.append(g)
    v.append(h)

    print(gate.MuxBus(v, ([0,0,0])) == a)
    print(gate.MuxBus(v, ([0,0,1])) == b)
    print(gate.MuxBus(v, ([0,1,0])) == c)
    print(gate.MuxBus(v, ([0,1,1])) == d)
    print(gate.MuxBus(v, ([1,0,0])) == e)
    print(gate.MuxBus(v, ([1,0,1])) == f)
    print(gate.MuxBus(v, ([1,1,0])) == g)
    print(gate.MuxBus(v, ([1,1,1])) == h)
    print("--")

  def TestDMux4Way(self):
    gate = Gate()
    print(gate.DmuxNWay(1,([1,1]),4) == [0,0,0,1])
    print("--")

  def TestDMux8Way(self):
    gate = Gate()
    print(gate.DmuxNWay(1,([1,1,1]),8) == [0,0,0,0,0,0,0,1])
    print("--")