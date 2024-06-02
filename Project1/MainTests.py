
from Gate import Gate
from GateTests import Test

gate = Gate()
test = Test()

print("Nand")
test.TestNand()

print("Not")
test.Test1(gate.Not, [1,0])

print("And")
test.Test2(gate.And,[0,0,0,1])

print("Or")
test.Test2(gate.Or,[0,1,1,1])

print("Xor")
test.Test2(gate.Xor,[0,1,1,0])

print("Mux")
test.TestMux()

print("Dmux")
test.Test2(gate.Dmux, ([0,0],[1,0],[0,0],[0,1]))

print("Not16")
test.TestNot16()

print("And16")
test.TestAnd16()

print("Or16")
test.TestOr16()

print("Mux16")
test.TestMux16()

print("Or8way")
test.TestOr8Way()

print("Mux4Way16")
test.TestMux4Way16()

print("Mux8Way16")
test.TestMux8Way16()

print("DMux4Way")
test.TestDMux4Way()

print("DMux8Way")
test.TestDMux4Way()