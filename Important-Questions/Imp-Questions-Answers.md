# Important Questions - Full Answers

Subject: Mathematics for Computer Science (3rd sem, VTU)

These are the questions from the college "Maths Important Questions" sheet. The
answers follow the class notes step by step. Where the notes themselves have a
slip, it is marked with a WARNING and the corrected value is used, so do not copy
that line from the notes into your answer book. Every number was checked by
computer before writing.

Contents:

- Module 1 (Modular Arithmetic): questions 1 to 8
- Module 2 (Statistics / Curve Fitting): questions 1 to 6
- Module 3 (Probability Distributions): questions 1 to 6

---

# MODULE 1: MODULAR ARITHMETIC

## Q.1 Find the last digit of (i) 7^2013 (ii) 13^37

**(i) Last digit of 7^2013**

The last digits of powers of 7 repeat in a cycle of 4:

| Power | 7^1 | 7^2 | 7^3 | 7^4 | 7^5 |
|---|---|---|---|---|---|
| Last digit | 7 | 9 | 3 | 1 | 7 |

So the cycle is 7, 9, 3, 1 with length 4.

Divide the power by 4 and keep the remainder:
2013 = 4 x 503 + 1, so the remainder is 1.

The first number of the cycle is 7.

**Last digit of 7^2013 = 7**

**(ii) Last digit of 13^37**

The last digits of powers of 13 repeat in a cycle of 4:

| Power | 13^1 | 13^2 | 13^3 | 13^4 | 13^5 |
|---|---|---|---|---|---|
| Last digit | 3 | 9 | 7 | 1 | 3 |

Cycle is 3, 9, 7, 1 with length 4.

37 = 4 x 9 + 1, remainder 1, so we take the first number of the cycle.

**Last digit of 13^37 = 3**

## Q.2 Find the remainder when (i) 2^23 is divided by 47 (ii) 4^8 is divided by 23

**(i) Remainder of 2^23 / 47**

Fermat's little theorem: for prime p and a not divisible by p,
a^(p-1) = 1 (mod p). Here p = 47, a = 2:

2^46 = 1 (mod 47), so 2^23 x 2^23 = 1 (mod 47). This means 2^23 is a self inverse,
so 2^23 = 1 or -1 (mod 47). Compute by repeated squaring:

2^2 = 4
2^4 = 16
2^8 = 256 = 256 - 5(47) = 21 (mod 47)
2^16 = 21^2 = 441 = 441 - 9(47) = 18 (mod 47)

2^23 = 2^16 x 2^4 x 2^2 x 2 = 18 x 16 x 4 x 2 (mod 47)
18 x 16 = 288 = 6 (mod 47)
6 x 4 = 24
24 x 2 = 48 = 1 (mod 47)

**Remainder of 2^23 divided by 47 = 1**

**(ii) Remainder of 4^8 / 23**

By Fermat with p = 23, a = 4: 4^22 = 1 (mod 23). But 4^8 is small enough to get
by squaring:

4^2 = 16
4^4 = 16^2 = 256 = 256 - 11(23) = 256 - 253 = 3 (mod 23)
4^8 = 3^2 = 9 (mod 23)

**Remainder of 4^8 divided by 23 = 9**

## Q.3 Show that 2^340 - 1 is divisible by 31 (Fermat's little theorem)

Fermat's little theorem with p = 31 (prime), a = 2:

2^30 = 1 (mod 31)

Now 340 = 30 x 11 + 10, so:

2^340 = (2^30)^11 x 2^10 = 1 x 2^10 (mod 31)

2^10 = 1024. Divide: 1024 = 33 x 31 + 1, so 2^10 = 1 (mod 31).

Therefore 2^340 = 1 (mod 31), that is, 2^340 - 1 = 0 (mod 31).

**Hence 2^340 - 1 is divisible by 31.**

Shortcut: 2^5 = 32 = 1 (mod 31) and 340 = 5 x 68, so 2^340 = (2^5)^68 = 1. Both
routes are correct, the Fermat route is the one asked.

## Q.4 Solve by Chinese remainder theorem: x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7)

The moduli 3, 5, 7 are pairwise coprime, so the CRT applies.

Step 1: M = 3 x 5 x 7 = 105.

