# Assignment 1 - Answers

Subject: Mathematics for Computer Science (3rd sem, VTU) | 10 questions x 5 marks

The questions are from the college Assignment 1 sheet. Answers are written the
way the class notes solve each type, with every step shown. All numbers were
checked by computer before writing.

---

## Q.1 Find the unit digit of 7^289. [5]

The unit digits of powers of 7 repeat in a cycle:

| Power | 7^1 | 7^2 | 7^3 | 7^4 | 7^5 |
|---|---|---|---|---|---|
| Unit digit | 7 | 9 | 3 | 1 | 7 |

So the cycle is 7, 9, 3, 1 and its length is 4.

Step: divide the power by 4 and keep the remainder.
289 = 4 x 72 + 1, so the remainder is 1.

When the remainder is 1, the unit digit is the first digit of the cycle, 7.

**Unit digit of 7^289 = 7**

## Q.2 Find the last digit of 7^2013. [5]

Same cycle as above: the last digits of 7, 7^2, 7^3, 7^4 are 7, 9, 3, 1, and the
pattern repeats every 4 powers.

Step: 2013 = 4 x 503 + 1, remainder 1.

So the last digit is the first number of the cycle.

**Last digit of 7^2013 = 7**

## Q.3 Find the remainder when 64 x 65 x 66 is divided by 67. [5]

Method from the notes: reduce each factor mod 67 first.

67 = 1 (mod 67), so:
64 = 64 - 67 = -3 (mod 67)
65 = 65 - 67 = -2 (mod 67)
66 = 66 - 67 = -1 (mod 67)

Product:
64 x 65 x 66 = (-3)(-2)(-1) = -6 (mod 67)

-6 + 67 = 61, so:

**Remainder = 61**

