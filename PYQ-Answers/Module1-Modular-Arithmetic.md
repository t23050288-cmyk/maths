# PYQ Answers - Module 1: Modular Arithmetic

Subject: Mathematics for Computer Science (3rd sem, VTU) | Module 1: Modular Arithmetic

Source: 7 previous BMATS101 (CSE stream) papers. The modular arithmetic questions
come as Q.7 / Q.8 of those papers (their Module 4). Every answer below was checked
by computer before writing. The steps follow the class notes pattern: reduce the
base, find the cycle, apply Fermat / Wilson / CRT as needed, show every step.

Papers covered:

1. Jan/Feb 2023 (BMATS101)
2. June/July 2023 (BMATS101)
3. Dec 2023/Jan 2024 (BMATS101)
4. June/July 2024 (BMATS101)
5. June/July 2024 Supplementary (BMATSCS101)
6. Dec 2024/Jan 2025 (BMATS101)
7. June/July 2025 (BMATS101)

---

## Standard results used (from the notes)

**Fermat's little theorem:** if p is prime and p does not divide a, then
a^(p-1) = 1 (mod p).

**Wilson's theorem:** p is prime if and only if (p-1)! = -1 (mod p).

**Euler's theorem:** if gcd(a, n) = 1 then a^phi(n) = 1 (mod n), where
phi(n) counts the numbers from 1 to n that are coprime to n.

**Last digit trick:** the last digit of a^k repeats in a cycle.
- Powers of 7 end in 7, 9, 3, 1, 7, 9, ... (cycle of 4)
- Powers of 13 end in 3, 9, 7, 1, 3, 9, ... (cycle of 4)
So divide the power by 4 and keep the remainder.

**Linear congruence ax = b (mod n):** let d = gcd(a, n). If d divides b,
there are d solutions. Divide everything by d to get a'x = b' (mod n/d),
find x0 = b' x (a')^(-1) (mod n/d), then the solutions are
x0, x0 + n/d, x0 + 2(n/d), ... up to n.

**Chinese remainder theorem:** to solve x = r1 (mod m1), x = r2 (mod m2), ...
with coprime moduli: M = m1 m2 m3..., Mi = M/mi, then
X = r1 M1 y1 + r2 M2 y2 + ... (mod M), where yi is the inverse of Mi mod mi.

---

# Paper 1: Jan/Feb 2023 (BMATS101)

## Q.7 a) Find the last digit in 13^37. Find the remainder when 7^118 is divided by 10. [6]

**(i) Last digit of 13^37**

The last digits of 13, 13^2, 13^3, 13^4 are 3, 9, 7, 1 and then the cycle repeats.
So the cycle length is 4.

Divide the power by 4: 37 = 4 x 9 + 1, remainder 1.

The first digit of the cycle is 3.

**Last digit of 13^37 = 3**

**(ii) Remainder when 7^118 is divided by 10 (this is the last digit of 7^118)**

The last digits of 7, 7^2, 7^3, 7^4 are 7, 9, 3, 1 and then the cycle repeats. Cycle
length 4.

Divide the power by 4: 118 = 4 x 29 + 2, remainder 2.

The second digit of the cycle is 9.

**Remainder of 7^118 divided by 10 = 9**

## Q.7 b) Find the solutions of the linear congruence 12x = 6 (mod 21). [7]

Here a = 12, b = 6, n = 21.

Step 1: d = gcd(12, 21) = 3. Since 3 divides 6, solutions exist, and there are
exactly 3 solutions.

Step 2: divide everything by 3:
12x = 6 (mod 21) becomes 4x = 2 (mod 7).

Step 3: find the inverse of 4 mod 7. We need 4y = 1 (mod 7). Trying values,
4 x 2 = 8 = 1 (mod 7), so the inverse is 2.

Step 4: x0 = 2 x 2 = 4 (mod 7).

Step 5: the solutions mod 21 are x0, x0 + 7, x0 + 14:
**x = 4, 11, 18 (mod 21)**

Check: 12 x 4 = 48 = 48 - 42 = 6 (mod 21) correct.

## Q.7 c) Find the general solution of the linear Diophantine equation 70x + 112y = 168. [7]

Step 1: d = gcd(70, 112) = 14. Since 14 divides 168, solutions exist.

Step 2: divide the whole equation by 14:
5x + 8y = 12.

Step 3: solve 5x = 12 (mod 8). Reduce: 5x = 4 (mod 8). The inverse of 5 mod 8 is 5
(5 x 5 = 25 = 1 mod 8). So x = 4 x 5 = 20 = 4 (mod 8).

