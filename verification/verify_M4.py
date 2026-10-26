import sys
sys.path.append('/app/conversations/6a9457922be742711f13922b/maths-work')
import sympy as sp
from fractions import Fraction as F
import numpy as np
from mathlib import *

print("Running verify_M4.py assertions...")

# M4-P1-3a
r1 = joint_table([1, 2], [-2, -1, 4, 5], [
    [F(1,10), F(2,10), 0, F(3,10)],
    [F(2,10), F(1,10), F(1,10), 0]
])
assert r1['px'] == [F(3,5), F(2,5)]
assert r1['py'] == [F(3,10), F(3,10), F(1,10), F(3,10)]
assert r1['EX'] == F(7,5)
assert r1['EY'] == F(1,1)
assert r1['EXY'] == F(9,10)
assert r1['cov'] == F(-1,2)
assert round(r1['rho'], 4) == -0.3294

# M4-P1-3b
sol_p1_3b = fixed_vector([
    [F(0), F(1), F(0)],
    [F(1,6), F(1,2), F(1,3)],
    [F(0), F(2,3), F(1,3)]
])
x0, x1, x2 = sp.symbols('x0 x1 x2')
assert sol_p1_3b[x0] == F(1,10)
assert sol_p1_3b[x1] == F(3,5)
assert sol_p1_3b[x2] == F(3,10)

# M4-P1-3c
P_boys = sp.Matrix([[0, 1, 0], [0, 0, 1], [F(1,2), F(1,2), 0]])
p0 = sp.Matrix([[0, 0, 1]])
p3 = p0 * (P_boys**3)
assert p3 == sp.Matrix([[F(1,4), F(1,4), F(1,2)]])

# M4-P1-4a
k_4a = F(1,42)
tab_4a = [[k_4a*(2*x + y) for y in range(4)] for x in range(3)]
px_4a = [sum(r) for r in tab_4a]
py_4a = [sum(tab_4a[i][j] for i in range(3)) for j in range(4)]
assert px_4a == [F(1,7), F(1,3), F(11,21)]
assert py_4a == [F(1,7), F(3,14), F(2,7), F(5,14)]

# M4-P1-4b
sol_p1_4b = fixed_vector([
    [F(0), F(1), F(0)],
    [F(0), F(0), F(1)],
    [F(1,2), F(1,2), F(0)]
])
assert sol_p1_4b[x0] == F(1,5)
assert sol_p1_4b[x1] == F(2,5)
assert sol_p1_4b[x2] == F(2,5)

# M4-P1-4c
P_car = sp.Matrix([[0, 1, 0], [0, 0, 1], [F(1,3), F(1,3), F(1,3)]])
p0_car = sp.Matrix([[0, 0, 1]])
p2_car = p0_car * (P_car**2)
p3_car = p0_car * (P_car**3)
assert p2_car == sp.Matrix([[F(1,9), F(4,9), F(4,9)]])
assert p3_car == sp.Matrix([[F(4,27), F(7,27), F(16,27)]])

# M4-P2-3a
r2_3a = joint_table([2, 4, 6], [1, 3, 9], [
    [F(1,8), F(1,24), F(1,12)],
    [F(1,4), F(1,4), 0],
    [F(1,8), F(1,24), F(1,12)]
])
assert r2_3a['px'] == [F(1,4), F(1,2), F(1,4)]
assert r2_3a['py'] == [F(1,2), F(1,3), F(1,6)]
assert r2_3a['cov'] == 0

# M4-P2-3b
sol_sales = fixed_vector([
    [F(0), F(1), F(0)],
    [F(2,3), F(0), F(1,3)],
    [F(2,3), F(1,3), F(0)]
])
assert sol_sales[x0] == F(2,5)
assert sol_sales[x1] == F(9,20)
assert sol_sales[x2] == F(3,20)

# M4-P2-4c
r2_4c = joint_table([0, 1], [0, 1, 2, 3], [
    [0, F(1,8), F(2,8), F(1,8)],
    [F(1,8), F(2,8), F(1,8), 0]
])
assert r2_4c['EXY'] == F(1,2)
assert r2_4c['cov'] == F(-1,4)

# M4-P3-3a
tab_3a = [[F(x+y, 30) for y in range(3)] for x in range(4)]
p_3a_i = sum(tab_3a[x][1] for x in range(3))
p_3a_ii = sum(tab_3a[x][y] for x in range(4) for y in range(3) if x > y)
assert p_3a_i == F(1,5)
assert p_3a_ii == F(3,5)