Step 2: partial products M1 = M/3 = 35, M2 = M/5 = 21, M3 = M/7 = 15.

Step 3: inverses.
- 35 = 2 (mod 3). Solve 2y = 1 (mod 3): y1 = 2 (2 x 2 = 4 = 1).
- 21 = 1 (mod 5). y2 = 1.
- 15 = 1 (mod 7). y3 = 1.

Step 4: X = r1 M1 y1 + r2 M2 y2 + r3 M3 y3 (mod M)

X = 2 x 35 x 2 + 3 x 21 x 1 + 2 x 15 x 1
X = 140 + 63 + 30 = 233

Step 5: X = 233 (mod 105) = 233 - 2(105) = 23.

**x = 23 (mod 105)**

Check: 23 = 2 (mod 3), 23 = 3 (mod 5), 23 = 2 (mod 7). Correct.

## Q.5 Solve by Chinese remainder theorem: x = 1 (mod 4), x = 3 (mod 5), x = 2 (mod 7)

Moduli 4, 5, 7 are pairwise coprime.

M = 4 x 5 x 7 = 140.
M1 = 140/4 = 35, M2 = 140/5 = 28, M3 = 140/7 = 20.

Inverses:
- 35 = 3 (mod 4). Solve 3y = 1 (mod 4): y1 = 3 (3 x 3 = 9 = 1 mod 4).
- 28 = 3 (mod 5). Solve 3y = 1 (mod 5): y2 = 2 (3 x 2 = 6 = 1 mod 5).
- 20 = 6 (mod 7). Solve 6y = 1 (mod 7): y3 = 6 (6 x 6 = 36 = 1 mod 7).

X = 1 x 35 x 3 + 3 x 28 x 2 + 2 x 20 x 6
X = 105 + 168 + 240 = 513

X = 513 (mod 140) = 513 - 3(140) = 513 - 420 = 93.

**x = 93 (mod 140)**

Check: 93 = 1 (mod 4) (93 = 92 + 1), 93 = 3 (mod 5) (93 = 90 + 3),
93 = 2 (mod 7) (93 = 91 + 2). Correct.

## Q.6 Solve the linear congruence 10x = 15 (mod 35)

a = 10, b = 15, n = 35.

Step 1: d = gcd(10, 35) = 5. Since 5 divides 15, solutions exist and there are
exactly d = 5 solutions.

Step 2: divide everything by 5:
2x = 3 (mod 7).

Step 3: inverse of 2 mod 7 is 4 (2 x 4 = 8 = 1 mod 7).

x0 = 3 x 4 = 12 = 5 (mod 7).

Step 4: solutions are x0 + k(n/d) = 5 + 7k for k = 0, 1, 2, 3, 4:

**x = 5, 12, 19, 26, 33 (mod 35)**

Check: 10 x 5 = 50 = 50 - 35 = 15 (mod 35). Correct.
10 x 12 = 120 = 120 - 3(35) = 15 (mod 35). Correct.

## Q.7 Solve the system: 3x + 4y = 5 (mod 13), 2x + 5y = 7 (mod 13)

Eliminate y. Multiply Eq1 by 5 and Eq2 by 4 so that both have 20y:

Eq1 x 5: 15x + 20y = 25 = 12 (mod 13)
Eq2 x 4: 8x + 20y = 28 = 2 (mod 13)

Subtract: (15x + 20y) - (8x + 20y) = 12 - 2
7x = 10 (mod 13)

Inverse of 7 mod 13: 7 x 2 = 14 = 1 (mod 13), so the inverse is 2.

x = 10 x 2 = 20 = 7 (mod 13). **x = 7**

Substitute into Eq1: 3(7) + 4y = 5 (mod 13)
21 + 4y = 5, so 4y = 5 - 21 = -16 = -16 + 26 = 10 (mod 13).

Inverse of 4 mod 13: 4 x 10 = 40 = 1 (mod 13), so the inverse is 10.

y = 10 x 10 = 100 = 100 - 7(13) = 100 - 91 = 9 (mod 13). **y = 9**

**Solution: x = 7, y = 9 (mod 13)**

Check: 3(7) + 4(9) = 21 + 36 = 57 = 57 - 52 = 5 (mod 13). Correct.
2(7) + 5(9) = 14 + 45 = 59 = 59 - 52 = 7 (mod 13). Correct.