Step 4: take x = 4. Then 5(4) + 8y = 12 gives 8y = -8, so y = -1.
One solution is (x, y) = (4, -1). Check: 70(4) + 112(-1) = 280 - 112 = 168.

Step 5: the general solution of 5x + 8y = 12 is
**x = 4 + 8t, y = -1 - 5t, for any integer t.**

## Q.8 a) Find the remainder when 14! is divided by 17. [6]

Wilson's theorem: for a prime p, (p-1)! = -1 (mod p). Here p = 17, so
16! = -1 (mod 17).

Now 16! = 16 x 15 x 14!. Reduce 16 and 15 mod 17: 16 = -1 (mod 17) and
15 = -2 (mod 17). So:

16 x 15 x 14! = (-1)(-2) x 14! = 2 x 14! = -1 (mod 17)

2 x 14! = -1 (mod 17)
14! = -1 x (inverse of 2) (mod 17)

The inverse of 2 mod 17 is 9, because 2 x 9 = 18 = 1 (mod 17).

14! = -9 = 17 - 9 = 8 (mod 17)

**Remainder when 14! is divided by 17 is 8**

## Q.8 b) Solve the system of linear congruences: 7x + 3y = 10 (mod 16), 2x + 5y = 9 (mod 16). [7]

The notes method: eliminate one variable.

Multiply the first equation by 2 and the second by 7 so that the x terms match:

Eq1 x 2: 14x + 6y = 20 = 4 (mod 16)
Eq2 x 7: 14x + 35y = 63 = 15 (mod 16)

Subtract: (14x + 35y) - (14x + 6y) = 29y = 15 - 4 = 11 (mod 16)
So 29y = 11 (mod 16). Reduce 29 mod 16: 13y = 11 (mod 16).

Find the inverse of 13 mod 16: 13 x 5 = 65 = 65 - 64 = 1 (mod 16), so the inverse
is 5.

y = 11 x 5 = 55 = 55 - 48 = 7 (mod 16). **y = 7**

Substitute in equation 1: 7x + 3(7) = 10 (mod 16), so 7x + 21 = 10, that is
7x = -11 = 5 (mod 16).

Inverse of 7 mod 16: 7 x 7 = 49 = 1 (mod 16), so the inverse is 7.

x = 5 x 7 = 35 = 3 (mod 16). **x = 3**

**Solution: x = 3, y = 7 (mod 16)**

Check: 7(3) + 3(7) = 42 = 42 - 32 = 10 (mod 16) correct.
2(3) + 5(7) = 41 = 41 - 32 = 9 (mod 16) correct.

## Q.8 c) Solve x = 3 (mod 5), x = 2 (mod 6), x = 4 (mod 7) using the Chinese remainder theorem. [7]

The moduli 5, 6, 7 are pairwise coprime, so CRT applies.

M = 5 x 6 x 7 = 210.
M1 = 210/5 = 42, M2 = 210/6 = 35, M3 = 210/7 = 30.

Find each inverse:
- 42 = 2 (mod 5); we need 2y = 1 (mod 5), so y1 = 3 (2 x 3 = 6 = 1).
- 35 = 5 (mod 6); we need 5y = 1 (mod 6), so y2 = 5 (5 x 5 = 25 = 1).
- 30 = 2 (mod 7); we need 2y = 1 (mod 7), so y3 = 4 (2 x 4 = 8 = 1).

X = r1 M1 y1 + r2 M2 y2 + r3 M3 y3
X = 3 x 42 x 3 + 2 x 35 x 5 + 4 x 30 x 4
X = 378 + 350 + 480 = 1208

X = 1208 (mod 210). Divide: 210 x 5 = 1050, and 1208 - 1050 = 158.

**x = 158 (mod 210)**

Check: 158 = 3 (mod 5) correct (158 = 155 + 3). 158 = 2 (mod 6) correct
(158 = 156 + 2). 158 = 4 (mod 7) correct (158 = 154 + 4).

---

# Paper 2: June/July 2023 (BMATS101)

## Q.7 a) Find the least positive values of x such that (i) 78 + x = 3 (mod 5) (ii) 89 = (x + 3) (mod 4). [6]

**(i) 78 + x = 3 (mod 5)**

Reduce 78 mod 5: 78 = 75 + 3, so 78 = 3 (mod 5).

3 + x = 3 (mod 5), so x = 0 (mod 5).

The least positive value is **x = 5**.

**(ii) 89 = (x + 3) (mod 4)**

