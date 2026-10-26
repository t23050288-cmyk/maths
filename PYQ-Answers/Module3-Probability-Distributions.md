# Module 3: Probability Distributions

## Table of Contents
- [Paper Dec 2023 / Jan 2024 (P1)](#paper-dec-2023--jan-2024-p1)
  - [Q.1 a) [6m] Discrete Probability Table (0..7)](#q1-a-6m-a-random-variable-x-has-the-following-probability-function-for-variable-values-of-x)
  - [Q.1 b) [7m] Mean and Variance of Binomial Distribution](#q1-b-7m-find-the-mean-and-variance-of-binomial-distribution)
  - [Q.1 c) [7m] Duration of Shower (Exponential Distribution)](#q1-c-7m-in-a-certain-town-the-duration-of-a-shower-is-exponentially-distributed-with-mean-5-minutes-what-is-the-probability-that-a-shower-will-last-for-i-10-minutes-or-more-ii-less-than-10-minutes-iii-between-10-and-12-minutes)
  - [Q.2 a) [6m] Continuous pdf f(x) = K x^2 on [-3, 3]](#q2-a-6m-a-random-variable-x-has-the-following-density-function-px--k-x2-for--3--x--3-0-elsewhere-find-the-value-of-k-evaluate-i-p1--x--2-ii-px--2)
  - [Q.2 b) [7m] Factory Defective Blades (Poisson Distribution)](#q2-b-7m-in-a-factory-producing-blades-the-probability-of-any-blade-being-defective-is-0002-if-blades-are-supplied-in-packets-of-10-using-poisson-distribution-determine-the-number-of-packets-containing-i-no-defective-ii-one-defective-iii-two-defective-blades-respectively-in-a-consignment-of-10000-packets)
  - [Q.2 c) [7m] Electric Bulbs Lifetime (Normal Distribution)](#q2-c-7m-in-a-test-on-electric-bulbs-it-was-found-that-the-life-time-of-a-particular-brand-was-distributed-normally-with-an-average-life-of-2000-hours-and-standard-deviation-of-60-hours-if-a-firm-purchases-2500-bulbs-find-the-number-of-bulbs-that-are-likely-to-last-for-i-more-than-2100-hours-ii-between-1900-to-2100-hours-iii-less-than-1950-hours-given-phi167--04525-phi083--02967)
- [Paper Jun / Jul 2024 (P2)](#paper-jun--jul-2024-p2)
  - [Q.1 a) [6m] Mean and Variance of Poisson Distribution](#q1-a-6m-obtain-the-mean-and-variance-of-poisson-distribution)
  - [Q.1 b) [7m] Families with 4 Children (Binomial Distribution)](#q1-b-7m-out-of-800-families-with-4-children-each-how-many-families-would-be-expected-to-have-i-2-boys-and-2-girls-ii-atleast-one-boy-iii-at-most-2-girls-assume-equal-probabilities-for-boys-and-girls)
  - [Q.1 c) [7m] Telephone Conversation Length (Exponential Distribution)](#q1-c-7m-the-length-of-telephone-conversation-in-a-booth-has-been-an-exponential-distribution-and-found-on-an-average-to-be-5-minutes-find-the-probability-that-a-random-call-made-from-this-booth-i-ends-less-than-5-minutes-ii-between-5-and-10-minutes)
  - [Q.2 a) [6m] Finite Discrete RV (-2 to 3)](#q2-a-6m-the-probability-distribution-of-a-finite-random-variable-x-is-given-by--x--2--1-0-1-2-3--px-01-k-02-2k-03-k--i-find-the-value-of-k-ii-variance-iii-px--2)
  - [Q.2 b) [7m] Taxi Driver Accidents (Poisson Distribution)](#q2-b-7m-the-number-of-accidents-in-a-year-to-taxi-drivers-in-a-city-follows-a-poisson-distribution-with-mean-3-out-of-1000-taxi-drivers-find-approximately-number-of-drivers-with-i-more-than-3-accidents-in-a-year-ii-at-most-2-accidents-in-a-year)
  - [Q.2 c) [7m] Student Marks (Normal Distribution)](#q2-c-7m-the-marks-of-1000-students-in-an-exam-follows-normal-distribution-with-mean-70-and-standard-deviation-5-find-the-students-whose-marks-will-be-i-less-than-65-ii-between-65-and-75-a1--03413)
- [Paper Dec 2024 / Jan 2025 (P3)](#paper-dec-2024--jan-2025-p3)
  - [Q.1 a) [7m] Discrete Probability Table (0..7)](#q1-a-7m-a-random-variable-x-has-the-following-prob-density-function-for-various-values-of-x--x-07--px-0-k-2k-2k-3k-k2-2k2-7k2k--find-the-value-of-k-and-evaluate-px--6-p3--x--6-and-x--6)
  - [Q.1 b) [6m] Mean and Variance of Poisson Distribution](#q1-b-6m-derive-the-mean-and-variance-of-poisson-distribution)
  - [Q.1 c) [7m] Duration of Shower (Exponential Distribution)](#q1-c-7m-in-a-certain-town-the-duration-of-a-shower-is-exponentially-distributed-with-mean-5-minutes-what-is-the-probability-that-a-shower-will-last-for-i-less-than-10-minutes-ii-more-than-10-minutes-and-iii-between-10-and-12-minutes)
  - [Q.2 a) [7m] Continuous pdf f(x) = K x^2 on (-3, 3)](#q2-a-7m-the-probability-density-function-of-fx--k-x2-for--3--x--3-0-elsewhere-find-the-value-of-k-and-evaluate-i-px--2-px--1-ii-p1--x--2)
  - [Q.2 b) [6m] Coin Tossed 4 Times](#q2-b-6m-when-a-coin-is-tossed-4-times-find-the-probability-of-getting-i-exactly-one-head-ii-atleast-three-heads-and-iii-less-than-two-heads)
  - [Q.2 c) [7m] Student Marks (Normal Distribution)](#q2-c-7m-the-marks-of-1000-students-in-an-examination-follows-a-normal-distribution-with-mean-70-and-sd-5-find-the-number-of-students-whose-marks-will-be-i-less-than-65-ii-more-than-75-and-iii-between-65-and-75)
- [Paper Jun / Jul 2025 (P4)](#paper-jun--jul-2025-p4)
  - [Q.1 a) [6m] Discrete Table (0..6, K to 13K)](#q1-a-6m-the-probability-density-function-of-a-variate-x-is-given-by-the-following-table-x-0-1-2-3-4-5-6--px-k-3k-5k-7k-9k-11k-13k--i-for-what-value-of-k-does-this-represent-a-valid-probability-distribution-ii-find-px4-iii-find-p3x6)
  - [Q.1 b) [7m] Defective Fuses (Poisson Distribution)](#q1-b-7m-2-fuses-manufactured-by-a-firm-are-found-to-be-defective-find-the-probability-that-the-box-containing-200-fuses-contains-i-no-defective-fuses-ii-3-or-more-defective-fuses-iii-atleast-one-defective-fuse)
  - [Q.1 c) [7m] Lady Speaking on Phone (Exponential Distribution)](#q1-c-7m-the-length-in-time-minutes-that-a-certain-lady-speaks-on-a-telephone-is-a-random-variable-with-probability-density-function-fx--a-e-x5-for-x--0-0-elsewhere-find-the-value-of-the-constant-a-what-is-the-probability-that-she-will-speak-over-the-phone-for-i-more-than-10-minutes-ii-less-than-5-minutes-iii-between-5-and-10-minutes)
  - [Q.2 a) [6m] Continuous pdf f(x) = K x^2 on (0, 3)](#q2-a-6m-find-the-constant-k-such-that-the-function-fx--k-x2-for-0--x--3-0-otherwise-is-a-probability-density-function-also-compute-p1--x--2-px--1)
  - [Q.2 b) [7m] Mean and Variance of Binomial Distribution](#q2-b-7m-obtain-the-mean-and-variance-of-binomial-distribution)
  - [Q.2 c) [7m] Student Marks (Normal Distribution)](#q2-c-7m-the-marks-of-1000-students-in-an-examination-follows-a-normal-distribution-with-mean-70-and-standard-deviation-5-find-the-number-of-students-whose-marks-will-be-i-less-than-65-ii-more-than-75-iii-between-65-and-75-given-a1--03413-where-az-is-the-area-under-standard-normal-curve-from-0-to-z)
- [Paper Jun / Jul 2025 Makeup (P5)](#paper-jun--jul-2025-makeup-p5)
  - [Q.1 a) [6m] Mean and Variance of Poisson Distribution](#q1-a-6m-derive-mean-and-variance-of-poisson-distribution)
  - [Q.1 b) [7m] Manufactured Pens (Binomial Distribution)](#q1-b-7m-the-probability-that-a-pen-manufactured-by-a-factory-be-defective-is-110-if-12-such-pens-are-manufactured-what-is-the-probability-that--i-exactly-two-are-defective-ii-atleast-two-are-defective-iii-none-of-them-are-defective)
  - [Q.1 c) [7m] Student Marks (Normal Distribution)](#q1-c-7m-the-marks-of-1000-students-in-an-examination-follows-a-normal-distribution-with-mean-70-and-standard-deviation-5-find-the-number-of-students-whose-marks-will-be-i-less-than-65-ii-more-than-75-iii-between-65-and-75-given-phi1--03413)
  - [Q.2 a) [6m] Discrete Table (0..6, k to 13k)](#q2-a-6m-the-pdf-of-a-variate-x-is-given-by-the-following-table-x-06--px-k-3k-5k-7k-9k-11k-13k-for-what-value-of-k-this-represents-a-valid-probability-distribution-also-find-px--5-and-p3--x--6)
  - [Q.2 b) [7m] Taxi Driver Accidents (Poisson Distribution)](#q2-b-7m-the-number-of-accidents-in-a-year-to-taxi-drivers-in-a-city-follows-a-poisson-distribution-with-mean-3-out-of-1000-taxi-drivers-find-approximately-the-number-of-the-drivers-with-i-no-accident-in-a-year-ii-more-than-3-accidents-in-a-year)
  - [Q.2 c) [7m] Normal Variate (Mean 30, SD 5)](#q2-c-7m-if-x-is-a-normal-variate-with-mean-30-and-standard-deviation-5-find-the-probability-that-i-26--x--40-ii-x--45)
- [Paper Dec 2025 / Jan 2026 (P6)](#paper-dec-2025--jan-2026-p6)
  - [Q.1 a) [6m] Discrete Probability Table (0..7)](#q1-a-6m-a-random-variable-x-has-the-following-probability-function-for-various-values-of-x--x-07--px-0-k-2k-2k-3k-k2-2k2-7k2k--i-find-the-value-of-k-ii-evaluate-px--6-p0--x--5-px--6)
  - [Q.1 b) [7m] Mean and Standard Deviation of Binomial Distribution](#q1-b-7m-find-the-mean-and-standard-deviation-of-binomial-distribution)
  - [Q.1 c) [7m] Bad Injection Reaction (Poisson Distribution)](#q1-c-7m-if-the-probability-of-a-bad-reaction-from-a-certain-injection-is-0001-determine-the-probability-that-out-of-2000-individuals-more-than-two-will-get-a-bad-reaction)
  - [Q.2 a) [6m] Continuous pdf f(x) = k e^-x on (0, 1)](#q2-a-6m-find-k-such-that-fx--k-e-x-for-0--x--1-0-otherwise-represents-a-valid-pdf-and-hence-find-mean-of-the-distribution)
  - [Q.2 b) [7m] Duration of Shower (Exponential Distribution)](#q2-b-7m-in-a-certain-town-the-duration-of-a-shower-is-exponentially-distributed-with-mean-5-minutes-what-is-the-probability-that-a-shower-will-last-for-i-10-minutes-or-more-ii-less-than-10-minutes)
  - [Q.2 c) [7m] Student Marks (Normal Distribution)](#q2-c-7m-the-marks-of-1000-students-in-an-examination-follows-a-normal-distribution-with-mu--70-and-sd--5-find-the-number-of-students-whose-marks-will-be-i-less-than-65-ii-more-than-75-iii-between-65--75-given-phi1--03413)
- [Paper Model Question Paper-I (P7)](#paper-model-question-paper-i-p7)
  - [Q.1 a) [6m] Discrete Probability Table (0..6, k to 13k)](#q1-a-6m-the-probability-distribution-function-of-variate-x-is-given-by-the-following-table-x-06--px-k-3k-5k-7k-9k-11k-13k-i-find-the-value-of-k-ii-px--5--iii-p3--x--6)
  - [Q.1 b) [7m] Bad Injection Reaction (Poisson Distribution)](#q1-b-7m-if-the-probability-of-a-bad-reaction-from-a-certain-injection-is-0001-determine-the-chance-that-more-than-two-of-2000-individuals-will-have-a-bad-reaction)
  - [Q.1 c) [7m] Mean and Standard Deviation of Poisson Distribution](#q1-c-7m-find-the-mean-and-standard-deviation-of-poissons-distribution)
  - [Q.2 a) [6m] Manufactured Pens (Binomial Distribution)](#q2-a-6m-the-probability-of-a-pen-manufactured-by-a-factory-be-defective-is-110-if-12-such-pens-are-manufactured-what-is-the-probability-that-i-exactly-2-are-defective-ii-at-least-2-are-defective-iii-none-of-them-are-defective)
  - [Q.2 b) [7m] Discrete Function f(x) = k(x^2 + 4)](#q2-b-7m-determine-the-value-of-k-so-that-the-function-fx--kx2--4-for-x--0-1-2-3-can-serve-as-a-probability-distribution-of-the-discrete-random-variable-x-also-find-i-p0--x--2-and-ii-px--1)
  - [Q.2 c) [7m] Mean and Standard Deviation of Binomial Distribution](#q2-c-7m-find-the-mean-and-standard-deviation-of-binomial-distribution)

---

### Paper Dec 2023 / Jan 2024 (P1)

## Q.1 a) [6m] A Random variable X has the following probability function for variable values of x.
x: 0 1 2 3 4 5 6 7 ; P(x): 0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2+k
(i) Find the value of k. (ii) Evaluate P(x >= 6) and P(3 < x <= 6).

**Given:**
Probability distribution table of discrete random variable X:
```
x   : 0   1   2   3   4   5     6      7
P(x): 0   k   2k  2k  3k  k^2   2k^2   7k^2+k
```

**Formula / Method:**
1. Sum of all probabilities for a valid discrete probability distribution is 1, i.e., sum(P(x)) = 1.
2. P(A) is obtained by summing P(x) for all x in A.

**Solution:**
Step 1: Find the value of k.
sum(P(x)) = 0 + k + 2k + 2k + 3k + k^2 + 2k^2 + (7k^2 + k) = 1
=> 10k^2 + 9k = 1
=> 10k^2 + 9k - 1 = 0
=> (10k - 1)(k + 1) = 0
=> k = 1/10 or k = -1.
Since probability P(x) >= 0 for all x, k cannot be negative.
Therefore, k = 1/10 = 0.1.

Step 2: Evaluate P(x >= 6).
P(x >= 6) = P(6) + P(7)
P(x >= 6) = 2k^2 + (7k^2 + k) = 9k^2 + k
Substitute k = 1/10:
P(x >= 6) = 9(1/10)^2 + (1/10) = 9/100 + 10/100 = 19/100 = 0.19.

Step 3: Evaluate P(3 < x <= 6).
The values of x satisfying 3 < x <= 6 are x = 4, 5, 6.
P(3 < x <= 6) = P(4) + P(5) + P(6)
P(3 < x <= 6) = 3k + k^2 + 2k^2 = 3k^2 + 3k
Substitute k = 1/10:
P(3 < x <= 6) = 3(1/10)^2 + 3(1/10) = 3/100 + 30/100 = 33/100 = 0.33.

**Answer:**
**(i) k = 1/10 = 0.1, (ii) P(x >= 6) = 19/100 = 0.19, P(3 < x <= 6) = 33/100 = 0.33**

**Check:**
For k = 0.1, sum(P(x)) = 0 + 0.1 + 0.2 + 0.2 + 0.3 + 0.01 + 0.02 + 0.17 = 1.0.


## Q.1 b) [7m] Find the mean and variance of Binomial distribution.

**Given:**
Binomial probability mass function: P(X = r) = nCr * p^r * q^(n-r), for r = 0, 1, 2, ..., n, where q = 1 - p.

**Formula / Method:**
1. Mean E(X) = sum(r * P(r)) for r = 0 to n.
2. Variance Var(X) = E(X^2) - [E(X)]^2, where E(X^2) = E[X(X-1)] + E(X).

**Solution:**
Step 1: Derivation of Mean E(X).
E(X) = sum_{r=0}^n r * nCr * p^r * q^(n-r)
The term for r = 0 is zero, so:
E(X) = sum_{r=1}^n r * [n! / (r! * (n-r)!)] * p^r * q^(n-r)
Using r / r! = 1 / (r-1)!:
E(X) = sum_{r=1}^n [n! / ((r-1)! * (n-r)!)] * p^r * q^(n-r)
Factor out n and p:
E(X) = n * p * sum_{r=1}^n [(n-1)! / ((r-1)! * ((n-1)-(r-1))!)] * p^(r-1) * q^((n-1)-(r-1))
Let j = r - 1. As r goes from 1 to n, j goes from 0 to n-1:
E(X) = n * p * sum_{j=0}^{n-1} (n-1)Cj * p^j * q^((n-1)-j)
By Binomial theorem, sum_{j=0}^{n-1} (n-1)Cj * p^j * q^((n-1)-j) = (q + p)^(n-1) = 1^(n-1) = 1.
Therefore, Mean E(X) = n * p.

Step 2: Derivation of E[X(X-1)].
E[X(X-1)] = sum_{r=0}^n r(r-1) * nCr * p^r * q^(n-r)
Terms for r = 0 and r = 1 are zero, so:
E[X(X-1)] = sum_{r=2}^n r(r-1) * [n! / (r! * (n-r)!)] * p^r * q^(n-r)
Using r(r-1) / r! = 1 / (r-2)!:
E[X(X-1)] = sum_{r=2}^n [n! / ((r-2)! * (n-r)!)] * p^r * q^(n-r)
Factor out n(n-1) and p^2:
E[X(X-1)] = n(n-1) * p^2 * sum_{r=2}^n [(n-2)! / ((r-2)! * ((n-2)-(r-2))!)] * p^(r-2) * q^((n-2)-(r-2))
Let j = r - 2. As r goes from 2 to n, j goes from 0 to n-2:
E[X(X-1)] = n(n-1) * p^2 * sum_{j=0}^{n-2} (n-2)Cj * p^j * q^((n-2)-j) = n(n-1) * p^2 * (q + p)^(n-2) = n(n-1) * p^2.

Step 3: Derivation of E(X^2) and Variance.
E(X^2) = E[X(X-1)] + E(X) = n(n-1)p^2 + np = n^2 p^2 - n p^2 + np.
Var(X) = E(X^2) - [E(X)]^2
Var(X) = (n^2 p^2 - n p^2 + np) - (np)^2
Var(X) = n^2 p^2 - n p^2 + np - n^2 p^2 = np - np^2 = np(1-p) = npq.

**Answer:**
**Mean = np, Variance = npq**

**Check:**
For n = 1 (Bernoulli distribution), Mean = p, Variance = p(1-p) = pq. Matches formula.


## Q.1 c) [7m] In a certain town the duration of a shower is exponentially distributed with mean 5 minutes. What is the probability that a shower will last for, (i) 10 minutes or more. (ii) Less than 10 minutes. (iii) Between 10 and 12 minutes.

**Given:**
Mean duration = 5 minutes.
Exponential parameter lambda = 1 / mean = 1/5 = 0.2.
Probability density function: f(x) = (1/5) * e^(-x/5) for x >= 0.

**Formula / Method:**
P(a <= X <= b) = integral_a^b (1/5) * e^(-x/5) dx = [-e^(-x/5)]_a^b = e^(-a/5) - e^(-b/5).

**Solution:**
Step 1: (i) Probability shower lasts 10 minutes or more, P(X >= 10).
P(X >= 10) = integral_10^infty (1/5) * e^(-x/5) dx
P(X >= 10) = [-e^(-x/5)]_10^infty = 0 - (-e^(-10/5)) = e^(-2)
Since e^(-2) = 0.135335..., P(X >= 10) = 0.1353.

Step 2: (ii) Probability shower lasts less than 10 minutes, P(X < 10).
P(X < 10) = integral_0^10 (1/5) * e^(-x/5) dx
P(X < 10) = [-e^(-x/5)]_0^10 = -e^(-10/5) - (-e^0) = 1 - e^(-2)
P(X < 10) = 1 - 0.135335... = 0.864665... = 0.8647.

Step 3: (iii) Probability shower lasts between 10 and 12 minutes, P(10 <= X <= 12).
P(10 <= X <= 12) = integral_10^12 (1/5) * e^(-x/5) dx
P(10 <= X <= 12) = [-e^(-x/5)]_10^12 = -e^(-12/5) - (-e^(-10/5)) = e^(-2) - e^(-2.4)
Since e^(-2) = 0.135335... and e^(-2.4) = 0.090718...:
P(10 <= X <= 12) = 0.135335 - 0.090718 = 0.044617... = 0.0446.

**Answer:**
**(i) P(X >= 10) = e^-2 = 0.1353, (ii) P(X < 10) = 1 - e^-2 = 0.8647, (iii) P(10 <= X <= 12) = e^-2 - e^-2.4 = 0.0446**

**Check:**
P(X < 10) + P(X >= 10) = 0.8647 + 0.1353 = 1.0000.


## Q.2 a) [6m] A random variable x has the following density function P(x) = K x^2 for -3 <= x <= 3, 0 elsewhere. Find the value of K. Evaluate (i) P(1 <= x <= 2) (ii) P(x <= 2).

**Given:**
Continuous pdf f(x) = K * x^2 for -3 <= x <= 3, 0 elsewhere.

**Formula / Method:**
1. integral_{-3}^3 f(x) dx = 1 to find K.
2. P(a <= x <= b) = integral_a^b f(x) dx.

**Solution:**
Step 1: Find K.
integral_{-3}^3 K * x^2 dx = 1
=> K * [x^3 / 3]_{-3}^3 = 1
=> K * [ (3^3 / 3) - ((-3)^3 / 3) ] = 1
=> K * [ (27/3) - (-27/3) ] = 1
=> K * [ 9 - (-9) ] = 18 K = 1
=> K = 1/18.

Step 2: Evaluate (i) P(1 <= x <= 2).
P(1 <= x <= 2) = integral_1^2 (1/18) * x^2 dx
P(1 <= x <= 2) = (1/18) * [x^3 / 3]_1^2 = (1/18) * [ (2^3 / 3) - (1^3 / 3) ]
P(1 <= x <= 2) = (1/18) * [ (8/3) - (1/3) ] = (1/18) * (7/3) = 7/54 = 0.1296.

Step 3: Evaluate (ii) P(x <= 2).
P(x <= 2) = integral_{-3}^2 (1/18) * x^2 dx
P(x <= 2) = (1/18) * [x^3 / 3]_{-3}^2 = (1/18) * [ (2^3 / 3) - ((-3)^3 / 3) ]
P(x <= 2) = (1/18) * [ (8/3) - (-27/3) ] = (1/18) * (35/3) = 35/54 = 0.6481.

**Answer:**
**K = 1/18, (i) P(1 <= x <= 2) = 7/54 = 0.1296, (ii) P(x <= 2) = 35/54 = 0.6481**

**Check:**
P(x <= 2) = integral_{-3}^2 f(x) dx = 1 - integral_2^3 (1/18) x^2 dx = 1 - (19/54) = 35/54.


## Q.2 b) [7m] In a factory producing blades, the probability of any blade being defective is 0.002. If blades are supplied in packets of 10, using Poisson distribution determine the number of packets containing, (i) No defective. (ii) One defective (iii) Two defective blades respectively in a consignment of 10,000 packets.

**Given:**
Probability of defective blade p = 0.002.
Packet size n = 10.
Total packets N = 10000.

**Formula / Method:**
Poisson parameter lambda = n * p = 10 * 0.002 = 0.02.
Poisson probability P(r) = e^(-lambda) * lambda^r / r!
Expected packets = N * P(r).

**Solution:**
Step 1: Compute lambda and e^(-lambda).
lambda = n * p = 10 * 0.002 = 0.02.
e^(-lambda) = e^(-0.02) = 0.98019867...

Step 2: (i) Packets with No defective blades (r = 0).
P(0) = e^(-0.02) = 0.98019867...
Number of packets = 10000 * 0.98019867... = 9801.98... = 9802 packets.

Step 3: (ii) Packets with One defective blade (r = 1).
P(1) = e^(-0.02) * (0.02)^1 / 1! = 0.98019867 * 0.02 = 0.01960397...
Number of packets = 10000 * 0.01960397... = 196.04... = 196 packets.

Step 4: (iii) Packets with Two defective blades (r = 2).
P(2) = e^(-0.02) * (0.02)^2 / 2! = 0.98019867 * 0.0004 / 2 = 0.00019604...
Number of packets = 10000 * 0.00019604... = 1.96... = 2 packets.

**Answer:**
**(i) 9802 packets, (ii) 196 packets, (iii) 2 packets**

**Check:**
9802 + 196 + 2 = 10000 packets.


## Q.2 c) [7m] In a test on electric bulbs, it was found that the life time of a particular brand was distributed normally with an average life of 2000 hours and standard deviation of 60 hours. If a firm purchases 2500 bulbs find the number of bulbs that are likely to last for, (i) More than 2100 hours. (ii) Between 1900 to 2100 hours. (iii) Less than 1950 hours. (Given phi(1.67) = 0.4525, phi(0.83) = 0.2967)

**Given:**
Mean mu = 2000 hours, Standard deviation sigma = 60 hours.
Total bulbs N = 2500.
Given normal area values: phi(1.67) = 0.4525, phi(0.83) = 0.2967.

**Formula / Method:**
Standard normal variate z = (x - mu) / sigma.
Expected number of bulbs = N * P.

**Solution:**
Step 1: (i) More than 2100 hours, P(x > 2100).
z = (2100 - 2000) / 60 = 100 / 60 = 1.67.
P(x > 2100) = P(z > 1.67) = 0.5 - phi(1.67) = 0.5 - 0.4525 = 0.0475.
Number of bulbs = 2500 * 0.0475 = 118.75 = 119 bulbs.

Step 2: (ii) Between 1900 to 2100 hours, P(1900 < x < 2100).
For x1 = 1900: z1 = (1900 - 2000) / 60 = -1.67.
For x2 = 2100: z2 = (2100 - 2000) / 60 = 1.67.
P(-1.67 < z < 1.67) = 2 * phi(1.67) = 2 * 0.4525 = 0.9050.
Number of bulbs = 2500 * 0.9050 = 2262.5 = 2263 bulbs (or 2262.5).

Step 3: (iii) Less than 1950 hours, P(x < 1950).
z = (1950 - 2000) / 60 = -50 / 60 = -0.83.
P(x < 1950) = P(z < -0.83) = 0.5 - phi(0.83) = 0.5 - 0.2967 = 0.2033.
Number of bulbs = 2500 * 0.2033 = 508.25 = 508 bulbs.

**Answer:**
**(i) 119 bulbs, (ii) 2263 bulbs (or 2262.5), (iii) 508 bulbs**

**Check:**
P(z > 1.67) + P(z < -1.67) = 2 * 0.0475 = 0.0950. 1 - 0.0950 = 0.9050, matching part (ii).

---

### Paper Jun / Jul 2024 (P2)

## Q.1 a) [6m] Obtain the mean and variance of Poisson distribution.

**Given:**
Poisson probability mass function: P(X = r) = e^(-m) * m^r / r! for r = 0, 1, 2, ...

**Formula / Method:**
1. Mean E(X) = sum_{r=0}^infty r * P(r).
2. Variance Var(X) = E(X^2) - [E(X)]^2, where E(X^2) = E[X(X-1)] + E(X).

**Solution:**
Step 1: Derivation of Mean E(X).
E(X) = sum_{r=0}^infty r * [e^(-m) * m^r / r!]
The term for r = 0 is zero, so:
E(X) = sum_{r=1}^infty r * [e^(-m) * m^r / r!] = e^(-m) * sum_{r=1}^infty [m^r / (r-1)!]
Factor out m:
E(X) = e^(-m) * m * sum_{r=1}^infty [m^(r-1) / (r-1)!]
Let j = r - 1. As r goes from 1 to infty, j goes from 0 to infty:
E(X) = e^(-m) * m * sum_{j=0}^infty [m^j / j!]
Since sum_{j=0}^infty [m^j / j!] = e^m:
E(X) = e^(-m) * m * e^m = m.
Therefore, Mean = m.

Step 2: Derivation of E[X(X-1)].
E[X(X-1)] = sum_{r=0}^infty r(r-1) * [e^(-m) * m^r / r!]
Terms for r = 0 and r = 1 are zero, so:
E[X(X-1)] = sum_{r=2}^infty r(r-1) * [e^(-m) * m^r / r!] = e^(-m) * sum_{r=2}^infty [m^r / (r-2)!]
Factor out m^2:
E[X(X-1)] = e^(-m) * m^2 * sum_{r=2}^infty [m^(r-2) / (r-2)!]
Let j = r - 2:
E[X(X-1)] = e^(-m) * m^2 * sum_{j=0}^infty [m^j / j!] = e^(-m) * m^2 * e^m = m^2.

Step 3: Derivation of Variance.
E(X^2) = E[X(X-1)] + E(X) = m^2 + m.
Var(X) = E(X^2) - [E(X)]^2 = (m^2 + m) - m^2 = m.

**Answer:**
**Mean = m, Variance = m**

**Check:**
In Poisson distribution, mean = variance = m.


## Q.1 b) [7m] Out of 800 families with 4 children each, how many families would be expected to have (i) 2 boys and 2 girls (ii) atleast one boy (iii) at most 2 girls. Assume equal probabilities for boys and girls.

**Given:**
Total families N = 800.
Number of children per family n = 4.
Probability of boy p = 1/2, probability of girl q = 1/2.
X = number of boys in family ~ Binomial(4, 1/2).

**Formula / Method:**
P(X = r) = 4Cr * (1/2)^4 = 4Cr / 16.
Expected families = N * P(r).

**Solution:**
Step 1: (i) Expected families with 2 boys and 2 girls (r = 2).
P(X = 2) = 4C2 * (1/2)^4 = 6 / 16 = 3/8.
Expected families = 800 * (3/8) = 300 families.

Step 2: (ii) Expected families with at least one boy (X >= 1).
P(X >= 1) = 1 - P(X = 0) = 1 - 4C0 * (1/2)^4 = 1 - (1/16) = 15/16.
Expected families = 800 * (15/16) = 750 families.

Step 3: (iii) Expected families with at most 2 girls.
At most 2 girls means girls <= 2, which means boys X >= 2.
P(X >= 2) = P(X=2) + P(X=3) + P(X=4) = (6/16) + (4/16) + (1/16) = 11/16.
Expected families = 800 * (11/16) = 550 families.

**Answer:**
**(i) 300 families, (ii) 750 families, (iii) 550 families**

**Check:**
P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) = (1 + 4 + 6 + 4 + 1)/16 = 16/16 = 1.


## Q.1 c) [7m] The length of telephone conversation in a booth has been an exponential distribution and found on an average to be 5 minutes. Find the probability that a random call made from this booth (i) ends less than 5 minutes (ii) between 5 and 10 minutes.

**Given:**
Mean = 5 minutes. Exponential parameter lambda = 1/5 = 0.2.
f(x) = (1/5) * e^(-x/5) for x >= 0.

**Formula / Method:**
P(a <= X <= b) = integral_a^b (1/5) * e^(-x/5) dx = e^(-a/5) - e^(-b/5).

**Solution:**
Step 1: (i) Probability ends in less than 5 minutes, P(X < 5).
P(X < 5) = integral_0^5 (1/5) * e^(-x/5) dx = [-e^(-x/5)]_0^5 = 1 - e^(-1).
Since e^(-1) = 0.367879..., P(X < 5) = 1 - 0.367879 = 0.632121... = 0.6321.

Step 2: (ii) Probability between 5 and 10 minutes, P(5 <= X <= 10).
P(5 <= X <= 10) = integral_5^10 (1/5) * e^(-x/5) dx = [-e^(-x/5)]_5^10 = e^(-1) - e^(-2).
Since e^(-1) = 0.367879... and e^(-2) = 0.135335...:
P(5 <= X <= 10) = 0.367879 - 0.135335 = 0.232544... = 0.2325.

**Answer:**
**(i) P(X < 5) = 1 - e^-1 = 0.6321, (ii) P(5 <= X <= 10) = e^-1 - e^-2 = 0.2325**

**Check:**
P(X < 10) = P(X < 5) + P(5 <= X <= 10) = 0.6321 + 0.2325 = 0.8646 = 1 - e^-2.


## Q.2 a) [6m] The probability distribution of a finite random variable X is given by  X: -2 -1 0 1 2 3 ; P(X): 0.1, k, 0.2, 2k, 0.3, k.  (i) Find the value of k (ii) Variance (iii) P(x <= 2)

**Given:**
Probability distribution table:
```
X   : -2   -1    0    1    2   3
P(X): 0.1   k   0.2  2k  0.3   k
```

**Formula / Method:**
1. sum(P(X)) = 1.
2. Mean E(X) = sum(x * P(x)).
3. Variance = E(X^2) - [E(X)]^2.

**Solution:**
Step 1: (i) Find k.
sum(P(X)) = 0.1 + k + 0.2 + 2k + 0.3 + k = 1
=> 0.6 + 4k = 1 => 4k = 0.4 => k = 0.1.
The complete distribution table is:
```
X   : -2    -1     0     1     2     3
P(X): 0.1   0.1   0.2   0.2   0.3   0.1
```

Step 2: (ii) Calculate Variance.
E(X) = (-2)(0.1) + (-1)(0.1) + (0)(0.2) + (1)(0.2) + (2)(0.3) + (3)(0.1)
E(X) = -0.2 - 0.1 + 0 + 0.2 + 0.6 + 0.3 = 0.8.

E(X^2) = (-2)^2(0.1) + (-1)^2(0.1) + 0^2(0.2) + 1^2(0.2) + 2^2(0.3) + 3^2(0.1)
E(X^2) = 4(0.1) + 1(0.1) + 0 + 1(0.2) + 4(0.3) + 9(0.1)
E(X^2) = 0.4 + 0.1 + 0 + 0.2 + 1.2 + 0.9 = 2.8.

Variance = E(X^2) - [E(X)]^2 = 2.8 - (0.8)^2 = 2.8 - 0.64 = 2.16.

Step 3: (iii) Evaluate P(x <= 2).
P(x <= 2) = P(-2) + P(-1) + P(0) + P(1) + P(2)
P(x <= 2) = 0.1 + 0.1 + 0.2 + 0.2 + 0.3 = 0.9.
Alternatively, P(x <= 2) = 1 - P(3) = 1 - 0.1 = 0.9.

**Answer:**
**(i) k = 0.1, (ii) Variance = 2.16, (iii) P(x <= 2) = 0.9**

**Check:**
E(X) = 0.8, E(X^2) = 2.8, Variance = 2.8 - 0.64 = 2.16.


## Q.2 b) [7m] The number of accidents in a year to taxi drivers in a city follows a Poisson distribution with mean 3. Out of 1000 taxi drivers find approximately number of drivers with (i) more than 3 accidents in a year (ii) at most 2 accidents in a year.

**Given:**
Poisson mean m = 3. Total drivers N = 1000.
P(r) = e^(-3) * 3^r / r!
e^(-3) = 0.049787...

**Formula / Method:**
Expected drivers = N * P.

**Solution:**
Step 1: Compute P(r) values.
P(0) = e^(-3) = 0.049787...
P(1) = 3 * e^(-3) = 0.149361...
P(2) = (3^2 / 2) * e^(-3) = 4.5 * e^(-3) = 0.224042...
P(3) = (3^3 / 6) * e^(-3) = 4.5 * e^(-3) = 0.224042...

Step 2: (i) More than 3 accidents in a year, P(X > 3).
P(X <= 3) = P(0) + P(1) + P(2) + P(3) = (1 + 3 + 4.5 + 4.5) * e^(-3) = 13 * e^(-3) = 0.647231...
P(X > 3) = 1 - 0.647231... = 0.352769... = 0.3528.
Expected drivers = 1000 * 0.352769... = 352.77 = 353 drivers.

Step 3: (ii) At most 2 accidents in a year, P(X <= 2).
P(X <= 2) = P(0) + P(1) + P(2) = (1 + 3 + 4.5) * e^(-3) = 8.5 * e^(-3) = 0.423190... = 0.4232.
Expected drivers = 1000 * 0.423190... = 423.19 = 423 drivers.

**Answer:**
**(i) 353 drivers, (ii) 423 drivers**

**Check:**
P(X <= 2) + P(X = 3) + P(X > 3) = 0.4232 + 0.2240 + 0.3528 = 1.0000.


## Q.2 c) [7m] The marks of 1000 students in an exam follows normal distribution with mean 70 and standard deviation 5. Find the students whose marks will be (i) less than 65 (ii) between 65 and 75. A(1) = 0.3413.

**Given:**
Mean mu = 70, Standard deviation sigma = 5, Total students N = 1000.
Given A(1) = 0.3413.

**Formula / Method:**
z = (x - mu) / sigma. Expected students = N * P.

**Solution:**
Step 1: (i) Less than 65, P(X < 65).
z = (65 - 70) / 5 = -1.
P(X < 65) = P(z < -1) = 0.5 - A(1) = 0.5 - 0.3413 = 0.1587.
Expected students = 1000 * 0.1587 = 158.7 = 159 students.

Step 2: (ii) Between 65 and 75, P(65 <= X <= 75).
For x1 = 65: z1 = (65 - 70) / 5 = -1.
For x2 = 75: z2 = (75 - 70) / 5 = 1.
P(-1 <= z <= 1) = 2 * A(1) = 2 * 0.3413 = 0.6826.
Expected students = 1000 * 0.6826 = 682.6 = 683 students.

**Answer:**
**(i) 159 students, (ii) 683 students**

**Check:**
P(X < 65) + P(65 <= X <= 75) + P(X > 75) = 0.1587 + 0.6826 + 0.1587 = 1.0000.

---

### Paper Dec 2024 / Jan 2025 (P3)

## Q.1 a) [7m] A random variable x has the following prob. density function for various values of x.  x: 0..7 ; P(x): 0, k, 2k, 2k, 3k, k^2, 2k^2, 7k^2+k.  Find the value of k and evaluate P(x < 6), P(3 < x <= 6) and (x >= 6).

**Given:**
Probability distribution table:
```
x   : 0   1   2   3   4   5     6      7
P(x): 0   k   2k  2k  3k  k^2   2k^2   7k^2+k
```

**Formula / Method:**
sum(P(x)) = 1 to find k.

**Solution:**
Step 1: Find k.
sum(P(x)) = 0 + k + 2k + 2k + 3k + k^2 + 2k^2 + (7k^2 + k) = 1
=> 10k^2 + 9k - 1 = 0
=> (10k - 1)(k + 1) = 0 => k = 1/10 = 0.1 (since P(x) >= 0).

Step 2: Evaluate P(x < 6).
P(x < 6) = P(0) + P(1) + P(2) + P(3) + P(4) + P(5)
P(x < 6) = 0 + k + 2k + 2k + 3k + k^2 = 8k + k^2
Substitute k = 1/10:
P(x < 6) = 8(1/10) + (1/10)^2 = 8/10 + 1/100 = 81/100 = 0.81.

Step 3: Evaluate P(3 < x <= 6).
P(3 < x <= 6) = P(4) + P(5) + P(6) = 3k + k^2 + 2k^2 = 3k^2 + 3k
Substitute k = 1/10:
P(3 < x <= 6) = 3/100 + 30/100 = 33/100 = 0.33.

Step 4: Evaluate P(x >= 6).
P(x >= 6) = P(6) + P(7) = 2k^2 + (7k^2 + k) = 9k^2 + k
Substitute k = 1/10:
P(x >= 6) = 9/100 + 10/100 = 19/100 = 0.19.

**Answer:**
**k = 1/10 = 0.1, P(x < 6) = 81/100 = 0.81, P(3 < x <= 6) = 33/100 = 0.33, P(x >= 6) = 19/100 = 0.19**

**Check:**
P(x < 6) + P(x >= 6) = 0.81 + 0.19 = 1.00.


## Q.1 b) [6m] Derive the mean and variance of Poisson distribution.
Same as Q.1 a) of Paper Jun / Jul 2024 (P2) (answer: Mean = m, Variance = m)


## Q.1 c) [7m] In a certain town the duration of a shower is exponentially distributed with mean 5 minutes. What is the probability that a shower will last for? (i) less than 10 minutes (ii) more than 10 minutes and (iii) between 10 and 12 minutes.
Same as Q.1 c) of Paper Dec 2023 / Jan 2024 (P1) (answer: (i) P(X < 10) = 1 - e^-2 = 0.8647, (ii) P(X > 10) = e^-2 = 0.1353, (iii) P(10 <= X <= 12) = e^-2 - e^-2.4 = 0.0446)


## Q.2 a) [7m] The probability density function of f(x) = K x^2 for -3 < x < 3, 0 elsewhere. Find the value of K and evaluate (i) P(x <= 2), P(x > 1) (ii) P(1 <= x <= 2)

**Given:**
Continuous pdf f(x) = K * x^2 for -3 < x < 3, 0 elsewhere.

**Formula / Method:**
integral_{-3}^3 f(x) dx = 1 to find K.

**Solution:**
Step 1: Find K.
integral_{-3}^3 K * x^2 dx = 1 => 18 K = 1 => K = 1/18.

Step 2: Evaluate P(x <= 2).
P(x <= 2) = integral_{-3}^2 (1/18) * x^2 dx = (1/18) * [x^3 / 3]_{-3}^2 = (1/18) * (8/3 + 27/3) = 35/54 = 0.6481.

Step 3: Evaluate P(x > 1).
P(x > 1) = integral_1^3 (1/18) * x^2 dx = (1/18) * [x^3 / 3]_1^3 = (1/18) * (27/3 - 1/3) = (1/18) * (26/3) = 26/54 = 13/27 = 0.4815.

Step 4: Evaluate P(1 <= x <= 2).
P(1 <= x <= 2) = integral_1^2 (1/18) * x^2 dx = (1/18) * [x^3 / 3]_1^2 = (1/18) * (8/3 - 1/3) = 7/54 = 0.1296.

**Answer:**
**K = 1/18, P(x <= 2) = 35/54 = 0.6481, P(x > 1) = 13/27 = 0.4815, P(1 <= x <= 2) = 7/54 = 0.1296**

**Check:**
P(x <= 1) + P(x > 1) = [ (1/18)*(1/3 + 27/3) ] + 26/54 = 28/54 + 26/54 = 54/54 = 1.0.


## Q.2 b) [6m] When a coin is tossed 4 times, find the probability of getting (i) exactly one head (ii) atleast three heads and (iii) less than two heads.

**Given:**
Number of tosses n = 4.
Probability of head p = 1/2, q = 1/2.
X = number of heads ~ Binomial(4, 1/2).

**Formula / Method:**
P(X = r) = 4Cr * (1/2)^4 = 4Cr / 16.

**Solution:**
Step 1: (i) Exactly one head, P(X = 1).
P(X = 1) = 4C1 * (1/2)^4 = 4 / 16 = 1/4 = 0.25.

Step 2: (ii) At least three heads, P(X >= 3).
P(X >= 3) = P(X = 3) + P(X = 4) = (4C3 + 4C4) / 16 = (4 + 1) / 16 = 5/16 = 0.3125.

Step 3: (iii) Less than two heads, P(X < 2).
P(X < 2) = P(X = 0) + P(X = 1) = (4C0 + 4C1) / 16 = (1 + 4) / 16 = 5/16 = 0.3125.

**Answer:**
**(i) P(X = 1) = 1/4 = 0.25, (ii) P(X >= 3) = 5/16 = 0.3125, (iii) P(X < 2) = 5/16 = 0.3125**

**Check:**
Sum of all probabilities for r = 0, 1, 2, 3, 4: (1 + 4 + 6 + 4 + 1)/16 = 16/16 = 1.


## Q.2 c) [7m] The marks of 1000 students in an examination follows a normal distribution with mean 70 and S.D 5. Find the number of students whose marks will be (i) less than 65 (ii) more than 75 and (iii) between 65 and 75.

Note: The question paper scan misprints mean as "> 0"; the correct value is mean = 70.

**Given:**
Mean mu = 70, Standard deviation sigma = 5, Total students N = 1000.
Normal table value A(1) = 0.3413.

**Formula / Method:**
z = (x - mu) / sigma. Expected students = N * P.

**Solution:**
Step 1: (i) Less than 65, P(X < 65).
z = (65 - 70) / 5 = -1.
P(X < 65) = P(z < -1) = 0.5 - A(1) = 0.5 - 0.3413 = 0.1587.
Expected students = 1000 * 0.1587 = 158.7 = 159 students.

Step 2: (ii) More than 75, P(X > 75).
z = (75 - 70) / 5 = 1.
P(X > 75) = P(z > 1) = 0.5 - A(1) = 0.5 - 0.3413 = 0.1587.
Expected students = 1000 * 0.1587 = 158.7 = 159 students.

Step 3: (iii) Between 65 and 75, P(65 <= X <= 75).
z1 = (65 - 70)/5 = -1, z2 = (75 - 70)/5 = 1.
P(-1 <= z <= 1) = 2 * A(1) = 2 * 0.3413 = 0.6826.
Expected students = 1000 * 0.6826 = 682.6 = 683 students.

**Answer:**
**(i) 159 students, (ii) 159 students, (iii) 683 students**

**Check:**
159 + 159 + 683 = 1001 (due to rounding of 158.7 + 158.7 + 682.6 = 1000.0).

---

### Paper Jun / Jul 2025 (P4)

## Q.1 a) [6m] The probability density function of a variate X is given by the following table: X: 0 1 2 3 4 5 6 ; P(X): K, 3K, 5K, 7K, 9K, 11K, 13K.  (i) For what value of K, does this represent a valid probability distribution? (ii) Find P(X<4) (iii) Find P(3<X<=6)

**Given:**
Probability table of discrete variate X:
```
X   : 0   1   2   3   4   5    6
P(X): K  3K  5K  7K  9K 11K  13K
```

**Formula / Method:**
1. sum(P(X)) = 1 to find K.
2. P(A) = sum of P(x) for x in A.

**Solution:**
Step 1: (i) Find K.
sum(P(X)) = K + 3K + 5K + 7K + 9K + 11K + 13K = 1
=> 49 K = 1 => K = 1/49.

Step 2: (ii) Find P(X < 4).
P(X < 4) = P(0) + P(1) + P(2) + P(3)
P(X < 4) = K + 3K + 5K + 7K = 16 K
Substitute K = 1/49:
P(X < 4) = 16/49 = 0.3265.

Step 3: (iii) Find P(3 < X <= 6).
The values of X satisfying 3 < X <= 6 are X = 4, 5, 6.
P(3 < X <= 6) = P(4) + P(5) + P(6)
P(3 < X <= 6) = 9K + 11K + 13K = 33 K
Substitute K = 1/49:
P(3 < X <= 6) = 33/49 = 0.6735.

**Answer:**
**(i) K = 1/49, (ii) P(X < 4) = 16/49 = 0.3265, (iii) P(3 < X <= 6) = 33/49 = 0.6735**

**Check:**
P(X < 4) + P(3 < X <= 6) = 16/49 + 33/49 = 49/49 = 1.0.


## Q.1 b) [7m] 2% fuses manufactured by a firm are found to be defective. Find the probability that the box containing 200 fuses contains. (i) No defective fuses (ii) 3 or more defective fuses. (iii) Atleast one defective fuse.

**Given:**
Defective fraction p = 2% = 0.02.
Box size n = 200.
Since n is large and p is small, use Poisson distribution with parameter lambda = n * p = 200 * 0.02 = 4.
e^(-4) = 0.0183156...

**Formula / Method:**
Poisson probability P(r) = e^(-4) * 4^r / r!

**Solution:**
Step 1: Compute P(r) values.
P(0) = e^(-4) = 0.0183156... = 0.0183.
P(1) = 4 * e^(-4) = 0.0732625...
P(2) = (4^2 / 2) * e^(-4) = 8 * e^(-4) = 0.1465251...

Step 2: (i) No defective fuses, P(0).
P(0) = e^(-4) = 0.0183156... = 0.0183.

Step 3: (ii) 3 or more defective fuses, P(X >= 3).
P(X < 3) = P(0) + P(1) + P(2) = (1 + 4 + 8) * e^(-4) = 13 * e^(-4) = 13 * 0.0183156... = 0.238103...
P(X >= 3) = 1 - P(X < 3) = 1 - 0.238103... = 0.761897... = 0.7619.

Step 4: (iii) At least one defective fuse, P(X >= 1).
P(X >= 1) = 1 - P(0) = 1 - e^(-4) = 1 - 0.0183156... = 0.981684... = 0.9817.

**Answer:**
**(i) P(0) = e^-4 = 0.0183, (ii) P(X >= 3) = 1 - 13 e^-4 = 0.7619, (iii) P(X >= 1) = 1 - e^-4 = 0.9817**

**Check:**
P(0) + P(1) + P(2) + P(X >= 3) = 13 e^-4 + (1 - 13 e^-4) = 1.0000.


## Q.1 c) [7m] The length in time (minutes) that a certain lady speaks on a telephone is a random variable with probability density function f(x) = A e^(-x/5) for x > 0, 0 elsewhere. Find the value of the constant A. What is the probability that she will speak over the phone for, (i) More than 10 minutes (ii) Less than 5 minutes (iii) Between 5 and 10 minutes.

**Given:**
Continuous pdf f(x) = A * e^(-x/5) for x > 0, 0 elsewhere.

**Formula / Method:**
1. integral_0^infty f(x) dx = 1 to find A.
2. P(a <= X <= b) = integral_a^b (1/5) e^(-x/5) dx = e^(-a/5) - e^(-b/5).

**Solution:**
Step 1: Find A.
integral_0^infty A * e^(-x/5) dx = 1
=> A * [-5 * e^(-x/5)]_0^infty = 1
=> A * [0 - (-5)] = 5 A = 1 => A = 1/5 = 0.2.

Step 2: (i) More than 10 minutes, P(X > 10).
P(X > 10) = integral_10^infty (1/5) * e^(-x/5) dx = [-e^(-x/5)]_10^infty = e^(-2).
Since e^(-2) = 0.135335..., P(X > 10) = 0.1353.

Step 3: (ii) Less than 5 minutes, P(X < 5).
P(X < 5) = integral_0^5 (1/5) * e^(-x/5) dx = [-e^(-x/5)]_0^5 = 1 - e^(-1).
Since e^(-1) = 0.367879..., P(X < 5) = 1 - 0.367879 = 0.632121... = 0.6321.

Step 4: (iii) Between 5 and 10 minutes, P(5 < X < 10).
P(5 < X < 10) = integral_5^10 (1/5) * e^(-x/5) dx = e^(-1) - e^(-2).
P(5 < X < 10) = 0.367879 - 0.135335 = 0.232544... = 0.2325.

**Answer:**
**A = 1/5 = 0.2, (i) P(X > 10) = e^-2 = 0.1353, (ii) P(X < 5) = 1 - e^-1 = 0.6321, (iii) P(5 < X < 10) = e^-1 - e^-2 = 0.2325**

**Check:**
P(X < 5) + P(5 < X < 10) + P(X > 10) = (1 - e^-1) + (e^-1 - e^-2) + e^-2 = 1.0.


## Q.2 a) [6m] Find the constant K such that the function f(x) = K x^2 for 0 < x < 3, 0 otherwise is a probability density function. Also compute P(1 < x < 2), P(x <= 1).

**Given:**
f(x) = K * x^2 for 0 < x < 3, 0 otherwise.

**Formula / Method:**
integral_0^3 f(x) dx = 1 to find K.

**Solution:**
Step 1: Find K.
integral_0^3 K * x^2 dx = 1
=> K * [x^3 / 3]_0^3 = 1
=> K * [27 / 3 - 0] = 9 K = 1 => K = 1/9.

Step 2: Compute P(1 < x < 2).
P(1 < x < 2) = integral_1^2 (1/9) * x^2 dx = (1/9) * [x^3 / 3]_1^2
P(1 < x < 2) = (1/9) * [ (8/3) - (1/3) ] = (1/9) * (7/3) = 7/27 = 0.2593.

Step 3: Compute P(x <= 1).
P(x <= 1) = integral_0^1 (1/9) * x^2 dx = (1/9) * [x^3 / 3]_0^1
P(x <= 1) = (1/9) * [1/3 - 0] = 1/27 = 0.0370.

**Answer:**
**K = 1/9, P(1 < x < 2) = 7/27 = 0.2593, P(x <= 1) = 1/27 = 0.0370**

**Check:**
P(x <= 1) + P(1 < x < 2) + P(x >= 2) = 1/27 + 7/27 + (1/9)*(27/3 - 8/3) = 8/27 + 19/27 = 27/27 = 1.0.


## Q.2 b) [7m] Obtain the mean and variance of Binomial distribution.
Same as Q.1 b) of Paper Dec 2023 / Jan 2024 (P1) (answer: Mean = np, Variance = npq)


## Q.2 c) [7m] The marks of 1000 students in an examination follows a normal distribution with mean 70 and standard deviation 5. Find the number of students whose marks will be, (i) Less than 65 (ii) More than 75 (iii) between 65 and 75, Given A(1) = 0.3413, where A(Z) is the area under standard normal curve from 0 to Z.
Same as Q.2 c) of Paper Dec 2024 / Jan 2025 (P3) (answer: (i) 159 students, (ii) 159 students, (iii) 683 students)

---

### Paper Jun / Jul 2025 Makeup (P5)

## Q.1 a) [6m] Derive Mean and Variance of Poisson Distribution.
Same as Q.1 a) of Paper Jun / Jul 2024 (P2) (answer: Mean = m, Variance = m)


## Q.1 b) [7m] The probability that a pen manufactured by a factory be defective is 1/10, if 12 such pens are manufactured. What is the probability that : (i) Exactly two are defective (ii) Atleast two are defective (iii) None of them are defective.

**Given:**
Defective probability p = 1/10 = 0.1, q = 1 - 0.1 = 0.9.
Number of pens n = 12.
X = number of defective pens ~ Binomial(12, 0.1).

**Formula / Method:**
P(X = r) = 12Cr * (0.1)^r * (0.9)^(12-r).

**Solution:**
Step 1: (i) Exactly two are defective, P(X = 2).
P(X = 2) = 12C2 * (0.1)^2 * (0.9)^10
12C2 = (12 * 11) / 2 = 66.
(0.1)^2 = 0.01.
(0.9)^10 = 0.34867844...
P(X = 2) = 66 * 0.01 * 0.34867844... = 0.230128... = 0.2301.

Step 2: (iii) None of them are defective, P(X = 0).
P(X = 0) = 12C0 * (0.1)^0 * (0.9)^12 = (0.9)^12 = 0.2824295... = 0.2824.

Step 3: (ii) At least two are defective, P(X >= 2).
P(X = 1) = 12C1 * (0.1)^1 * (0.9)^11 = 12 * 0.1 * 0.3138106... = 0.3765727...
P(X < 2) = P(X = 0) + P(X = 1) = 0.2824295 + 0.3765727 = 0.6590022...
P(X >= 2) = 1 - P(X < 2) = 1 - 0.6590022... = 0.340998... = 0.3410.

**Answer:**
**(i) P(X = 2) = 0.2301, (ii) P(X >= 2) = 0.3410, (iii) P(X = 0) = 0.2824**

**Check:**
P(0) + P(1) + P(2) + P(X > 2) = 0.2824 + 0.3766 + 0.2301 + (1 - 0.6590 - 0.2301) = 1.0000.


## Q.1 c) [7m] The marks of 1000 students in an examination follows a normal distribution with mean 70 and standard deviation 5. Find the number of students whose marks will be: (i) Less than 65 (ii) More than 75 (iii) Between 65 and 75 [Given phi(1) = 0.3413]
Same as Q.2 c) of Paper Dec 2024 / Jan 2025 (P3) (answer: (i) 159 students, (ii) 159 students, (iii) 683 students)