# M4-P3-3c
P_boys_v2 = sp.Matrix([[0, 1, 0], [1, 0, 0], [F(1,2), F(1,2), 0]])
p3_b = sp.Matrix([[0, 0, 1]]) * (P_boys_v2**3)
assert p3_b == sp.Matrix([[F(1,2), F(1,2), 0]])

# M4-P3-4b
P_p3_4b = sp.Matrix([[0, 0, 1], [F(1,2), 0, F(1,2)], [0, 1, 0]])
assert all(entry > 0 for entry in (P_p3_4b**5))

# M4-P3-4c
P_gambler = sp.Matrix([[F(6,10), F(4,10)], [F(3,10), F(7,10)]])
p1_g = sp.Matrix([[F(1,2), F(1,2)]]) * P_gambler
assert p1_g[0] == F(9,20)

# M4-P4-3b
sol_study = fixed_vector([[F(3,10), F(7,10)], [F(4,10), F(6,10)]])
assert sol_study[x0] == F(4,11)

# M4-P4-4b
P_club = sp.Matrix([[0, 1], [F(1,2), F(1,2)]])
p3_c = sp.Matrix([[0, 1]]) * (P_club**3)
assert p3_c == sp.Matrix([[F(3,8), F(5,8)]])

# M4-P4-4c
k_p4 = F(1,27)
tab_p4 = [[k_p4*(2*x + y) for y in range(3)] for x in range(3)]
assert sum(sum(r) for r in tab_p4) == 1

# M4-P5-3a
r5_3a = joint_table([1, 5], [-4, 2, 7], [
    [F(1,8), F(1,4), F(1,8)],
    [F(1,4), F(1,8), F(1,8)]
])
assert r5_3a['EX'] == 3
assert r5_3a['EY'] == 1
assert r5_3a['EXY'] == F(3,2)
assert r5_3a['cov'] == F(-3,2)
assert round(r5_3a['rho'], 4) == -0.1732

# M4-P5-3b
P_p5_3b = [[F(0), F(2,3), F(1,3)], [F(1,2), F(0), F(1,2)], [F(1,2), F(1,2), F(0)]]
sol_p5_3b = fixed_vector(P_p5_3b)
assert sol_p5_3b[x0] == F(1,3)
assert sol_p5_3b[x1] == F(10,27)
assert sol_p5_3b[x2] == F(8,27)

# M4-P5-4c
P_p5_4c = sp.Matrix([[F(1,2), 0, F(1,2)], [1, 0, 0], [F(1,4), F(1,2), F(1,4)]])
p2_p5_4c = sp.Matrix([[F(1,2), F(1,2), 0]]) * (P_p5_4c**2)
assert p2_p5_4c[0] == F(7,16)

# M4-P6-4b
r6_4b = joint_table([1, 2], [-2, 5, 3], [
    [F(21,100), F(35,100), F(14,100)],
    [F(9,100), F(15,100), F(6,100)]
])
assert r6_4b['cov'] == 0

# M4-P7-3a
r7_3a = joint_table([1, 2], [-3, 2, 4], [
    [F(1,10), F(2,10), F(2,10)],
    [F(3,10), F(1,10), F(1,10)]
])
assert r7_3a['px'][0]*r7_3a['py'][0] != F(1,10)

# M4-P7-3b
r7_3b = joint_table([-2, 0, 2], [-2, 3], [
    [0, F(5,15)],
    [F(2,15), F(3,15)],
    [F(4,15), F(1,15)]
])
assert r7_3b['cov'] == F(-8,3)

# M4-P7-3c
P_xyz = sp.Matrix([[0, 1, 0], [0, 0, 1], [F(1,2), F(1,2), 0]])
p4_xyz = sp.Matrix([[0, 0, 1]]) * (P_xyz**4)
assert p4_xyz[0] == F(1,4)

# M4-P7-4c
P_study2 = [[F(4,10), F(6,10)], [F(8,10), F(2,10)]]
sol_study2 = fixed_vector(P_study2)
assert sol_study2[x0] == F(4,7)
p4_s2 = sp.Matrix([[1, 0]]) * (sp.Matrix(P_study2)**4)
assert p4_s2[1] == F(261,625)

print("ALL VERIFICATION ASSERTIONS PASSED SUCCESSFULLY!")