Reduce 89 mod 4: 89 = 88 + 1, so 89 = 1 (mod 4).

x + 3 = 1 (mod 4), so x = -2 = 2 (mod 4).

The least positive value is **x = 2**.

## Q.7 b) Find the solution of the linear congruence 14x = 12 (mod 18). [7]

a = 14, b = 12, n = 18.

d = gcd(14, 18) = 2. Since 2 divides 12, there are 2 solutions.

Divide everything by 2:
7x = 6 (mod 9).

Inverse of 7 mod 9: 7 x 4 = 28 = 1 (mod 9), so the inverse is 4.

x0 = 6 x 4 = 24 = 6 (mod 9).

Solutions mod 18: x = x0 and x0 + 9:
**x = 6, 15 (mod 18)**

Check: 14 x 6 = 84 = 84 - 72 = 12 (mod 18) correct.
14 x 15 = 210 = 210 - 198 = 12 (mod 18) correct.

## Q.7 c) Encrypt the message STOP using RSA with key (2537, 13) using the prime numbers 43 and 59. [7]

RSA steps:

1. Choose primes p = 43, q = 59.
2. n = p x q = 43 x 59 = 2537.
3. phi(n) = (p - 1)(q - 1) = 42 x 58 = 2436.
4. Encryption key e = 13 (given in the key pair (2537, 13)), with gcd(13, 2436) = 1.
5. Public key = (n, e) = (2537, 13).
6. Decryption key d: ed = 1 (mod phi), that is 13d = 1 (mod 2436).
   d = 937 because 13 x 937 = 12181 = 5 x 2436 + 1.

Convert letters to numbers: S = 18, T = 19, O = 14, P = 15 (A = 0, B = 1, ...).

Encrypt each block: C = m^e (mod n):

- S = 18: 18^13 (mod 2537) = 2222
- T = 19: 19^13 (mod 2537) = 2299
- O = 14: 14^13 (mod 2537) = 1616
- P = 15: 15^13 (mod 2537) = 2116

**Encrypted message: 2222 2299 1616 2116**

(Each cipher value decodes back correctly with d = 937: for example
2222^937 (mod 2537) = 18 = S.)

## Q.8 a) Find the remainder when 2^23 is divided by 47. [6]

Fermat's little theorem with p = 47 (prime) and a = 2:
2^46 = 1 (mod 47).

So 2^23 x 2^23 = 2^46 = 1 (mod 47), which means 2^23 is its own inverse mod 47,
so 2^23 = 1 or -1 (mod 47).

Compute step by step using repeated squaring:
2^2 = 4
2^4 = 16
2^8 = 256 = 256 - 5 x 47 = 256 - 235 = 21 (mod 47)
2^16 = 21^2 = 441 = 441 - 9 x 47 = 441 - 423 = 18 (mod 47)
2^23 = 2^16 x 2^4 x 2^2 x 2^1 = 18 x 16 x 4 x 2 (mod 47)

18 x 16 = 288 = 288 - 6 x 47 = 288 - 282 = 6 (mod 47)
6 x 4 = 24
24 x 2 = 48 = 1 (mod 47)

**Remainder when 2^23 is divided by 47 is 1**

## Q.8 b) Solve the system of linear congruences x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7) using the Remainder theorem (CRT). [7]

Moduli 3, 5, 7 are pairwise coprime.

M = 3 x 5 x 7 = 105.
M1 = 105/3 = 35, M2 = 105/5 = 21, M3 = 105/7 = 15.

Inverses:
- 35 = 2 (mod 3); 2y = 1 (mod 3) gives y1 = 2.
- 21 = 1 (mod 5); y2 = 1.
- 15 = 1 (mod 7); y3 = 1.

X = 2 x 35 x 2 + 3 x 21 x 1 + 2 x 15 x 1
X = 140 + 63 + 30 = 233

X = 233 (mod 105) = 233 - 210 = 23.

**x = 23 (mod 105)**

Check: 23 = 2 (mod 3), 23 = 3 (mod 5), 23 = 2 (mod 7). All correct.

## Q.8 c) Find the remainder when 175 x 113 x 53 is divided by 11. Also solve x^2 + 2x - 3 = 0 (mod 9). [7]

**(i) Remainder of 175 x 113 x 53 mod 11**

Reduce each factor mod 11:
175 = 11 x 15 + 10, so 175 = 10 = -1 (mod 11)
113 = 11 x 10 + 3, so 113 = 3 (mod 11)
53 = 44 + 9, so 53 = 9 = -2 (mod 11)