## Q.2 a) [6m] The p.d.f of a variate X is given by the following table: x: 0..6 ; p(x): k, 3k, 5k, 7k, 9k, 11k, 13k. For what value of K, this represents a valid probability distribution? Also find p(x >= 5) and p(3 < x <= 6).

**Given:**
Probability table:
```
x   : 0   1   2   3   4   5    6
p(x): k  3k  5k  7k  9k 11k  13k
```

**Formula / Method:**
sum(p(x)) = 1 to find k.

**Solution:**
Step 1: Find k.
sum(p(x)) = k + 3k + 5k + 7k + 9k + 11k + 13k = 49 k = 1 => k = 1/49.

Step 2: Find p(x >= 5).
p(x >= 5) = p(5) + p(6) = 11k + 13k = 24k
Substitute k = 1/49:
p(x >= 5) = 24/49 = 0.4898.

Step 3: Find p(3 < x <= 6).
p(3 < x <= 6) = p(4) + p(5) + p(6) = 9k + 11k + 13k = 33k
Substitute k = 1/49:
p(3 < x <= 6) = 33/49 = 0.6735.

**Answer:**
**k = 1/49, p(x >= 5) = 24/49 = 0.4898, p(3 < x <= 6) = 33/49 = 0.6735**

**Check:**
p(x < 5) + p(x >= 5) = 25/49 + 24/49 = 49/49 = 1.0.


