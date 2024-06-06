from Cl_ALU   import ALU
from Cl_Gate  import Gate
from Cl_Comp1 import Component1

class TestAlu():
  def Test1(self):
    gate = Gate()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 0
    zy = 1
    ny = 0
    f  = 1
    no = 0 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    out_comp  = [0] * 16
    zr        = res[1]
    zr_comp   = 0
    ng        = res[2]
    ng_comp   = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp == 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")
  
  def Test2(self):
    gate = Gate()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 1
    ny = 1
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    out_comp  = [0] * 16
    out_comp[15] = 1
    zr        = res[1]
    zr_comp   = 0
    ng        = res[2]
    ng_comp   = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp == 1
    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")
  
  def Test3(self):
    gate = Gate()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 1
    ny = 0
    f  = 1
    no = 0 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = [1] * 16    
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test4(self):
    gate = Gate()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 0
    zy = 1
    ny = 1
    f  = 0
    no = 0 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = x   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test5(self):
    gate = Gate()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 0
    ny = 0
    f  = 0
    no = 0 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = y   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test6(self):
    gate = Gate()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 0
    zy = 1
    ny = 1
    f  = 0
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = gate.NotBus(x)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test7(self):
    gate = Gate()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 0
    ny = 0
    f  = 0
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = gate.NotBus(y)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test8(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 0
    zy = 1
    ny = 1
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    =  comp.Negative(x)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")
  
  def Test9(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 0
    ny = 0
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    =  comp.Negative(y)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test10(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 1
    zy = 1
    ny = 1
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    add1        = [0] * 16
    add1[15]    = 1
    out_comp    = comp.NBitAdder(x,add1)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test11(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 0
    ny = 1
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    add1        = [0] * 16
    add1[15]    = 1
    out_comp    = comp.NBitAdder(y,add1)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test12(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 0
    ny = 1
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    add1        = [1] * 16
    out_comp    = comp.NBitAdder(x,add1)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")
  
  def Test13(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 1
    nx = 1
    zy = 0
    ny = 0
    f  = 1
    no = 0 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    add1        = [1] * 16
    out_comp    = comp.NBitAdder(y,add1)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test14(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 0
    zy = 0
    ny = 0
    f  = 1
    no = 0 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = comp.NBitAdder(x,y)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test15(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 1
    zy = 0
    ny = 0
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = comp.NBitAdder(x,comp.Negative(y))   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")
  
  def Test16(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 0
    zy = 0
    ny = 1
    f  = 1
    no = 1 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = comp.NBitAdder(y,comp.Negative(x))   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test17(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 0
    zy = 0
    ny = 0
    f  = 0
    no = 0 
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = gate.AndBus(x,y)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")

  def Test18(self):
    gate = Gate()
    comp = Component1()
    alu = ALU()
    x = [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
    y = [0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0]
    zx = 0
    nx = 1
    zy = 0
    ny = 1
    f  = 0
    no = 1
    res = alu.Run(x,y,zx,nx,zy,ny,f,no)
    out       = res[0]
    zr        = res[1]
    ng        = res[2]

    out_comp    = gate.OrBus(x,y)   
    zr_comp     = 0
    ng_comp     = 0

    if (gate.OrWay(out) == 0):
      zr_comp = 1
    
    if(out[0] == 1):
      ng_comp = 1

    print(out == out_comp, zr == zr_comp, ng == ng_comp)
    print("--")