Product: (-1) x 3 x (-2) = 6 (mod 11)

**Remainder = 6**

**(ii) Solve x^2 + 2x - 3 = 0 (mod 9)**

Test x = 0 to 8:

| x | x^2 + 2x - 3 | mod 9 |
|---|---|---|
| 0 | -3 | 6 |
| 1 | 0 | 0 |
| 2 | 5 | 5 |
| 3 | 12 | 3 |
| 4 | 21 | 3 |
| 5 | 32 | 5 |
| 6 | 45 | 0 |
| 7 | 60 | 6 |
| 8 | 77 | 5 |

**Solutions: x = 1, 6 (mod 9)**

Note: some printed versions of this question read x^3 + 2x - 3 = 0 (mod 9). For
that cubic the solutions are x = 1, 2, 6 (mod 9), found the same way, by testing
each value.

---

# Paper 3: Dec 2023/Jan 2024 (BMATS101)

## Q.7 a) Find the last digit in 7^289. Find the remainder when 135 x 74 x 48 is divided by 7. [7]

**(i) Last digit of 7^289**

The last digits of powers of 7 cycle as 7, 9, 3, 1 with cycle length 4.
289 = 4 x 72 + 1, remainder 1, so we take the first digit of the cycle.

**Last digit of 7^289 = 7**

**(ii) Remainder of 135 x 74 x 48 divided by 7**

Reduce each factor mod 7:
135 = 7 x 19 + 2, so 135 = 2 (mod 7)
74 = 70 + 4, so 74 = 4 (mod 7)
48 = 42 + 6, so 48 = 6 (mod 7)

Product: 2 x 4 x 6 = 48 = 48 - 42 = 6 (mod 7)

**Remainder = 6**

## Q.7 b) Solve the linear congruence 6x = 15 (mod 21). [6]

a = 6, b = 15, n = 21.

d = gcd(6, 21) = 3. Since 3 divides 15, there are 3 solutions.

Divide everything by 3:
2x = 5 (mod 7).

Inverse of 2 mod 7: 2 x 4 = 8 = 1 (mod 7), so the inverse is 4.

x0 = 5 x 4 = 20 = 6 (mod 7).

Solutions mod 21: x = 6, 6 + 7, 6 + 14:
**x = 6, 13, 20 (mod 21)**

Check: 6 x 6 = 36 = 36 - 21 = 15 (mod 21) correct.

## Q.7 c) Using Wilson's theorem show that 4(29)! + 5! is divisible by 31. [7]

Wilson's theorem with p = 31 (prime):
(31 - 1)! = 30! = -1 (mod 31).

Split 30!: 30! = 30 x 29 x 28 x ... x 6 x 5!

Working mod 31: the numbers 30, 29, 28, ..., 6 are the same as -1, -2, -3, ..., -25
(mod 31). So:

30! = (-1)(-2)(-3)...(-25) x 5! = (-1)^25 x 25! x 5! = -25! x 5! (mod 31)

But the standard shortcut used in the notes is simpler. Since
30! = 30 x 29! = -1 (mod 31) and 30 = -1 (mod 31):

-1 x 29! = -1 (mod 31), so 29! = 1 (mod 31).

Also 5! = 120 = 120 - 3 x 31 = 120 - 93 = 27 (mod 31), so 5! = -4 (mod 31).

Therefore:
4(29)! + 5! = 4 x 1 + 27 = 31 = 0 (mod 31)

**So 4(29)! + 5! is divisible by 31.**

## Q.8 a) Solve the set of simultaneous congruences x = 5 (mod 3), x = 2 (mod 5), x = 1 (mod 11). [7]

First reduce x = 5 (mod 3): 5 = 2 (mod 3), so the system is
x = 2 (mod 3), x = 2 (mod 5), x = 1 (mod 11).

Moduli 3, 5, 11 are pairwise coprime.

M = 3 x 5 x 11 = 165.
M1 = 165/3 = 55, M2 = 165/5 = 33, M3 = 165/11 = 15.

Inverses:
- 55 = 1 (mod 3); y1 = 1.
- 33 = 3 (mod 5); 3y = 1 (mod 5) gives y2 = 2 (3 x 2 = 6 = 1).
- 15 = 4 (mod 11); 4y = 1 (mod 11) gives y3 = 3 (4 x 3 = 12 = 1).

X = 2 x 55 x 1 + 2 x 33 x 2 + 1 x 15 x 3
X = 110 + 132 + 45 = 287