## Q.2 b) [7m] The number of accidents in a year to taxi drivers in a city follows a Poisson distribution with mean 3. Out of 1000 taxi drivers find approximately the number of the drivers with (i) No accident in a year (ii) More than 3 accidents in a year.

**Given:**
Poisson mean m = 3, N = 1000 drivers.
P(r) = e^(-3) * 3^r / r!
e^(-3) = 0.049787...

**Formula / Method:**
Expected drivers = N * P.

**Solution:**
Step 1: (i) No accident in a year, P(0).
P(0) = e^(-3) = 0.049787... = 0.0498.
Expected drivers = 1000 * 0.049787... = 49.79 = 50 drivers.

Step 2: (ii) More than 3 accidents in a year, P(X > 3).
P(X <= 3) = P(0) + P(1) + P(2) + P(3) = (1 + 3 + 4.5 + 4.5) * e^(-3) = 13 * e^(-3) = 0.647231...
P(X > 3) = 1 - 0.647231... = 0.352769... = 0.3528.
Expected drivers = 1000 * 0.352769... = 352.77 = 353 drivers.

**Answer:**
**(i) 50 drivers, (ii) 353 drivers**

**Check:**
P(0) = 0.0498, 1000 * 0.049787 = 49.79 ~ 50.


## Q.2 c) [7m] If x is a normal variate with mean 30 and standard deviation 5 find the probability that (i) 26 <= x <= 40 (ii) x >= 45