## Q.8 Find the remainder when (i) 135 x 74 x 48 is divided by 7 (ii) 175 x 113 x 53 is divided by 11 (iii) 135 x 146 x 73 is divided by 7

Method from the notes: reduce each factor mod the divisor first, then multiply
the small remainders.

**(i) 135 x 74 x 48 mod 7**

135 = 7(19) + 2 = 2 (mod 7)
74 = 7(10) + 4 = 4 (mod 7)
48 = 7(6) + 6 = 6 (mod 7)

Product = 2 x 4 x 6 = 48 = 48 - 42 = 6 (mod 7)

**Remainder = 6**

**(ii) 175 x 113 x 53 mod 11**

175 = 11(15) + 10 = 10 = -1 (mod 11)
113 = 11(10) + 3 = 3 (mod 11)
53 = 44 + 9 = 9 = -2 (mod 11)

Product = (-1) x 3 x (-2) = 6 (mod 11)

**Remainder = 6**

**(iii) 135 x 146 x 73 mod 7**

135 = 2 (mod 7)
146 = 7(20) + 6 = 6 = -1 (mod 7)
73 = 70 + 3 = 3 (mod 7)

Product = 2 x (-1) x 3 = -6 = 1 (mod 7)

**Remainder = 1**

---

# MODULE 2: STATISTICS (CURVE FITTING)

## Q.1 Fit a straight line y = ax + b for the data:

x: -2, -1, 0, 1, 2
y: 1, 2, 3, 3, 4

The normal equations for the least squares straight line y = ax + b are:

Sum(y) = n b + a Sum(x)
Sum(xy) = b Sum(x) + a Sum(x^2)

Table of sums:

| x | y | xy | x^2 |
|---|---|---|---|
| -2 | 1 | -2 | 4 |
| -1 | 2 | -2 | 1 |
| 0 | 3 | 0 | 0 |
| 1 | 3 | 3 | 1 |
| 2 | 4 | 8 | 4 |
| **Sum** | **13** | **7** | **10** |

Sum(x) = 0, Sum(y) = 13, Sum(xy) = 7, Sum(x^2) = 10, n = 5.

Normal equations:
13 = 5b + a(0) ... (1)
7 = b(0) + 10a ... (2)

From (1): b = 13/5 = 2.6
From (2): a = 7/10 = 0.7

**y = 0.7x + 2.6**

(This is the same answer as the notes, which write it as y = ax + b with
a = 13/5 and b = 7/10 in the other notation. If you write y = ax + b then
a = 0.7 and b = 2.6. Match the notation to how the question prints it.)

## Q.2 Fit a straight line for the data:

x: 1, 2, 3, 4, 5
y: 2, 5, 3, 8, 7

Table of sums:

| x | y | xy | x^2 |
|---|---|---|---|
| 1 | 2 | 2 | 1 |
| 2 | 5 | 10 | 4 |
| 3 | 3 | 9 | 9 |
| 4 | 8 | 32 | 16 |
| 5 | 7 | 35 | 25 |
| **15** | **25** | **88** | **55** |

n = 5, Sum(x) = 15, Sum(y) = 25, Sum(xy) = 88, Sum(x^2) = 55.

Normal equations:
25 = 5a + 15b ... (1)
88 = 15a + 55b ... (2)

From (1): a = (25 - 15b)/5 = 5 - 3b.
Substitute in (2): 88 = 15(5 - 3b) + 55b = 75 - 45b + 55b = 75 + 10b
10b = 13, so b = 1.3, and a = 5 - 3(1.3) = 5 - 3.9 = 1.1.

**y = 1.1 + 1.3x** (writing y = a + bx), or **y = 1.3x + 1.1** (y = ax + b form).

Same answer as the notes.

## Q.3 Fit a parabola y = a + bx + cx^2 for the data:

x: -2, -1, 0, 1, 2
y: -3.15, -1.39, 0.62, 2.88, 5.378

The normal equations for the parabola are:

Sum(y) = n a + b Sum(x) + c Sum(x^2)
Sum(xy) = a Sum(x) + b Sum(x^2) + c Sum(x^3)
Sum(x^2 y) = a Sum(x^2) + b Sum(x^3) + c Sum(x^4)

