## @file test_driver.py
#  @author Rithvik Bhogadi
#  @brief Tests for complex_adt.py and triangle_adt.py
#  @date 01/21/2021

from complex_adt import ComplexT
from triangle_adt import TriangleT, TriType

## ComplexT
# Test of add method
a = ComplexT(1.0, 2.0)
b = ComplexT(0.5, -0.5)
c = a.add(b)
if(c.x == 1.5 and c.y == 1.5):
   print("add test passes")
else:
   print("add test FAILS")

a = ComplexT(1.0, 2.0)
if(a.x == 1.0):
   print("real test passes")
else:
   print("real test FAILS")

a = ComplexT(3.0, 4.0)
if(a.y == 4.0):
   print("imag test passes")
else:
   print("imag test FAILS")

a = ComplexT(-2.0, 3.0)
getso = round(a.get_r(), 2)
if(getso == 3.61):
   print("get_r test passes")
else:
   print("get_r test FAILS")

a = ComplexT(1.0, 2.0)
phiso = round(a.get_phi(), 2)
if(phiso == 0.46):
   print("get_phi test passes")
else:
   print("get_phi test FAILS")

a = ComplexT(1.5, 1.5)
b = ComplexT(1.5, 1.4)
c = a.equal(b)
if(c == True):
   print("equal test passes")
else:
   print("equal test FAILS")

a = ComplexT(1.0, -2.0)
b = ComplexT(1.0, -2.0)
c = a.conj()
if(c.x == 1.0 and c.y == -2.0):
   print("conj test passes")
else:
   print("conj test FAILS")

a = ComplexT(1.0, 2.0)
b = ComplexT(0.5, 0.5)
c = a.sub(b)
if(c.x == 0.5 and c.y == 1.5):
   print("sub test passes")
else:
   print("sub test FAILS")

a = ComplexT(3.0, -4.0)
b = ComplexT(4.0, 5.0)
c = a.mult(b)
if(c.x == 32.0 and c.y == -1.0):
   print("mult test passes")
else:
   print("mult test FAILS")

# @details Assuming that non-zero value will be used for input
a = ComplexT(3.0, 4.0)
c = a.sqrt()
if(c.x == 2.0 and c.y == 1.0):
   print("sqrt test passes")
else:
   print("sqrt test fails")

a = ComplexT(2.0, 4.0)
c = a.recip()
if(c.x == 1/10 and c.y == -1/5):
   print("recip test passes")
else:
   print("recip test FAILS")

a = ComplexT(3.0, -1.0)
b = ComplexT(2.0, -2.0)
c = a.div(b)
if(c.equal(ComplexT(1.0, 0.5))):
   print("div test passes")
else:
   print("div test FAILS")


# TriangleT
t1 = TriangleT(3, 4, 5)
t1.get_sides()
if(t1.l1 < 0 and t1.l2 < 0 and t1.l3 < 0):
   print("get_sides test FAILS")
if(t1.l1 == 3 and t1.l2 == 4 and t1.l3 == 5):
   print("get_sides test passes")
else:
   print("get_sides test FAILS")

# Test of equal method
t1 = TriangleT(4, 5, 6)
t2 = TriangleT(4, 5, 7)
if (t1.equal(t2)):
   print("triangle equal test passes")
else:
   print("triangle equal test FAILS")

t1 = TriangleT(4, 6, 2)
if(t1.perim() < 0):
   print("perim test FAILS")
if (t1.perim() == 12):
   print("perim test passes")
else:
   print("perim test FAILS")

t1 = TriangleT(5.0, 7.0, 8.0)
aresa = round(t1.area(), 2)
if(aresa == 17.32):
   print("area test passes")
else:
   print("area test FAILS")

t1 = TriangleT(0, 23, 11)
if(t1.is_valid == True):
   print("is_valid test passes")
else:
   print("is_valid test FAILS")

# Test triangle type
t1 = TriangleT(3, 4, 5)
if (t1.tri_type() == TriType.equilat):
   print("tri_type test passes")
else:
   print("tri_type test FAILS")

if (t1.tri_type() == TriType.isosceles):
   print("tri_type test passes")
else:
   print("tri_type test FAILS")

if (t1.tri_type() == TriType.scalene):
   print("tri_type test passes")
else:
   print("tri_type test FAILS")

if (t1.tri_type() == TriType.right):
   print("tri_type test passes")
else:
   print("tri_type test FAILS")