**Given:**
Mean mu = 30, Standard deviation sigma = 5.
Normal table values: phi(0.8) = 0.2881, phi(2.0) = 0.4772, phi(3.0) = 0.4987.

**Formula / Method:**
z = (x - mu) / sigma.

**Solution:**
Step 1: (i) Probability 26 <= x <= 40.
For x1 = 26: z1 = (26 - 30) / 5 = -4/5 = -0.8.
For x2 = 40: z2 = (40 - 30) / 5 = 10/5 = 2.0.
P(-0.8 <= z <= 2.0) = phi(0.8) + phi(2.0)
P(-0.8 <= z <= 2.0) = 0.2881 + 0.4772 = 0.7653.

Step 2: (ii) Probability x >= 45.
For x = 45: z = (45 - 30) / 5 = 15/5 = 3.0.
P(z >= 3.0) = 0.5 - phi(3.0) = 0.5 - 0.4987 = 0.0013.

**Answer:**
**(i) P(26 <= x <= 40) = 0.7653, (ii) P(x >= 45) = 0.0013**

**Check:**
P(x < 26) = 0.5 - 0.2881 = 0.2119. P(26 <= x <= 40) = 0.7653. P(40 < x < 45) = 0.4987 - 0.4772 = 0.0215. P(x >= 45) = 0.0013. Sum = 0.2119 + 0.7653 + 0.0215 + 0.0013 = 1.0000.

