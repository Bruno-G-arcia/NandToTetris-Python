from Cl_Ram import Ram

class TestsRam():
  def Test4x16Ram(self):
    ram = Ram(4,16)
    #vamos escrever no primeiro registro
    i   = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    ept = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    add = [0]
    r = ram.Run(i,add,1)
    r = ram.Run(ept,add,0)
    print(f'R0-1:{r == i}')
    i = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]
    r = ram.Run(i,add,1)
    r = ram.Run(ept,add,0)
    print(f'R0-2:{r == i}')
    i   = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    add = [0,1]
    r = ram.Run(i,add,1)
    r = ram.Run(ept,add,0)
    print(f'R1-1:{r == i}')
    i   = [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0]
    add = [1,0]
    r = ram.Run(i,add,1)
    r = ram.Run(ept,add,0)
    print(f'R2-1:{r == i}')
    i   = [0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0]
    add = [1,1]
    r = ram.Run(i,add,1)
    r = ram.Run(ept,add,0)
    print(f'R3-1:{r == i}')
    i = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]
    add = [0]
    r = ram.Run(ept,add,0)
    print(f'R0-3:{r == i}')
