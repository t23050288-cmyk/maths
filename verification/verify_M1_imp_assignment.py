"""Verification for Module 1 (modular arithmetic): every PYQ answer, every
Important Question answer, and every Assignment 1 answer.
Run:  python3 verify_M1.py
"""
from math import gcd, factorial

fails = []

def ok(a, b, msg):
    if a != b:
        fails.append(f"{msg}: expected {b}, got {a}")
    else:
        print(f"OK   {msg}")

# --- last digits ---
ok(pow(7, 2013, 10), 7, "last digit 7^2013")
ok(pow(13, 37, 10), 3, "last digit 13^37")
ok(pow(7, 289, 10), 7, "last digit 7^289")
ok(pow(7, 126, 10), 9, "last digit 7^126")
ok(pow(7, 118, 10), 9, "last digit 7^118")
# --- remainders ---
ok(pow(41, 75, 3), 2, "41^75 mod 3")
ok(pow(2, 23, 47), 1, "2^23 mod 47")
ok(pow(4, 8, 23), 9, "4^8 mod 23 (imp Q2)")
ok(pow(2, 340, 31), 1, "2^340 mod 31")
ok(pow(8, 30, 31), 1, "8^30 mod 31")
ok(factorial(14) % 17, 8, "14! mod 17")
ok(factorial(29) % 31, 1, "29! mod 31 (Wilson step)")
ok((4 * (factorial(29) % 31) + 120) % 31, 0, "4(29)!+5! mod 31")
ok(pow(7, 121, 13), 7, "7^121 mod 13")
ok((64 * 65 * 66) % 67, 61, "64*65*66 mod 67 (assignment Q3)")
ok((135 * 74 * 48) % 7, 6, "135*74*48 mod 7")
ok((175 * 113 * 53) % 11, 6, "175*113*53 mod 11")
ok((135 * 146 * 73) % 7, 1, "135*146*73 mod 7")
ok((349 * 74 * 36) % 3, 0, "349*74*36 mod 3")
# --- linear congruences ---
ok(sorted(x for x in range(21) if (12 * x) % 21 == 6), [4, 11, 18], "12x=6 mod21")
ok(sorted(x for x in range(18) if (14 * x) % 18 == 12), [6, 15], "14x=12 mod18")
ok(sorted(x for x in range(21) if (6 * x) % 21 == 15), [6, 13, 20], "6x=15 mod21")
ok(sorted(x for x in range(42) if (18 * x) % 42 == 30), [4, 11, 18, 25, 32, 39], "18x=30 mod42")
ok(sorted(x for x in range(35) if (10 * x) % 35 == 15), [5, 12, 19, 26, 33], "10x=15 mod35 (imp Q6)")
# --- systems ---
ok(((7 * 3 + 3 * 7) % 16, (2 * 3 + 5 * 7) % 16), (10, 9), "system mod 16 -> (3,7)")
ok(((2 * 4 + 6 * 0) % 7, (4 * 4 + 3 * 0) % 7), (1, 2), "system mod 7 -> (4,0)")
ok(((3 * 7 + 4 * 9) % 13, (2 * 7 + 5 * 9) % 13), (5, 7), "system mod 13 -> (7,9)")
# --- Diophantine ---
ok(70 * 4 + 112 * (-1), 168, "70x+112y particular (4,-1)")
ok(13 * 3 + 17 * (-2), 5, "13x+17y particular (3,-2)")
# --- CRT ---
def crt(rs):
    N = 1
    for r, m in rs:
        N *= m
    return sum(r * (N // m) * pow(N // m, -1, m) for r, m in rs) % N
ok(crt([(2, 3), (3, 5), (2, 7)]), 23, "CRT 2,3,2 (mod 3,5,7)")
ok(crt([(1, 4), (3, 5), (2, 7)]), 93, "CRT 1,3,2 (mod 4,5,7) (imp Q5)")
ok(crt([(3, 5), (2, 6), (4, 7)]), 158, "CRT 3,2,4 (mod 5,6,7)")
ok(crt([(5, 3), (2, 5), (1, 11)]), 122, "CRT 5,2,1 (mod 3,5,11)")
# --- RSA ---
ok(pow(13, -1, 2436), 937, "RSA STOP private key d")
for ch, m, c in [("S", 18, 2222), ("T", 19, 2299), ("O", 14, 1616), ("P", 15, 2116)]:
    ok(pow(m, 13, 2537), c, f"RSA {ch} encrypts to {c}")
    ok(pow(c, 937, 2537), m, f"RSA {c} decrypts back to {m}")
ok(pow(31, 7, 33), 4, "RSA p=3,q=11,e=7,m=31 -> C=4")
ok(pow(4, 3, 33), 31, "RSA C=4 decrypts to 31")
# --- least positive x ---
ok(71 % 8, 7, "71=x mod 8 -> x=7")
ok((67 + 2) % 4, 1, "67+x=1 mod 4 -> x=2")
ok((89 - 3) % 5, 1, "89=(x+3) mod 5 -> x=1")
ok((78 + 5) % 5, 3, "78+x=3 mod 5 -> x=5")
ok((89 - 3) % 4, 2, "89=(x+3) mod 4 -> x=2")
# --- polynomial congruences ---
ok(sorted(x for x in range(5) if (x * x + 2 * x - 3) % 5 == 0), [1, 2], "x^2+2x-3 mod 5")
ok(sorted(x for x in range(9) if (x * x + 2 * x - 3) % 9 == 0), [1, 6], "x^2+2x-3 mod 9")

# --- Important Questions Module 2 / 3 numbers ---
import numpy as np

def line(x, y):
    x = np.array(x, float); y = np.array(y, float); n = len(x)
    A = np.array([[n, x.sum()], [x.sum(), (x * x).sum()]])
    B = np.array([y.sum(), (x * y).sum()])
    return np.linalg.solve(A, B)

ok(np.allclose(line([-2, -1, 0, 1, 2], [1, 2, 3, 3, 4]), [2.6, 0.7]), True, "imp M2 Q1 line a=2.6 b=0.7")
ok(np.allclose(line([1, 2, 3, 4, 5], [2, 5, 3, 8, 7]), [1.1, 1.3]), True, "imp M2 Q2 line a=1.1 b=1.3")

def parab(x, y):
    x = np.array(x, float); y = np.array(y, float); n = len(x)
    A = np.array([[n, x.sum(), (x * x).sum()],
                  [x.sum(), (x * x).sum(), (x ** 3).sum()],
                  [(x * x).sum(), (x ** 3).sum(), (x ** 4).sum()]])
    B = np.array([y.sum(), (x * y).sum(), ((x * x) * y).sum()])
    return np.linalg.solve(A, B)

ok(np.allclose(parab([-2, -1, 0, 1, 2], [-3.15, -1.39, 0.62, 2.88, 5.378]),
               [0.6210, 2.1326, 0.12328], atol=1e-4), True, "imp M2 Q3 parabola")
ok(np.allclose(parab([1, 2, 3, 4, 5], [10, 12, 13, 16, 19]),
               [9.4, 17 / 35, 2 / 7], atol=1e-6), True, "imp/assignment Q6 parabola")

def power(x, y):
    X = np.log(np.array(x, float)); Y = np.log(np.array(y, float)); n = len(x)
    A = np.array([[n, X.sum()], [X.sum(), (X * X).sum()]])
    B = np.array([Y.sum(), (X * Y).sum()])
    Av, Bv = np.linalg.solve(A, B)
    return Av, Bv, np.exp(Av)

Av, Bv, a_ = power([1, 2, 3, 4, 5], [0.5, 2, 4.5, 8, 12.5])
ok(abs(Bv - 2) < 1e-9 and abs(a_ - 0.5) < 1e-9, True, "imp M2 Q5 power y=0.5 x^2")
Av, Bv, a_ = power([2, 3, 4, 5], [27.8, 62.1, 110, 161])
ok(abs(Bv - 1.9302) < 1e-4 and abs(a_ - 7.3799) < 1e-4, True, "imp M2 Q6 / assignment Q7 power a=7.3799 b=1.9302")

# assignment Q8 correlation/regression
x = np.array([65, 66, 67, 67, 68, 69, 70, 72], float)
y = np.array([67, 68, 65, 68, 72, 72, 69, 71], float)
n = 8
Sxx = (x * x).sum() - x.sum() ** 2 / n
Syy = (y * y).sum() - y.sum() ** 2 / n
Sxy = (x * y).sum() - x.sum() * y.sum() / n
ok((round(Sxx), round(Syy), round(Sxy)), (36, 44, 24), "assignment Q8 Sxx,Syy,Sxy")
ok(abs(Sxy / (Sxx * Syy) ** 0.5 - 0.603) < 5e-4, True, "assignment Q8 r=0.603")
ok(abs(Sxy / Sxx - 0.6667) < 1e-4 and abs(69 - (Sxy / Sxx) * 68 - 23.6667) < 1e-3, True, "assignment Q8 y-on-x line")
ok(abs(Sxy / Syy - 0.5455) < 1e-4 and abs(68 - (Sxy / Syy) * 69 - 30.3636) < 1e-3, True, "assignment Q8 x-on-y line")

# imp M3
from fractions import Fraction as F
from math import comb
p = [F(1, 8), F(3, 8), F(3, 8), F(1, 8)]
m = sum(F(a) * b for a, b in zip([10, 20, 30, 40], p))
ex2 = sum(F(a * a) * b for a, b in zip([10, 20, 30, 40], p))
ok((m, ex2 - m * m), (25, 75), "imp M3 Q1 mean 25 var 75")
k = F(1, 10)
P = [F(0), k, 2 * k, 2 * k, 3 * k, k * k, 2 * k * k, 7 * k * k + k]
ok((sum(P), sum(P[:6]), sum(P[6:]), sum(P[4:7])), (F(1), F(81, 100), F(19, 100), F(33, 100)), "imp M3 Q2 k-table")
tot = comb(12, 2)
pr = [F(comb(3, i) * comb(9, 2 - i), tot) for i in [0, 1, 2]]
mm = sum(F(i) * pp for i, pp in zip([0, 1, 2], pr))
vv = sum(F(i * i) * pp for i, pp in zip([0, 1, 2], pr)) - mm * mm
ok((pr, mm, vv), ([F(6, 11), F(9, 22), F(1, 22)], F(1, 2), F(15, 44)), "imp M3 Q3 apples")
k5 = F(1, 49)
P5 = [(2 * i + 1) * k5 for i in range(7)]
ok((sum(P5[5:]), sum(P5[3:7]), sum(P5[:4])), (F(24, 49), F(40, 49), F(16, 49)), "imp M3 Q5 k,3k,... table")

print()
if fails:
    print(f"{len(fails)} FAILURES:")
    for f in fails:
        print(" ", f)
    raise SystemExit(1)
print("ALL MODULE 1 + IMP + ASSIGNMENT VERIFICATIONS PASSED OK")