---

### Paper Dec 2025 / Jan 2026 (P6)

## Q.1 a) [6m] A random variable X has the following probability function for various values of X.  X: 0..7 ; P(x): 0, K, 2k, 2k, 3k, k^2, 2k^2, 7k^2+k.  i) Find the value of k ii) Evaluate P[x < 6], P[0 < x < 5], P[x >= 6].

**Given:**
Probability table:
```
X   : 0   1   2   3   4   5     6      7
P(x): 0   k   2k  2k  3k  k^2   2k^2   7k^2+k
```

**Formula / Method:**
sum(P(x)) = 1 to find k.

**Solution:**
Step 1: i) Find k.
sum(P(x)) = 10k^2 + 9k = 1 => 10k^2 + 9k - 1 = 0 => (10k - 1)(k + 1) = 0 => k = 1/10 = 0.1.

Step 2: ii) Evaluate P[x < 6].
P[x < 6] = P(0) + P(1) + P(2) + P(3) + P(4) + P(5) = 8k + k^2 = 8(1/10) + (1/100) = 81/100 = 0.81.

Step 3: Evaluate P[0 < x < 5].
The values of x satisfying 0 < x < 5 are x = 1, 2, 3, 4.
P[0 < x < 5] = P(1) + P(2) + P(3) + P(4) = k + 2k + 2k + 3k = 8k
Substitute k = 1/10:
P[0 < x < 5] = 8/10 = 4/5 = 0.8.