Table of sums:

| x | y | xy | x^2 | x^2 y | x^3 | x^4 |
|---|---|---|---|---|---|---|
| -2 | -3.15 | 6.30 | 4 | -12.60 | -8 | 16 |
| -1 | -1.39 | 1.39 | 1 | -1.39 | -1 | 1 |
| 0 | 0.62 | 0 | 0 | 0 | 0 | 0 |
| 1 | 2.88 | 2.88 | 1 | 2.88 | 1 | 1 |
| 2 | 5.378 | 10.756 | 4 | 21.512 | 8 | 16 |
| **0** | **4.338** | **21.326** | **10** | **10.402** | **0** | **34** |

Normal equations:
4.338 = 5a + 0b + 10c ... (1)
21.326 = 0a + 10b + 0c ... (2)
10.402 = 10a + 0b + 34c ... (3)

From (2): b = 2.1326.

From (1): 5a + 10c = 4.338 ... (1)
From (3): 10a + 34c = 10.402 ... (3)

Multiply (1) by 2: 10a + 20c = 8.676. Subtract from (3):
14c = 1.726, so c = 0.12328.

Then from (1): 5a = 4.338 - 1.2328 = 3.1052, so a = 0.6210.

**y = 0.6210 + 2.1326x + 0.1233x^2**

Same answer as the notes (a = 0.6210, b = 2.1326, c = 0.12328).

## Q.4 Fit a parabola for the data:

x: 1, 2, 3, 4, 5
y: 10, 12, 13, 16, 19

Table of sums:

| x | y | xy | x^2 | x^2 y | x^3 | x^4 |
|---|---|---|---|---|---|---|
| 1 | 10 | 10 | 1 | 10 | 1 | 1 |
| 2 | 12 | 24 | 4 | 48 | 8 | 16 |
| 3 | 13 | 39 | 9 | 117 | 27 | 81 |
| 4 | 16 | 64 | 16 | 256 | 64 | 256 |
| 5 | 19 | 95 | 25 | 475 | 125 | 625 |
| **15** | **70** | **232** | **55** | **906** | **225** | **979** |

Normal equations:
70 = 5a + 15b + 55c ... (1)
232 = 15a + 55b + 225c ... (2)
906 = 55a + 225b + 979c ... (3)

Solving the three equations:

(1) x 3: 210 = 15a + 45b + 165c. Subtract from (2) x 1:
232 - 210 = 10b + 60c, so 22 = 10b + 60c, that is b + 6c = 2.2 ... (4)

(1) x 11: 770 = 55a + 165b + 605c. Subtract from (3):
906 - 770 = 60b + 374c, so 136 = 60b + 374c ... (5)

From (4): b = 2.2 - 6c. Substitute in (5):
136 = 60(2.2 - 6c) + 374c = 132 - 360c + 374c = 132 + 14c
14c = 4, so c = 2/7 = 0.2857.
Then b = 2.2 - 6(0.2857) = 2.2 - 1.7143 = 0.4857.
From (1): 5a = 70 - 15(0.4857) - 55(0.2857) = 70 - 7.2857 - 15.7143 = 47,
so a = 9.4.

**y = 9.4 + 0.4857x + 0.2857x^2**

Same answer as the notes.

## Q.5 Fit a power curve y = a x^b for the data:

x: 1, 2, 3, 4, 5
y: 0.5, 2, 4.5, 8, 12.5

For the power curve y = a x^b, take logs of both sides:
log y = log a + b log x.

Write A = log a, and put X = log x, Y = log y. Then the problem becomes fitting
the straight line Y = A + bX.

Table of sums:

| x | y | X = log x | Y = log y | XY | X^2 |
|---|---|---|---|---|---|
| 1 | 0.5 | 0.0000 | -0.6931 | 0.0000 | 0.0000 |
| 2 | 2 | 0.6931 | 0.6931 | 0.4805 | 0.4805 |
| 3 | 4.5 | 1.0986 | 1.5041 | 1.6524 | 1.2069 |
| 4 | 8 | 1.3863 | 2.0794 | 2.8827 | 1.9218 |
| 5 | 12.5 | 1.6094 | 2.5257 | 4.0650 | 2.5903 |
| | | **4.7875** | **6.1092** | **9.0806** | **6.1995** |