(This also connects to Wilson's theorem: 67 is prime, so 66! = -1 (mod 67).)

## Q.4 What is a linear congruence? Explain with an example. [5]

**Definition:** A linear congruence is an equation of the form

a x = b (mod n)

where a, b and n are integers (n > 0). It asks: which integers x leave the same
remainder as b when both are divided by n?

**When does it have a solution?** Let d = gcd(a, n). The congruence
a x = b (mod n) has a solution if and only if d divides b. If it has a
solution, it has exactly d solutions mod n.

**How to solve it:**

1. Find d = gcd(a, n) and check d divides b.
2. Divide everything by d: a' x = b' (mod n').
3. Find the inverse of a' mod n' and get x0.
4. The d solutions are x0, x0 + n', x0 + 2n', ... up to n - n'.

**Example: solve 6x = 15 (mod 21)**

Step 1: d = gcd(6, 21) = 3, and 3 divides 15, so there are 3 solutions.

Step 2: divide everything by 3:
2x = 5 (mod 7).

Step 3: inverse of 2 mod 7 is 4, because 2 x 4 = 8 = 1 (mod 7).
x0 = 5 x 4 = 20 = 6 (mod 7).

Step 4: the solutions are x0 + 7k for k = 0, 1, 2:
x = 6, 13, 20 (mod 21).

Check: 6 x 6 = 36 = 36 - 21 = 15 (mod 21) correct.

**Answer: x = 6, 13, 20 (mod 21)**

## Q.5 Explain the method of fitting a straight line by least squares. Fit a
straight line y = ax + b for the data: x: -2, -1, 0, 1, 2 and y: 1, 2, 3, 3, 4. [5]

**Method (principle of least squares):** we choose a and b so that the sum of
squares of the errors (actual y minus fitted y) is minimum. For the straight
line y = ax + b this gives two equations, called the normal equations:

Sum(y) = n b + a Sum(x)
Sum(xy) = b Sum(x) + a Sum(x^2)

**Working:**

| x | y | xy | x^2 |
|---|---|---|---|
| -2 | 1 | -2 | 4 |
| -1 | 2 | -2 | 1 |
| 0 | 3 | 0 | 0 |
| 1 | 3 | 3 | 1 |
| 2 | 4 | 8 | 4 |
| **0** | **13** | **7** | **10** |

n = 5, Sum(x) = 0, Sum(y) = 13, Sum(xy) = 7, Sum(x^2) = 10.

Normal equations:
13 = 5b + 0a ... (1)
7 = 0b + 10a ... (2)

From (1): b = 13/5 = 2.6
From (2): a = 7/10 = 0.7

**y = 0.7x + 2.6**

## Q.6 Explain fitting a parabola y = a + bx + cx^2 by least squares. Fit a
parabola for x: 1, 2, 3, 4, 5 and y: 10, 12, 13, 16, 19. [5]

**Method:** minimize the sum of squared errors for y = a + bx + cx^2. This
gives three normal equations:

Sum(y) = n a + b Sum(x) + c Sum(x^2)
Sum(xy) = a Sum(x) + b Sum(x^2) + c Sum(x^3)
Sum(x^2 y) = a Sum(x^2) + b Sum(x^3) + c Sum(x^4)

**Working:**

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

Eliminate a. (2) - 3 x (1): 22 = 10b + 60c, so b + 6c = 2.2 ... (4)
(3) - 11 x (1): 136 = 60b + 374c ... (5)

From (4) b = 2.2 - 6c. Substitute in (5):
136 = 132 - 360c + 374c = 132 + 14c, so 14c = 4, c = 2/7 = 0.2857.
Then b = 2.2 - 6(0.2857) = 0.4857.
From (1): 5a = 70 - 15(0.4857) - 55(0.2857) = 47, so a = 9.4.

**y = 9.4 + 0.4857x + 0.2857x^2**

## Q.7 Explain fitting a power curve y = a x^b. Fit y = a x^b for the data
x: 2, 3, 4, 5 and y: 27.8, 62.1, 110, 161. [5]

**Method:** the power curve y = a x^b is made linear by taking logarithms of
both sides:

log y = log a + b log x

Put Y = log y, X = log x, A = log a. Then Y = A + bX is a straight line, and we
fit it by least squares using the normal equations:

Sum(Y) = nA + b Sum(X)
Sum(XY) = A Sum(X) + b Sum(X^2)

Finally a = e^A (or 10^A if base 10 logs were used).

**Working (natural logs):**

| x | y | X = log x | Y = log y | XY | X^2 |
|---|---|---|---|---|---|
| 2 | 27.8 | 0.6931 | 3.3250 | 2.3047 | 0.4805 |
| 3 | 62.1 | 1.0986 | 4.1287 | 4.5359 | 1.2069 |
| 4 | 110 | 1.3863 | 4.7005 | 6.5162 | 1.9218 |
| 5 | 161 | 1.6094 | 5.0814 | 8.1782 | 2.5903 |
| | | **4.7875** | **17.2357** | **21.5351** | **6.1995** |

n = 4.

Normal equations:
17.2357 = 4A + 4.7875b ... (1)
21.5351 = 4.7875A + 6.1995b ... (2)

From (1): A = 4.3089 - 1.1969b. Substitute in (2):

21.5351 = 4.7875(4.3089 - 1.1969b) + 6.1995b = 20.6273 + 0.4696b
0.9078 = 0.4696b
b = 1.9302

A = 4.3089 - 1.1969(1.9302) = 1.9988

a = e^1.9988 = 7.3799

**y = 7.3799 x^1.9302**

(NOTE: if you use base 10 logarithms the b comes out the same 1.9302 and
a = 10^0.8675 = 7.37. Both log bases give the same curve.)

## Q.8 Explain correlation and regression. For the following data on fathers
(x) and sons (y), compute the correlation coefficient and the two regression
lines. [5]

x (fathers): 65, 66, 67, 67, 68, 69, 70, 72
y (sons): 67, 68, 65, 68, 72, 72, 69, 71

**Correlation:** correlation measures how strongly two variables move together,
from -1 to +1. Karl Pearson's formula:

r = Sum(x - xbar)(y - ybar) / sqrt[Sum(x - xbar)^2 Sum(y - ybar)^2]
= Sxy / sqrt(Sxx x Syy)

**Regression:** a regression line predicts one variable from the other.
- Regression line of y on x: y = a + bxy x, where bxy = Sxy / Sxx
- Regression line of x on y: x = a' + byx y, where byx = Sxy / Syy

Also r^2 = bxy x byx, and both regression coefficients have the same sign as r.

**Working:**

n = 8. Sums: Sum(x) = 544, so xbar = 68. Sum(y) = 552, so ybar = 69.

| x | y | x^2 | y^2 | xy |
|---|---|---|---|---|
| 65 | 67 | 4225 | 4489 | 4355 |
| 66 | 68 | 4356 | 4624 | 4488 |
| 67 | 65 | 4489 | 4225 | 4355 |
| 67 | 68 | 4489 | 4624 | 4556 |
| 68 | 72 | 4624 | 5184 | 4896 |
| 69 | 72 | 4761 | 5184 | 4968 |
| 70 | 69 | 4900 | 4761 | 4830 |
| 72 | 71 | 5184 | 5041 | 5112 |
| **544** | **552** | **37028** | **38132** | **37560** |

Sxx = 37028 - (544)^2/8 = 37028 - 36992 = 36
Syy = 38132 - (552)^2/8 = 38132 - 38088 = 44
Sxy = 37560 - (544)(552)/8 = 37560 - 37536 = 24

**Correlation:**

r = 24 / sqrt(36 x 44) = 24 / sqrt(1584) = 24 / 39.799 = 0.603

**r = 0.603** (moderate positive correlation: taller fathers tend to have
taller sons)

**Regression line of y on x:**

byx (slope of y on x) = Sxy / Sxx = 24/36 = 2/3 = 0.6667

y - ybar = byx (x - xbar)
y - 69 = 0.6667(x - 68)
y = 0.6667x + 69 - 45.3333 = 0.6667x + 23.6667

**y on x: y = 0.6667x + 23.67**

**Regression line of x on y:**

bxy (slope of x on y) = Sxy / Syy = 24/44 = 6/11 = 0.5455

x - xbar = bxy (y - ybar)
x - 68 = 0.5455(y - 69)
x = 0.5455y + 68 - 37.6364 = 0.5455y + 30.3636

**x on y: x = 0.5455y + 30.36**

Check: bxy x byx = 0.6667 x 0.5455 = 0.3636 = r^2 = (0.603)^2. Correct.

## Q.9 Derive the mean and variance of the Binomial distribution. [5]

For n independent trials with success probability p (q = 1 - p), the number of
successes X has

P(X = r) = nCr p^r q^(n-r), r = 0, 1, ..., n

**Mean:**

E(X) = Sum over r of r nCr p^r q^(n-r)

The r = 0 term is zero, so sum from r = 1. Use r x nCr = n x (n-1)C(r-1):

E(X) = Sum r=1..n of n (n-1)C(r-1) p^r q^(n-r)
     = n p x Sum r=1..n of (n-1)C(r-1) p^(r-1) q^(n-r)

Put s = r - 1:

E(X) = n p x Sum s=0..n-1 of (n-1)Cs p^s q^(n-1-s)
     = n p (p + q)^(n-1)
     = n p (1)^(n-1)

**E(X) = n p**

**Variance:**

E(X^2) = Sum [r(r-1) + r] nCr p^r q^(n-r)
       = Sum r(r-1) nCr p^r q^(n-r) + E(X)

For the first part use r(r-1) nCr = n(n-1) (n-2)C(r-2):

Sum r(r-1) nCr p^r q^(n-r)
= n(n-1) p^2 Sum t=0..n-2 of (n-2)Ct p^t q^(n-2-t)
= n(n-1) p^2 (p + q)^(n-2)
= n(n-1) p^2

So E(X^2) = n(n-1) p^2 + n p.

Var(X) = E(X^2) - [E(X)]^2
       = n(n-1) p^2 + n p - n^2 p^2
       = n p q

**Mean = n p and Variance = n p q**

## Q.10 Derive the mean and variance of the Poisson distribution. [5]

The Poisson distribution gives the probability of r events in a fixed interval,
when events happen independently at a constant average rate m:

P(X = r) = e^(-m) m^r / r!, r = 0, 1, 2, ...

(So the mean of a Poisson distribution equals its parameter m, and the variance
is also m.)

**Mean:**

E(X) = Sum r=0..infinity of r x e^(-m) m^r / r!

The r = 0 term is zero, so start at r = 1:

E(X) = Sum r=1..infinity of r e^(-m) m^r / r!

Use r / r! = 1 / (r - 1)!:

E(X) = e^(-m) Sum r=1..infinity of m^r / (r-1)!
     = e^(-m) x m Sum s=0..infinity of m^s / s!      (put s = r - 1)

The sum Sum m^s / s! = e^m. So:

E(X) = e^(-m) x m x e^m = m

**E(X) = m**

**Variance:**

E(X^2) = Sum r(r-1) e^(-m) m^r / r! + Sum r e^(-m) m^r / r!
       = Sum r(r-1) e^(-m) m^r / r! + m

For the first sum, use r(r-1)/r! = 1/(r-2)! and start at r = 2:

Sum r=2..infinity of e^(-m) m^r / (r-2)!
= e^(-m) x m^2 Sum t=0..infinity of m^t / t!      (put t = r - 2)
= e^(-m) x m^2 x e^m = m^2

So E(X^2) = m^2 + m.

Var(X) = E(X^2) - [E(X)]^2 = m^2 + m - m^2 = m

**Mean = m and Variance = m**

So for the Poisson distribution, mean = variance = m. This is the special
property of the Poisson distribution.