Step 4: Evaluate P[x >= 6].
P[x >= 6] = P(6) + P(7) = 2k^2 + (7k^2 + k) = 9k^2 + k = 9/100 + 1/10 = 19/100 = 0.19.

**Answer:**
**i) k = 1/10 = 0.1, ii) P[x < 6] = 81/100 = 0.81, P[0 < x < 5] = 4/5 = 0.8, P[x >= 6] = 19/100 = 0.19**

**Check:**
P[0 < x < 5] + P(0) + P(5) = 0.8 + 0 + 0.01 = 0.81 = P[x < 6].


## Q.1 b) [7m] Find the mean and standard deviation of Binomial distribution.
Same as Q.1 b) of Paper Dec 2023 / Jan 2024 (P1), with Standard Deviation sigma = sqrt(npq) (answer: Mean = np, Standard Deviation = sqrt(npq))


## Q.1 c) [7m] If the probability of a bad reaction from a certain injection is 0.001. Determine the probability that out of 2000 individuals more than two will get a bad reaction.

**Given:**
Probability of bad reaction p = 0.001.
Number of individuals n = 2000.
Poisson parameter lambda = n * p = 2000 * 0.001 = 2.
e^(-2) = 0.135335...

**Formula / Method:**
Poisson probability P(r) = e^(-2) * 2^r / r!
P(X > 2) = 1 - [P(0) + P(1) + P(2)].