Normal equations:
Sum(Y) = nA + b Sum(X)
Sum(XY) = A Sum(X) + b Sum(X^2)

6.1092 = 5A + 4.7875b ... (1)
9.0806 = 4.7875A + 6.1995b ... (2)

Solving: from (1) A = (6.1092 - 4.7875b)/5. Substitute in (2):

9.0806 = 4.7875(6.1092 - 4.7875b)/5 + 6.1995b
9.0806 = 5.8537 - 4.5865b + 6.1995b
9.0806 - 5.8537 = 1.613b
3.2269 = 1.613b
b = 2.0000

A = (6.1092 - 4.7875 x 2)/5 = (6.1092 - 9.575)/5 = -3.4658/5 = -0.6931

a = e^A = e^(-0.6931) = 0.5

**y = 0.5 x^2**

(Check: 0.5(1)^2 = 0.5, 0.5(4) = 2, 0.5(9) = 4.5, 0.5(16) = 8, 0.5(25) = 12.5.
The fit is exact, the data was made from y = 0.5x^2.)

## Q.6 Fit a power curve y = a x^b for the data:

x: 2, 3, 4, 5
y: 27.8, 62.1, 110, 161

Same method: X = log x, Y = log y, fit Y = A + bX with A = log a.

Table of sums:

| x | y | X = log x | Y = log y | XY | X^2 |
|---|---|---|---|---|---|
| 2 | 27.8 | 0.6931 | 3.3250 | 2.3047 | 0.4805 |
| 3 | 62.1 | 1.0986 | 4.1287 | 4.5359 | 1.2069 |
| 4 | 110 | 1.3863 | 4.7005 | 6.5162 | 1.9218 |
| 5 | 161 | 1.6094 | 5.0814 | 8.1782 | 2.5903 |
| | | **4.7875** | **17.2357** | **21.5351** | **6.1995** |

Normal equations (n = 4):
17.2357 = 4A + 4.7875b ... (1)
21.5351 = 4.7875A + 6.1995b ... (2)

From (1): A = (17.2357 - 4.7875b)/4 = 4.3089 - 1.1969b.

Substitute in (2):
21.5351 = 4.7875(4.3089 - 1.1969b) + 6.1995b
21.5351 = 20.6273 - 5.7299b + 6.1995b
21.5351 - 20.6273 = 0.4696b
0.9078 = 0.4696b
b = 1.9302

A = 4.3089 - 1.1969(1.9302) = 4.3089 - 2.3101 = 1.9988

a = e^A = e^1.9988 = 7.3799

**y = 7.3799 x^1.9302**

WARNING (notes slip): the notes print log 2 = 0.6981 in the X column, which
should be 0.6931. Because of this the notes get b = 1.9406 and a = 7.27. The
correct values are b = 1.9302 and a = 7.3799 (approximately 7.38). The steps are
the same, only that one log value was mistyped in the notes.

---

# MODULE 3: PROBABILITY DISTRIBUTIONS

## Q.1 A random variable X takes the values 10, 20, 30, 40 with probabilities
1/8, 3/8, 3/8, 1/8. Show that it is a probability distribution and find its
mean and variance.

**Check that it is a probability distribution:**

Each probability is between 0 and 1, and

1/8 + 3/8 + 3/8 + 1/8 = 8/8 = 1.

Since the probabilities are non negative and add up to 1, it is a valid
probability distribution.

**Mean:**

E(X) = Sum x P(x)
= 10(1/8) + 20(3/8) + 30(3/8) + 40(1/8)
= (10 + 60 + 90 + 40)/8
= 200/8 = 25

**Mean = 25**

**Variance:**

E(X^2) = Sum x^2 P(x)
= 100(1/8) + 400(3/8) + 900(3/8) + 1600(1/8)
= (100 + 1200 + 2700 + 1600)/8
= 5600/8 = 700

Variance = E(X^2) - [E(X)]^2 = 700 - 625 = 75

**Variance = 75**

## Q.2 A random variable X takes values 0, 1, 2, 3, 4, 5, 6, 7 with probabilities
0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2 + k. Find k, P(X < 6), P(X >= 6) and P(3 < X <= 6).

