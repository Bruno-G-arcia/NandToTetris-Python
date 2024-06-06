from Cl_Comp1 import Component1 
from Cl_Gate  import Gate

class ALU():
  
  # The ALU (Arithmetic Logic Unit).
  # Computes one of the following functions:
  # x+y, x-y, y-x, 0, 1, -1, x, y, -x, -y, !x, !y,
  # x+1, y+1, x-1, y-1, x&y, x|y on two 16-bit inputs,
  # according to 6 input bits denoted zx,nx,zy,ny,f,no.
  # In addition, the ALU computes two 1-bit outputs:
  # if the ALU output == 0, zr is set to 1; otherwise zr is set to 0;
  # if the ALU output < 0, ng is set to 1; otherwise ng is set to 0.

  # Implementation: the ALU logic manipulates the x and y inputs
  # and operates on the resulting values, as follows:
  # if (zx == 1) set x = 0        // 16-bit constant
  # if (nx == 1) set x = !x       // bitwise not
  # if (zy == 1) set y = 0        // 16-bit constant
  # if (ny == 1) set y = !y       // bitwise not
  # if (f == 1)  set out = x + y  // integer 2's complement addition
  # if (f == 0)  set out = x & y  // bitwise and
  # if (no == 1) set out = !out   // bitwise not
  # if (out == 0) set zr = 1
  # if (out < 0) set ng = 1

  # Mux16(a=x, b=false, sel=zx, out=t1);
  # Mux16(a=y, b=false, sel=zy, out=t2);
  # Not16(in=t1, out=notT1);
  # Not16(in=t2, out=notT2);
  # Mux16(a=t1, b=notT1, sel=nx, out=t3);
  # Mux16(a=t2, b=notT2, sel=ny, out=t4);
  # Add16(a=t3, b=t4, out=sumT3T4);
  # And16(a=t3, b=t4, out=andT3T4);
  # Mux16(a=andT3T4, b=sumT3T4, sel=f, out=t5);
  # Not16(in=t5, out=notT5);
  # Mux16(a=t5, b=notT5, sel=no, out=out, out[15]=msbOut, out[0..7]=rightOut, out[8..15]=leftOut);
  # And(a=msbOut, b=true, out=ng);
  # Or8Way(in=leftOut, out=orWayLeftOut);
  # Or8Way(in=rightOut, out=orWayRightOut);
  # Or(a=orWayLeftOut, b=orWayRightOut, out=orWayOut);
  # Not(in=orWayOut, out=zr);

  def Run(self,x,y,zx,nx,zy,ny,f,no):
    gate = Gate()
    comp = Component1()
    fl = [0] * 16
    t1 = gate.Mux16(x,fl,zx)
    t2 = gate.Mux16(y,fl,zy)
    notT1 = gate.NotBus(t1)
    notT2 = gate.NotBus(t2)
    t3 = gate.Mux16(t1,notT1,nx)
    t4 = gate.Mux16(t2,notT2,ny)
    sumT3T4 = comp.NBitAdder(t3,t4)
    andT3T4 = gate.AndBus(t3,t4)
    t5 = gate.Mux16(andT3T4,sumT3T4, f)
    notT5 = gate.NotBus(t5)
    out = gate.Mux16(t5,notT5,no)
    ng = out[0]
    rightOut = [out[15],out[14], out[13],out[12], out[11], out[10], out[9], out[8]]
    leftOut  = [out[7],out[6],out[5],out[4],out[3],out[2],out[1],out[0]]
    orWayLeftOut = gate.OrWay(leftOut)
    orWayRightOut = gate.OrWay(rightOut)
    orWayOut = gate.Or(orWayLeftOut, orWayRightOut)
    zr = gate.Not(orWayOut)
    return [out, zr, ng]