X = 287 (mod 165) = 287 - 165 = 122.

**x = 122 (mod 165)**

Check: 122 = 2 (mod 3) correct, 122 = 2 (mod 5) correct, 122 = 1 (mod 11) correct
(122 = 121 + 1). This also satisfies the printed x = 5 (mod 3), since 5 = 2 (mod 3).

## Q.8 b) Solve 7x + 3y = 10 (mod 16), 2x + 5y = 9 (mod 16). [6]

Same system as Paper 1 Q.8 b). Eliminate x: multiply Eq1 by 2 and Eq2 by 7:

14x + 6y = 4 (mod 16)
14x + 35y = 15 (mod 16)

Subtract: 29y = 11 (mod 16), that is 13y = 11 (mod 16).
Inverse of 13 mod 16 is 5 (13 x 5 = 65 = 1 mod 16).
y = 55 = 7 (mod 16).

Then 7x = 10 - 21 = -11 = 5 (mod 16), and the inverse of 7 mod 16 is 7,
so x = 35 = 3 (mod 16).

**x = 3, y = 7 (mod 16)**

## Q.8 c) Show that 2^340 - 1 is divisible by 31 using Fermat's little theorem. [7]

Fermat's little theorem with p = 31 (prime) and a = 2 (31 does not divide 2):

2^30 = 1 (mod 31)

Raise both sides to the power 11:
(2^30)^11 = 2^330 = 1 (mod 31)

Now 340 = 330 + 10, so
2^340 = 2^330 x 2^10 = 1 x 1024 (mod 31)

1024 = 31 x 33 + 1, so 1024 = 1 (mod 31).

Therefore 2^340 = 1 (mod 31), that is:

**2^340 - 1 = 0 (mod 31), so 2^340 - 1 is divisible by 31.**

(Even shorter: 2^5 = 32 = 1 (mod 31), and 340 = 5 x 68, so
2^340 = (2^5)^68 = 1^68 = 1 (mod 31).)

---

# Paper 4: June/July 2024 (BMATS101)

## Q.7 a) Find the last digit of 7^2013. Find the last digit of 13^37. [6]

**(i) Last digit of 7^2013**

Powers of 7 end in 7, 9, 3, 1 and repeat (cycle 4).
2013 = 4 x 503 + 1, remainder 1, so take the first digit of the cycle.

**Last digit of 7^2013 = 7**

**(ii) Last digit of 13^37**

Powers of 13 end in 3, 9, 7, 1 and repeat (cycle 4).
37 = 4 x 9 + 1, remainder 1, so take the first digit of the cycle.

**Last digit of 13^37 = 3**

## Q.7 b) Find the remainder when 175 x 113 x 53 is divided by 11. Also find the remainder when 2^23 is divided by 47. [7]

**(i) 175 x 113 x 53 mod 11**

Same working as Paper 2 Q.8 c)(i):
175 = -1, 113 = 3, 53 = -2 (mod 11).
(-1) x 3 x (-2) = 6.

**Remainder = 6**

**(ii) 2^23 mod 47**

Same working as Paper 2 Q.8 a) (Fermat plus repeated squaring):

2^16 = 18, 2^4 = 16, 2^2 = 4, 2 = 2 (mod 47).
2^23 = 18 x 16 x 4 x 2 = 6 x 4 x 2 = 24 x 2 = 48 = 1 (mod 47).

**Remainder = 1**

## Q.7 c) Encrypt the message STOP using RSA with key (2537, 13) using the prime numbers 43 and 59. [7]

Same as Paper 2 Q.7 c):

n = 43 x 59 = 2537, phi = 42 x 58 = 2436, e = 13, d = 937.

S = 18 -> 2222, T = 19 -> 2299, O = 14 -> 1616, P = 15 -> 2116.

**Encrypted message: 2222 2299 1616 2116**

## Q.8 a) Solve 2x + 6y = 1 (mod 7), 4x + 3y = 2 (mod 7). [6]

Eliminate y. Multiply Eq2 by 2:

8x + 6y = 4 (mod 7). Reduce 8 mod 7: x + 6y = 4 (mod 7).

Subtract Eq1 (2x + 6y = 1) from this:
(x + 6y) - (2x + 6y) = 4 - 1
-x = 3 (mod 7), so x = -3 = 4 (mod 7).

**x = 4**

Substitute into Eq1: 2(4) + 6y = 1 (mod 7), so 8 + 6y = 1, that is
1 + 6y = 1 (mod 7) (since 8 = 1 mod 7).