**Find k:**

The probabilities must add up to 1:

0 + k + 2k + 2k + 3k + k^2 + 2k^2 + (7k^2 + k) = 1
10k^2 + 9k = 1
10k^2 + 9k - 1 = 0

Factor: (10k - 1)(k + 1) = 0

k = 1/10 or k = -1. A probability cannot be negative, so

**k = 1/10 = 0.1**

The full distribution with k = 1/10:

| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| P(x) | 0 | 0.1 | 0.2 | 0.2 | 0.3 | 0.01 | 0.02 | 0.17 |

(Check: 0 + 0.1 + 0.2 + 0.2 + 0.3 + 0.01 + 0.02 + 0.17 = 1.)

**P(X < 6):**

P(X < 6) = P(0) + P(1) + P(2) + P(3) + P(4) + P(5)
= 0 + 0.1 + 0.2 + 0.2 + 0.3 + 0.01 = 0.81

**P(X < 6) = 81/100 = 0.81**

**P(X >= 6):**

P(X >= 6) = P(6) + P(7) = 0.02 + 0.17 = 0.19

**P(X >= 6) = 19/100 = 0.19**

(Check: 0.81 + 0.19 = 1, correct.)

**P(3 < X <= 6):**

P(3 < X <= 6) = P(4) + P(5) + P(6) = 0.3 + 0.01 + 0.02 = 0.33

**P(3 < X <= 6) = 33/100 = 0.33**

NOTE: the imp sheet prints only 7 probability entries (0, k, 2k, 2k, 3k, k^2,
7k^2 + k), which does not give a clean k. The actual VTU question (it appears in
three BCS301 papers) has 8 entries as solved above, and k = 1/10. Solve the
8 value version.

## Q.3 A lot of 12 apples contains 3 perished ones. Two apples are picked at
random. Find the probability distribution of the number of perished apples, and
its mean and variance.

Let X = number of perished apples among the 2 picked. X can be 0, 1 or 2.

Total ways to pick 2 apples from 12 = 12C2 = 66.

P(X = 0) = both good = 9C2 / 12C2 = 36/66 = 6/11
P(X = 1) = one perished, one good = (3C1 x 9C1) / 12C2 = 27/66 = 9/22
P(X = 2) = both perished = 3C2 / 12C2 = 3/66 = 1/22

Check: 6/11 + 9/22 + 1/22 = 12/22 + 9/22 + 1/22 = 22/22 = 1.

| x | 0 | 1 | 2 |
|---|---|---|---|
| P(x) | 6/11 | 9/22 | 1/22 |

**Mean:**

E(X) = 0(6/11) + 1(9/22) + 2(1/22) = 9/22 + 2/22 = 11/22 = 1/2

**Mean = 1/2**

**Variance:**

E(X^2) = 0 + 1(9/22) + 4(1/22) = 9/22 + 4/22 = 13/22

Variance = E(X^2) - [E(X)]^2 = 13/22 - 1/4 = 26/44 - 11/44 = 15/44

**Variance = 15/44**

(If the question instead asks for the number of GOOD apples, the distribution
reverses to 1/22, 9/22, 6/11, the mean becomes 3/2 and the variance stays
15/44.)

## Q.4 Derive the mean and variance of the Binomial distribution.

A binomial random variable X counts the number of successes in n independent
trials, where each trial has success probability p. Write q = 1 - p. Then:

P(X = r) = nCr p^r q^(n-r), r = 0, 1, 2, ..., n

**Mean:**

E(X) = Sum over r of r x nCr p^r q^(n-r)

The r = 0 term vanishes (r = 0), so start from r = 1:

E(X) = Sum r=1..n of r x nCr p^r q^(n-r)

Use the identity r x nCr = n x (n-1)C(r-1). (Take r common: r nCr =
n (n-1) C (r-1).)

E(X) = n p x Sum r=1..n of (n-1)C(r-1) p^(r-1) q^(n-r)

Put s = r - 1:

E(X) = n p x Sum s=0..n-1 of (n-1)Cs p^s q^(n-1-s)

The sum is the binomial expansion of (p + q)^(n-1) = 1^(n-1) = 1.

**E(X) = n p x 1 = n p**