**Solution:**
Step 1: Compute P(0), P(1), P(2).
P(0) = e^(-2) = 0.135335...
P(1) = 2 * e^(-2) = 0.270670...
P(2) = (2^2 / 2) * e^(-2) = 2 * e^(-2) = 0.270670...

Step 2: Sum P(0) + P(1) + P(2).
P(X <= 2) = P(0) + P(1) + P(2) = (1 + 2 + 2) * e^(-2) = 5 * e^(-2) = 5 * 0.135335... = 0.676676...

Step 3: Compute P(X > 2).
P(X > 2) = 1 - 5 * e^(-2) = 1 - 0.676676... = 0.323324... = 0.3233.

**Answer:**
**P(X > 2) = 1 - 5 e^-2 = 0.3233**

**Check:**
5 * e^(-2) + (1 - 5 e^(-2)) = 1.0000.


## Q.2 a) [6m] Find K such that F(x) = k e^(-x) for 0 < x < 1, 0 otherwise represents a valid pdf and hence find mean of the distribution.

Note: The question text uses F(x) to denote the probability density function.

**Given:**
pdf f(x) = k * e^(-x) for 0 < x < 1, 0 otherwise.

**Formula / Method:**
1. integral_0^1 k * e^(-x) dx = 1 to find k.
2. Mean E(X) = integral_0^1 x * f(x) dx.