6y = 0 (mod 7), so y = 0 (mod 7).

**y = 0**

**Solution: x = 4, y = 0 (mod 7)**

Check: 2(4) + 6(0) = 8 = 1 (mod 7) correct.
4(4) + 3(0) = 16 = 2 (mod 7) correct.

## Q.8 b) Using Fermat's little theorem, show that 8^30 - 1 is divisible by 31. [7]

Fermat's little theorem with p = 31 (prime) and a = 8 (31 does not divide 8):

8^30 = 1 (mod 31)

Therefore 8^30 - 1 = 0 (mod 31).

**So 8^30 - 1 is divisible by 31.**

(The same result comes from 8 = 2^3, so 8^30 = 2^90, and 2^5 = 32 = 1 (mod 31)
with 90 = 5 x 18.)

## Q.8 c) Show that 4(29)! + 5! is divisible by 31. [7]

Same as Paper 3 Q.7 c). By Wilson's theorem 30! = -1 (mod 31), and since
30! = 30 x 29! = -1 x 29!:

29! = 1 (mod 31), and 5! = 120 = 27 (mod 31).

4(29)! + 5! = 4 + 27 = 31 = 0 (mod 31).

**So 4(29)! + 5! is divisible by 31.**

---

# Paper 5: June/July 2024 Supplementary (BMATSCS101)

## Q.7 a) Find the remainder when 41^75 is divided by 3. Find the last digit in 7^289. [6]

**(i) 41^75 mod 3**

Reduce the base: 41 = 2 (mod 3) (41 = 39 + 2).

2^1 = 2 (mod 3), 2^2 = 4 = 1 (mod 3), so powers of 2 mod 3 alternate 2, 1, 2, 1, ...

75 is odd, so 2^75 = 2 (mod 3).

**Remainder = 2**

**(ii) Last digit of 7^289**

Powers of 7 end in 7, 9, 3, 1 (cycle 4). 289 = 4 x 72 + 1, remainder 1.

**Last digit = 7**

## Q.7 b) Find the solution of the linear congruence 18x = 30 (mod 42). [7]

a = 18, b = 30, n = 42.

d = gcd(18, 42) = 6. Since 6 divides 30, there are 6 solutions.

Divide everything by 6:
3x = 5 (mod 7).

Inverse of 3 mod 7: 3 x 5 = 15 = 1 (mod 7), so the inverse is 5.

x0 = 5 x 5 = 25 = 4 (mod 7).

The solutions are x0 + k x (42/6) = 4 + 7k for k = 0 to 5:
**x = 4, 11, 18, 25, 32, 39 (mod 42)**

Check: 18 x 4 = 72 = 72 - 42 = 30 (mod 42) correct.

## Q.7 c) Using the RSA algorithm find the public key and private key with respect to p = 3, q = 11 and m = 31. [7]

Step 1: n = p x q = 3 x 11 = 33.

Step 2: phi(n) = (p - 1)(q - 1) = 2 x 10 = 20.

Step 3: choose the encryption key e such that 1 < e < 20 and gcd(e, 20) = 1.
The question does not print e, so take e = 7 (7 is coprime to 20). Any e coprime
to 20 works the same way.

Public key = (n, e) = (33, 7).

Step 4: find the decryption key d from ed = 1 (mod 20):
7d = 1 (mod 20). Trying d = 3: 7 x 3 = 21 = 1 (mod 20). So d = 3.

Private key = d = 3 (the pair (33, 3) is kept secret).

Step 5: encrypt the message m = 31:
C = m^e (mod n) = 31^7 (mod 33).

31 = -2 (mod 33), so 31^7 = (-2)^7 = -128 (mod 33).
-128 = -128 + 4 x 33 = -128 + 132 = 4 (mod 33).

**C = 4**

Step 6: check decryption: C^d = 4^3 = 64 = 64 - 33 = 31 = m (mod 33). Correct.

**Public key (33, 7), private key d = 3, and the message 31 encrypts to 4.**

## Q.8 a) Show that 8^30 - 1 is divisible by 31 using Fermat's little theorem. [6]

Same as Paper 4 Q.8 b). Fermat: 8^30 = 1 (mod 31), so 8^30 - 1 = 0 (mod 31).

**8^30 - 1 is divisible by 31.**

## Q.8 b) Solve the system of linear congruences using CRT: x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7). [7]

Same as Paper 2 Q.8 b):

M = 105, M1 = 35, M2 = 21, M3 = 15, inverses y1 = 2, y2 = 1, y3 = 1.