**Variance:**

E(X^2) = Sum r^2 nCr p^r q^(n-r) = Sum [r(r-1) + r] nCr p^r q^(n-r)
= Sum r(r-1) nCr p^r q^(n-r) + E(X)

For the first sum, use r(r-1) nCr = n(n-1) (n-2)C(r-2):

Sum r=0..n of r(r-1) nCr p^r q^(n-r)
= n(n-1) p^2 x Sum t=0..n-2 of (n-2)Ct p^t q^(n-2-t)
= n(n-1) p^2 x (p + q)^(n-2) = n(n-1) p^2

So E(X^2) = n(n-1) p^2 + n p.

Variance = E(X^2) - [E(X)]^2
= n(n-1) p^2 + n p - n^2 p^2
= n^2 p^2 - n p^2 + n p - n^2 p^2
= n p - n p^2
= n p (1 - p) = n p q

**Mean = n p, Variance = n p q**

## Q.5 A random variable X takes values 0, 1, 2, 3, 4, 5, 6 with probabilities
k, 3k, 5k, 7k, 9k, 11k, 13k. Find k, P(X >= 5), P(3 <= X <= 6) and P(X < 4).

**Find k:**

k + 3k + 5k + 7k + 9k + 11k + 13k = 1
49k = 1

**k = 1/49**

The distribution:

| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| P(x) | 1/49 | 3/49 | 5/49 | 7/49 | 9/49 | 11/49 | 13/49 |

**P(X >= 5):**

P(X >= 5) = P(5) + P(6) = 11/49 + 13/49 = 24/49

**P(X >= 5) = 24/49**

**P(3 <= X <= 6):**

P(3 <= X <= 6) = P(3) + P(4) + P(5) + P(6) = (7 + 9 + 11 + 13)/49 = 40/49

**P(3 <= X <= 6) = 40/49**

**P(X < 4):**

P(X < 4) = P(0) + P(1) + P(2) + P(3) = (1 + 3 + 5 + 7)/49 = 16/49

**P(X < 4) = 16/49**

## Q.6 A random variable X takes the values -3, -2, -1, 0, 1, 2, 3, with
P(X = 0) = P(X < 0) = P(X > 0). Find the probability distribution of X.

The three events {X < 0}, {X = 0} and {X > 0} cover every outcome, so their
probabilities must add up to 1:

P(X < 0) + P(X = 0) + P(X > 0) = 1

All three are equal, so each equals 1/3:

**P(X = 0) = P(X < 0) = P(X > 0) = 1/3**

Now, X < 0 covers the three values -3, -2, -1. Assuming equal probability for
each:

P(-3) + P(-2) + P(-1) = 1/3, so each is (1/3)/3 = 1/9.

Similarly for X > 0 (values 1, 2, 3): each is 1/9.

The distribution:

| x | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| P(x) | 1/9 | 1/9 | 1/9 | 1/3 | 1/9 | 1/9 | 1/9 |

Check: 3(1/9) + 1/3 + 3(1/9) = 1/3 + 1/3 + 1/3 = 1. Correct.

---

## Notes errors found while checking (summary)

1. Power curve question 6 (x = 2..5): the notes' X column prints log 2 = 0.6981,
   it should be 0.6931. So the notes' b = 1.9406 and a = 7.27 are slightly off.
   Correct: b = 1.9302, a = 7.3799.
2. Euler's theorem example in the notes (23^130 mod 25) uses phi(25) = 16.
   Actually phi(25) = phi(5^2) = 25(1 - 1/5) = 20. With 23^20 = 1 (mod 25), the
   answer comes out as 24, not 11.
3. The notes' CRT worked example with moduli 9 and 10 (the 4x = 5 and 2x = 6
   problem) uses a wrong total modulus M = 180 and mixes up one residue. The
   correct modulus is M = 90 and the answer is x = 53 (mod 90).
4. The imp sheet's probability table question prints 7 entries; the real VTU
   question (3 papers) has 8 entries, giving k = 1/10. Solved above with 8.

The three-item list above only covers items that touch the imp questions or
nearby worked examples. A fuller list of checked corrections for the statistics
part of the notes (parabola sign slip, correlation constant, regression r sign)
is included with the notes checks in this repo's verification scripts.