**Solution:**
Step 1: Find k.
integral_0^1 k * e^(-x) dx = 1
=> k * [-e^(-x)]_0^1 = 1
=> k * (-e^(-1) - (-1)) = k * (1 - e^(-1)) = 1
=> k = 1 / (1 - e^(-1)).
Since e^(-1) = 0.367879..., 1 - e^(-1) = 0.632121...
k = 1 / 0.632121... = 1.581977... = 1.5820.

Step 2: Find Mean E(X).
E(X) = integral_0^1 x * [k * e^(-x)] dx = k * integral_0^1 x * e^(-x) dx.
Using integration by parts on integral_0^1 x e^(-x) dx:
integral x e^(-x) dx = -x e^(-x) - e^(-x) = -e^(-x)(x + 1).
Evaluated from 0 to 1:
[-e^(-1)(1 + 1)] - [-e^0(0 + 1)] = -2 e^(-1) - (-1) = 1 - 2 e^(-1).
Since 2 e^(-1) = 2 * 0.367879... = 0.735759...:
integral_0^1 x e^(-x) dx = 1 - 0.735759... = 0.264241...

Multiply by k:
E(X) = k * (1 - 2 e^(-1)) = [1 / (1 - e^(-1))] * (1 - 2 e^(-1)).
E(X) = 1.581977... * 0.264241... = 0.418023... = 0.4180.

**Answer:**
**k = 1 / (1 - e^-1) = 1.5820, Mean E(X) = 0.4180**

**Check:**
0 < E(X) < 1, which lies within the interval (0, 1).


## Q.2 b) [7m] In a certain town the duration of a shower is exponentially distributed with mean 5 minutes. What is the probability that a shower will last for i) 10 minutes or more ii) less than 10 minutes.
Same as parts (i) and (ii) of Q.1 c) of Paper Dec 2023 / Jan 2024 (P1) (answer: (i) P(X >= 10) = e^-2 = 0.1353, (ii) P(X < 10) = 1 - e^-2 = 0.8647)


## Q.2 c) [7m] The marks of 1000 students in an examination follows a normal distribution with mu = 70 and S.D = 5. Find the number of students whose marks will be i) less than 65 ii) more than 75 iii) between 65 & 75. Given phi(1) = 0.3413.
Same as Q.2 c) of Paper Dec 2024 / Jan 2025 (P3) (answer: (i) 159 students, (ii) 159 students, (iii) 683 students)

---

### Paper Model Question Paper-I (P7)

## Q.1 a) [6m] The probability distribution function of variate X is given by the following table; x: 0..6 ; P(x): k, 3k, 5k, 7k, 9k, 11k, 13k. i) Find the value of k, ii) P(x >= 5) & iii) P(3 < x <= 6).
Same as Q.2 a) of Paper Jun / Jul 2025 Makeup (P5) (answer: (i) k = 1/49, (ii) P(x >= 5) = 24/49 = 0.4898, (iii) P(3 < x <= 6) = 33/49 = 0.6735)


## Q.1 b) [7m] If the probability of a bad reaction from a certain injection is 0.001, determine the chance that more than two of 2000 individuals will have a bad reaction.
Same as Q.1 c) of Paper Dec 2025 / Jan 2026 (P6) (answer: P(X > 2) = 1 - 5 e^-2 = 0.3233)


## Q.1 c) [7m] Find the mean and standard deviation of Poisson's distribution.
Same as Q.1 a) of Paper Jun / Jul 2024 (P2), with Standard Deviation sigma = sqrt(m) (answer: Mean = m, Standard Deviation = sqrt(m))


## Q.2 a) [6m] The probability of a pen manufactured by a factory be defective is 1/10. If 12 such pens are manufactured, what is the probability that i) exactly 2 are defective, ii) at least 2 are defective, iii) none of them are defective.
Same as Q.1 b) of Paper Jun / Jul 2025 Makeup (P5) (answer: (i) P(X = 2) = 0.2301, (ii) P(X >= 2) = 0.3410, (iii) P(X = 0) = 0.2824)


## Q.2 b) [7m] Determine the value of k, so that the function f(x) = k(x^2 + 4) for x = 0, 1, 2, 3 can serve as a probability distribution of the discrete random variable X: Also find i) P(0 < x <= 2) and ii) P(x >= 1).

**Given:**
Discrete function f(x) = k(x^2 + 4) for x = 0, 1, 2, 3.

**Formula / Method:**
1. sum_{x=0}^3 f(x) = 1 to find k.
2. P(A) = sum of f(x) for x in A.

**Solution:**
Step 1: Find k.
sum_{x=0}^3 k(x^2 + 4) = 1
k * [ (0^2 + 4) + (1^2 + 4) + (2^2 + 4) + (3^2 + 4) ] = 1
k * [ 4 + 5 + 8 + 13 ] = 1
30 k = 1 => k = 1/30.

Step 2: i) Find P(0 < x <= 2).
The values of x satisfying 0 < x <= 2 are x = 1, 2.
P(0 < x <= 2) = f(1) + f(2) = k(5 + 8) = 13 k
Substitute k = 1/30:
P(0 < x <= 2) = 13/30 = 0.4333.

Step 3: ii) Find P(x >= 1).
P(x >= 1) = f(1) + f(2) + f(3) = 1 - f(0)
f(0) = 4 k = 4/30.
P(x >= 1) = 1 - 4/30 = 26/30 = 13/15 = 0.8667.

**Answer:**
**k = 1/30, i) P(0 < x <= 2) = 13/30 = 0.4333, ii) P(x >= 1) = 13/15 = 0.8667**

**Check:**
f(0) + f(1) + f(2) + f(3) = (4 + 5 + 8 + 13)/30 = 30/30 = 1.0.


## Q.2 c) [7m] Find the mean and standard deviation of Binomial distribution.
Same as Q.1 b) of Paper Dec 2023 / Jan 2024 (P1), with Standard Deviation sigma = sqrt(npq) (answer: Mean = np, Standard Deviation = sqrt(npq))