X = 2 x 35 x 2 + 3 x 21 x 1 + 2 x 15 x 1 = 140 + 63 + 30 = 233 = 23 (mod 105).

**x = 23 (mod 105)**

## Q.8 c) Find the remainder when 349 x 74 x 36 is divided by 3. Also find the roots of x^2 + 2x - 3 = 0 (mod 5). [7]

**(i) 349 x 74 x 36 mod 3**

Reduce: 349 = 3 x 116 + 1, so 349 = 1 (mod 3).
74 = 3 x 24 + 2, so 74 = 2 (mod 3).
36 = 3 x 12, so 36 = 0 (mod 3).

Since one factor is 0 mod 3, the product is 0.

**Remainder = 0**

**(ii) Roots of x^2 + 2x - 3 = 0 (mod 5)**

Factor: x^2 + 2x - 3 = (x - 1)(x + 3).

So x = 1 (mod 5) or x = -3 = 2 (mod 5).

Check by testing: x = 1 gives 1 + 2 - 3 = 0 correct.
x = 2 gives 4 + 4 - 3 = 5 = 0 (mod 5) correct.

**Roots: x = 1, 2 (mod 5)**

---

# Paper 6: Dec 2024/Jan 2025 (BMATS101)

## Q.7 a) Find the remainder when (349 x 74 x 36) is divided by 3. [6]

Same as Paper 5 Q.8 c)(i): 349 = 1, 74 = 2, 36 = 0 (mod 3).

**Remainder = 0**

## Q.7 b) Solve the linear Diophantine equation 13x + 17y = 5. [7]

Step 1: gcd(13, 17) = 1, and 1 divides 5, so solutions exist.

Step 2: find one particular solution. Solve 13x = 5 (mod 17).

The inverse of 13 mod 17: 13 x 4 = 52 = 52 - 3 x 17 = 1 (mod 17), so the
inverse is 4.

x0 = 5 x 4 = 20 = 3 (mod 17). Take x = 3.

Then 13(3) + 17y = 5 gives 39 + 17y = 5, so 17y = -34 and y = -2.

Check: 13(3) + 17(-2) = 39 - 34 = 5 correct.

Step 3: general solution. For ax + by = c with solution (x0, y0), the general
solution is x = x0 + (b/d) t, y = y0 - (a/d) t with d = gcd(a, b) = 1:

**x = 3 + 17t, y = -2 - 13t, for any integer t.**

(Other particular solutions: (20, -15), (-14, 11), ... all from the same formula.)

## Q.7 c) Solve the system of linear congruences x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7) using the Remainder theorem. [7]

Same as Paper 2 Q.8 b): **x = 23 (mod 105)**

Working: M = 105, M1 = 35 (y1 = 2), M2 = 21 (y2 = 1), M3 = 15 (y3 = 1),
X = 140 + 63 + 30 = 233 = 23 (mod 105).

## Q.8 a) Find the last digit in 7^126. [6]

Powers of 7 end in 7, 9, 3, 1 (cycle 4).
126 = 4 x 31 + 2, remainder 2, so take the second digit of the cycle.

**Last digit of 7^126 = 9**

## Q.8 b) Solve 2x + 6y = 1 (mod 7), 4x + 3y = 2 (mod 7). [7]

Same as Paper 4 Q.8 a): subtract 2 x Eq2 - reduce to get x + 6y = 4, subtract Eq1
to get x = 4, then 6y = 0 so y = 0.

**x = 4, y = 0 (mod 7)**

## Q.8 c) Find the remainder when 7^121 is divided by 13. [7]

Fermat's little theorem with p = 13 and a = 7 (13 does not divide 7):

7^12 = 1 (mod 13)

121 = 12 x 10 + 1, so:
7^121 = (7^12)^10 x 7^1 = 1 x 7 = 7 (mod 13)

**Remainder = 7**

---

# Paper 7: June/July 2025 (BMATS101)

## Q.7 a) Find the least positive values of x such that (i) 71 = x (mod 8) (ii) 67 + x = 1 (mod 4) (iii) 89 = (7 + 3) (mod 5). [6]

**(i) 71 = x (mod 8)**

71 = 64 + 7, so 71 = 7 (mod 8). **x = 7**

**(ii) 67 + x = 1 (mod 4)**

67 = 64 + 3 = 3 (mod 4), so 3 + x = 1 (mod 4), x = -2 = 2 (mod 4). **x = 2**

**(iii) 89 = (7 + 3) (mod 5)**

The printed "(7 + 3)" is a misprint for "(x + 3)", which is how the same question
appears in the July 2023 paper. Solving 89 = (x + 3) (mod 5):

89 = 85 + 4 = 4 (mod 5), so x + 3 = 4 (mod 5), x = 1 (mod 5). **x = 1**

## Q.7 b) Find the solutions of the linear congruence 14x = 12 (mod 18). [7]

Same as Paper 2 Q.7 b): d = gcd(14, 18) = 2, divide to get 7x = 6 (mod 9),
inverse of 7 mod 9 is 4, x0 = 24 = 6 (mod 9).

**x = 6, 15 (mod 18)**

## Q.7 c) Encode STOP using the RSA algorithm with key (2537, 13) using the prime numbers 43 and 59. [7]

Same as Paper 2 Q.7 c):

n = 2537, phi = 2436, e = 13, d = 937.

**S = 18 -> 2222, T = 19 -> 2299, O = 14 -> 1616, P = 15 -> 2116**

## Q.8 a) Find the last digit of 7^2013. Find the last digit of 13^37. [7]

Same as Paper 4 Q.7 a):

**Last digit of 7^2013 = 7** (2013 = 4 x 503 + 1, first digit of cycle 7, 9, 3, 1)
**Last digit of 13^37 = 3** (37 = 4 x 9 + 1, first digit of cycle 3, 9, 7, 1)

## Q.8 b) Solve the system of linear congruences x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7) using the Remainder theorem. [7]

Same as Paper 2 Q.8 b): **x = 23 (mod 105)**

## Q.8 c) Show that 2^340 = 1 (mod 31) by Fermat's little theorem. [7]

Same as Paper 3 Q.8 c): 2^5 = 32 = 1 (mod 31) and 340 = 5 x 68, so
2^340 = (2^5)^68 = 1 (mod 31). Or by Fermat 2^30 = 1 (mod 31) with
340 = 30 x 11 + 10 and 2^10 = 1024 = 1 (mod 31).

**2^340 = 1 (mod 31)**

---

## How the questions repeat across papers (quick revision map)

- Last digit of 7^2013: Papers 4, 7. Answer 7.
- Last digit of 13^37: Papers 1, 4, 7. Answer 3.
- Last digit of 7^289: Papers 3, 5. Answer 7.
- Last digit of 7^126: Paper 6. Answer 9.
- Last digit of 7^118: Paper 1. Answer 9.
- 41^75 mod 3: Paper 5. Answer 2.
- 2^23 mod 47: Papers 2, 4. Answer 1.
- 2^340 - 1 divisible by 31: Papers 3, 7.
- 8^30 - 1 divisible by 31: Papers 4, 5.
- 4(29)! + 5! divisible by 31: Papers 3, 4.
- 14! mod 17: Paper 1. Answer 8.
- 7^121 mod 13: Paper 6. Answer 7.
- Products mod small numbers: 135x74x48 mod 7 = 6 (Paper 3); 175x113x53 mod 11 = 6
  (Papers 2, 4); 349x74x36 mod 3 = 0 (Papers 5, 6).
- Linear congruences: 12x = 6 (mod 21) -> 4, 11, 18 (Paper 1); 14x = 12 (mod 18) ->
  6, 15 (Papers 2, 7); 6x = 15 (mod 21) -> 6, 13, 20 (Paper 3); 18x = 30 (mod 42) ->
  4, 11, 18, 25, 32, 39 (Paper 5).
- Diophantine: 70x + 112y = 168 (Paper 1), 13x + 17y = 5 (Paper 6).
- Systems of two congruences: 7x + 3y = 10, 2x + 5y = 9 (mod 16) -> (3, 7)
  (Papers 1, 3); 2x + 6y = 1, 4x + 3y = 2 (mod 7) -> (4, 0) (Papers 4, 6).
- CRT: 2, 3, 2 with moduli 3, 5, 7 -> 23 (Papers 2, 5, 6, 7); 5, 2, 1 with moduli
  3, 5, 11 -> 122 (Paper 3); 3, 2, 4 with moduli 5, 6, 7 -> 158 (Paper 1).
- RSA STOP with (2537, 13): Papers 2, 4, 7. Cipher: 2222 2299 1616 2116.
- RSA p = 3, q = 11, m = 31: Paper 5. Public (33, 7), private d = 3, C = 4.
- Least positive x values: Papers 2, 7.
- x^2 + 2x - 3 = 0 (mod 5) -> 1, 2 (Paper 5); (mod 9) -> 1, 6 (Paper 2).
