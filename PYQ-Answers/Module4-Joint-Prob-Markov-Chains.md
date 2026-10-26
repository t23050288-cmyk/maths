# Module 4: Joint Probability Distribution + Markov Chains

## Table of Contents
- [Paper 1 (Dec 2023 / Jan 2024)](#paper-1-dec-2023--jan-2024)
  - [Q.3 a) Joint Table X={1,2}, Y={-2,-1,4,5} [6 marks]](#q3-a-the-joint-probability-distribution-table-for-two-random-variable-x-and-y-is-as-follows-y--2--1-4-5--x1-01-02-0-03--x2-02-01-01-0-determine-the-marginal-probability-distribution-of-x-and-y-obtain-the-correlation-coefficient-between-x-and-y-6-marks)
  - [Q.3 b) Fixed Probability Vector for P1 [7 marks]](#q3-b-find-the-unique-fixed-probability-vector-for-the-regular-stochastic-matrix-a---01016121302313-7-marks)
  - [Q.3 c) Three Boys Throwing Ball (3 Throws) [7 marks]](#q3-c-three-boys-a-b-c-are-throwing-ball-to-each-other-a-always-throws-the-ball-to-b-and-b-always-throws-the-ball-to-c-c-is-just-as-likely-to-throw-the-ball-to-b-as-to-a-if-c-was-the-first-person-to-throw-the-ball-find-the-probabilities-that-after-three-throws--i-a-has-the-ball-ii-b-has-the-ball-iii-c-has-the-ball-7-marks)
  - [Q.4 a) Joint PMF f(x,y) = k(2x+y) for 0<=x<=2, 0<=y<=3 [6 marks]](#q4-a-the-joint-probability-distribution-of-two-discrete-random-variables-x-and-y-is-given-by-fx-y--k2xy-where-x-and-y-are-integers-such-that-0--x--2-0--y--3-i-find-the-value-of-the-constant-k-ii-find-the-marginal-probability-distribution-of-x-and-y-iii-show-that-the-random-variables-x-and-y-are-dependent-6-marks)
  - [Q.4 b) Fixed Probability Vector for P2 [7 marks]](#q4-b-find-the-unique-fixed-probability-vector-for-the-matrix-p---01000112120-7-marks)
  - [Q.4 c) Car Trading Problem (Swift, Dzire, Wagnor) [7 marks]](#q4-c-each-year-a-man-trades-his-car-for-a-new-car-in-3-brands-of-the-popular-company-if-he-has-a-swift-he-trades-it-for-dzire-if-he-has-a-dzire-he-trades-it-for-a-wagnor-if-he-has-a-wagnor-he-is-just-as-likely-to-trade-it-for-a-new-wagnor-or-for-a-dzire-or-a-swift-one-in-2020-he-bought-his-first-car-which-was-wagnor-find-the-probability-that-he-has-i-2022-wagnor-ii-2022-swift-iii-2023-dzire-iv-2023-wagnor-7-marks)
- [Paper 2 (June / July 2024)](#paper-2-june--july-2024)
  - [Q.3 a) Joint Table X={2,4,6}, Y={1,3,9} [6 marks]](#q3-a-given-the-following-joint-distribution-of-the-random-variables-x-and-y-find-the-corresponding-marginal-distribution-also-compute-the-covariance-y-1-3-9--x2-18-124-112--x4-14-14-0--x6-18-124-112-6-marks)
  - [Q.3 b) Salesman Territory Problem [7 marks]](#q3-b-a-salesmens-territory-consists-of-3-cities-a-b-and-c-he-never-sells-in-the-same-city-for-2-consecutive-days-if-he-sells-in-city-a-then-the-next-day-he-sells-in-city-b-however-if-he-sells-in-either-b-or-c-then-the-next-day-he-is-twice-as-likely-to-sell-in-city-a-as-in-the-other-city-in-the-long-run-how-often-does-he-sell-in-each-of-the-cities-7-marks)
  - [Q.3 c) Regular Stochastic Matrix and Fixed Vector [7 marks]](#q3-c-show-that-p---01000112120-is-a-regular-stochastic-matrix-also-find-the-associated-unique-fixed-probability-vector-7-marks)
  - [Q.4 a) Definitions: Probability Vector, Regular Stochastic Matrix, Fixed Probability Vector [6 marks]](#q4-a-define-probability-vector-regular-stochastic-matrix-fixed-prob-vector-6-marks)
  - [Q.4 b) Joint PMF f(x,y) = k(2x+y) with P(X >= 1, Y <= 2) [7 marks]](#q4-b-the-joint-probability-distribution-of-two-discrete-random-variables-x-and-y-is-fxy--k2xy-where-x-and-y-are-integers-such-that-0x2-0y3-i-find-the-value-of-the-constant-k-ii-show-that-the-random-variables-x-and-y-are-dependent-iii-find-px--1-y--2-7-marks)
  - [Q.4 c) Fair Coin Tossed Thrice (Joint Distribution of X and Y) [7 marks]](#q4-c-a-fair-coin-is-tossed-thrice-the-random-variables-x-and-y-are-defined-as-x--0-or-1-according-as-head-or-tail-occurs-on-the-first-toss-y--number-of-heads-compute-ex-y--ie-find-exy--joint-distribution--covariance-7-marks)
- [Paper 3 (Dec 2024 / Jan 2025)](#paper-3-dec-2024--jan-2025)
  - [Q.3 a) Joint PMF f(x,y) = (x+y)/30 [7 marks]](#q3-a-if-the-joint-prob-distribution-of-x-and-y-is-given-by-fxy--xy30-for-x--0123--y--012-find-i-px--2-y--1-ii-px--y-7-marks)
  - [Q.3 b) Fixed Probability Vector for P1 (Repeat) [6 marks]](#q3-b-find-the-unique-fixed-probability-vector-of-p---01016121302313-6-marks)
  - [Q.3 c) Three Boys Throwing Ball (B always throws to A variant) [7 marks]](#q3-c-three-boys-a-b-and-c-are-throwing-a-ball-to-each-other-a-always-throw-the-ball-to-b-b-always-throw-the-ball-to-a-and-c-is-just-as-likely-to-throw-the-ball-to-a-as-to-b-find-the-probability-that-c-has-the-ball-after-three-throws-if-c-starts-the-game-7-marks)
  - [Q.4 a) Expectations E(X) and E(Y) for Joint Table 1 (Repeat) [7 marks]](#q4-a-the-joint-prob-distribution-for-the-following-data-find-ex-and-ey-y--2--1-4-5--x1-01-02-00-03--x2-02-01-01-0-7-marks)
  - [Q.4 b) Regular Stochastic Matrix Proof for P3 [6 marks]](#q4-b-show-that-the-matrix-p---00112012010-is-a-regular-stochastic-matrix-6-marks)
  - [Q.4 c) Gambler Luck Pattern [7 marks]](#q4-c-a-gamblers-luck-follows-pattern-if-he-wins-a-game-the-prob-of-winning-the-next-game-is-06-however-if-he-loses-a-game-the-prob-of-losing-the-next-game-is-07-there-is-an-even-chance-of-the-gambler-winning-the-first-game-what-is-the-prob-of-he-winning-the-second-game-7-marks)
- [Paper 4 (June / July 2025)](#paper-4-june--july-2025)
  - [Q.3 a) Definitions: Probability Vector, Regular Stochastic Matrix, Absorbing State [6 marks]](#q3-a-define-i-probability-vector-ii-regular-stochastic-matrix-iii-absorbing-state-of-markov-chain-6-marks)
  - [Q.3 b) Student Study Habits (70% and 60%) [7 marks]](#q3-b-a-students-study-habits-are-as-follows-if-he-studies-one-night-he-is-70-sure-not-to-study-the-next-night-on-the-other-hand-if-he-does-not-study-one-night-he-is-60-sure-not-to-study-the-next-night-in-the-long-run-how-often-does-he-study-7-marks)
  - [Q.3 c) Marginals, Expectations, Covariance for Joint Table 1 (Repeat) [7 marks]](#q3-c-the-joint-probability-distribution-for-two-random-variables-x-and-y-is-given-below-y--2--1-4-5--x1-01-02-0-03--x2-02-01-01-0-determine-i-the-marginal-distribution-of-x-and-y-ii-ex-ey-exy-iii-covx-y-7-marks)
  - [Q.4 a) Fixed Probability Vector for P2 (Repeat) [6 marks]](#q4-a-find-the-fixed-probability-vector-of-the-regular-stochastic-matrix-p---01000112120-6-marks)
  - [Q.4 b) Habitual Gambler Club Visits (A and B) [7 marks]](#q4-b-a-habitual-gambler-is-a-member-of-two-clubs-a-and-b-he-visits-either-of-the-clubs-every-day-for-playing-cards-he-never-visits-club-a-on-two-consecutive-days-but-if-he-visits-club-b-on-a-particular-day-then-the-next-day-he-is-as-likely-to-visit-club-b-or-club-a-if-the-person-had-visited-club-b-on-monday-find-the-probability-that-he-visits-club-a-on-thursday-7-marks)
  - [Q.4 c) Joint PMF f(x,y) = k(2x+y) for 0<=x<=2, 0<=y<=2 [7 marks]](#q4-c-the-joint-probability-distribution-of-two-discrete-random-variable-x-and-y-is-given-by-fx-y--k2xy-where-x-y-are-integers-such-that-0x2-0y2-find-i-k-ii-marginal-probability-distribution-of-x-and-y-iii-px--1-y--2-7-marks)
- [Paper 5 (Makeup)](#paper-5-makeup)
  - [Q.3 a) Joint Table X={1,5}, Y={-4,2,7} [6 marks]](#q3-a-the-joint-distribution-of-two-random-variables-x-and-y-is-as-follows-rows-x-cols-y-y--4-2-7--x1-18-14-18--x5-14-18-18-compute-the-following-ex-ey-exy-covxy-6-marks)
  - [Q.3 b) Irreducible Markov Chain and Stationary Vector [7 marks]](#q3-b-prove-that-the-markov-chain-whose-tpm-is-p---023131201212120-is-irreducible-find-the-corresponding-stationary-probability-vector-7-marks)
  - [Q.3 c) Three Boys Throwing Ball (Prob B has ball after 3 throws) (Repeat) [7 marks]](#q3-c-three-boys-a-b-c-are-throwing-ball-to-each-other-a-always-throws-the-ball-to-b-and-b-always-throws-the-ball-to-c-c-is-just-as-likely-to-throw-the-ball-to-b-as-to-a-if-c-was-the-first-person-to-throw-the-ball-find-the-probabilities-that-after-three-throws-b-has-the-ball-7-marks)
  - [Q.4 a) Definitions: Probability Vector, Stochastic Matrix, Regular Stochastic Matrix [6 marks]](#q4-a-define-i-probability-vector-ii-stochastic-matrix-iii-regular-stochastic-matrix-6-marks)
  - [Q.4 b) Joint PMF f(x,y) = k(2x+y) with Specific Probabilities [7 marks]](#q4-b-the-joint-probability-distribution-of-two-discrete-random-variables-x-and-y-is-given-by-fx-y--k2x--y-where-x-and-y-are-integers-such-that-0x2-0y3-i-find-the-value-of-k-ii-px--1-y--2-iii-px--2-y--1-iv-px--1-y--2-7-marks)
  - [Q.4 c) Transition Matrix P and State Probability Vector P_1^(2) [7 marks]](#q4-c-the-tpm-of-a-markov-chain-is-given-by-p---12012100141214-and-the-initial-probability-distribution-is-p0---12-12-0-find-p_12--px2--1-7-marks)
- [Paper 6 (Dec 2025 / Jan 2026)](#paper-6-dec-2025--jan-2026)
  - [Q.3 a) Joint Table X={1,5}, Y={-4,2,7} Marginals and Covariance (Repeat) [6 marks]](#q3-a-the-joint-probability-distribution-of-two-random-variables-x-and-y-is-rows-x-cols-y-y--4-2-7--x1-18-14-18--x5-14-18-18-i-find-the-marginal-distribution-of-x-and-y-ii-obtain-the-covariance-of-x-and-y-6-marks)
  - [Q.3 b) Fixed Probability Vector for P1 (Repeat) [7 marks]](#q3-b-find-the-unique-fixed-probability-vector-of-p---01016121302313-7-marks)
  - [Q.3 c) Student Study Habits (Repeat) [7 marks]](#q3-c-a-student-study-habit-are-as-follows-if-he-studies-one-night-he-is-70-sure-of-not-studying-next-night-on-the-other-hand-if-he-does-not-study-one-night-he-is-60-sure-not-to-study-the-next-night-in-the-long-run-how-often-does-he-study-7-marks)
  - [Q.4 a) Definitions: Probability Vector, Regular Stochastic Matrix, Absorbing State (Repeat) [6 marks]](#q4-a-define-the-following-i-probability-vector-ii-regular-stochastic-matrix-iii-absorbing-state-6-marks)
  - [Q.4 b) Independent Random Variables X and Y Joint PMF and Covariance [7 marks]](#q4-b-if-x-and-y-are-two-independent-random-variables-with-the-following-distribution-find-the-joint-probability-distribution-of-x-and-y-and-hence-find-the-covariance-x-1-2--fx-07-03--y--2-5-3--gy-03-05-02-7-marks)
  - [Q.4 c) Three Girls Throwing Ball (Repeat with misprint note) [7 marks]](#q4-c-three-girls-a-b-c-are-throwing-the-ball-to-each-other-a-always-throws-the-ball-to-b-b-always-throws-the-ball-to-c-c-is-just-as-likely-to-throw-the-ball-to-b-as-to-c-if-c-was-the-first-person-to-throw-the-ball-find-the-probability-that-after-3-throws-a-b-c-has-the-ball-7-marks)
- [Paper 7 (Model Q-I)](#paper-7-model-q-i)
  - [Q.3 a) Joint Table X={1,2}, Y={-3,2,4} Marginals and Dependence [6 marks]](#q3-a-the-joint-probability-distribution-of-discrete-random-variables-x--y-are-as-follows-rows-x-cols-y-y--3-2-4--x1-01-02-02--x2-03-01-01-then-i-determine-marginal-distribution-of-x--y-ii-show-that-x--y-are-dependent-6-marks)
  - [Q.3 b) Joint PMF f(x,y) = k|x - y| [7 marks]](#q3-b-determine-the-value-of-k-so-that-the-function-fx-y--kx---y-for-x---2-0-2-y---2-3-represents-joint-probability-distribution-of-the-random-variables-x-and-y-also-determine-covx-y-7-marks)
  - [Q.3 c) Three Boys X, Y, Z Ball Throwing (Fourth Throw) [7 marks]](#q3-c-three-boys-x-y-z-are-throwing-a-ball-to-each-other-x-always-throws-the-ball-to-y--y-always-throws-the-ball-to-z-but-z-is-just-as-likely-to-throw-the-ball-to-y-or-as-to-x-write-tpm-if-z-is-the-first-person-to-throw-the-ball-find-the-probability-that-x-has-the-ball-after-fourth-throw-7-marks)
  - [Q.4 a) Joint Table 1 Marginals, Expectations, Covariance, Correlation (Repeat) [6 marks]](#q4-a-given-the-following-joint-distribution-of-the-random-variable-x--y-x1--201--102-40-503--x2--202--101-401-50-determine-the-marginal-probability-distributions-of-x--y-also-compute-i-expectations-of-x-y--xy-ii-covariance-of-x--y-iii-correlation-of-x--y-6-marks)
  - [Q.4 b) Joint Table 2 Marginals, Expectations, Covariance, Correlation (Repeat) [7 marks]](#q4-b-the-joint-probability-distribution-of-random-variables-x--y-are-as-follows-rows-x-cols-y-y--4-2-7--x1-18-14-18--x5-14-18-18-then-determine-i-marginal-distribution-of-x--y-ii-ex-ey--exy-iii-covx-y-iv-rhox-y-7-marks)
  - [Q.4 c) Student Study Habits Variant (60% and 80%, 4th Step) [7 marks]](#q4-c-the-students-study-habits-are-as-follows-if-he-studies-on-one-night-he-is-60-sure-not-to-study-on-next-night-on-the-other-hand-if-he-does-not-study-on-tonight-he-is-80-sure-to-study-next-night-write-the-transition-probability-matrix-for-his-chain-of-study-in-the-long-run-how-often-does-he-study-suppose-he-studies-on-monday-night-what-is-the-probability-that-he-does-not-study-on-friday-night-7-marks)

---

### Paper 1 (Dec 2023 / Jan 2024)

## Q.3 a) The joint probability distribution table for two random variable x and y is as follows: Y: -2, -1, 4, 5 ; X=1: 0.1, 0.2, 0, 0.3 ; X=2: 0.2, 0.1, 0.1, 0. Determine the marginal probability distribution of x and y. Obtain the correlation coefficient between x and y. [6 marks]

**Given:**
Joint probability distribution table p(x,y):
```
       Y = -2    Y = -1    Y = 4    Y = 5
X = 1   0.1       0.2       0        0.3
X = 2   0.2       0.1       0.1      0
```

**Formula / Method:**
1. Marginal distribution of X: P(X = x_i) = f(x_i) = sum_j p(x_i, y_j)
2. Marginal distribution of Y: P(Y = y_j) = g(y_j) = sum_i p(x_i, y_j)
3. Expectations: E(X) = sum x f(x), E(Y) = sum y g(y), E(XY) = sum sum x y p(x,y)
4. Variances: Var(X) = E(X^2) - [E(X)]^2, Var(Y) = E(Y^2) - [E(Y)]^2
5. Covariance: Cov(X,Y) = E(XY) - E(X)E(Y)
6. Correlation coefficient: rho(X,Y) = Cov(X,Y) / (sigma_X * sigma_Y)

**Solution:**

Step 1: Build the table with row sums (marginal distribution of X) and column sums (marginal distribution of Y).

```
       Y = -2    Y = -1    Y = 4    Y = 5    Marginal f(x)
X = 1   0.1       0.2       0        0.3      0.1 + 0.2 + 0 + 0.3 = 0.6
X = 2   0.2       0.1       0.1      0        0.2 + 0.1 + 0.1 + 0 = 0.4
------------------------------------------------------------------
g(y)    0.3       0.3       0.1      0.3      Total sum = 1.0
```

Marginal distribution of X:
- P(X = 1) = f(1) = 0.6 = 3/5
- P(X = 2) = f(2) = 0.4 = 2/5

Marginal distribution of Y:
- P(Y = -2) = g(-2) = 0.3 = 3/10
- P(Y = -1) = g(-1) = 0.3 = 3/10
- P(Y = 4) = g(4) = 0.1 = 1/10
- P(Y = 5) = g(5) = 0.3 = 3/10

Step 2: Compute E(X) and E(X^2).
- E(X) = (1 * 0.6) + (2 * 0.4) = 0.6 + 0.8 = 1.4 = 7/5
- E(X^2) = (1^2 * 0.6) + (2^2 * 0.4) = 0.6 + 1.6 = 2.2 = 11/5
- Var(X) = E(X^2) - [E(X)]^2 = 2.2 - (1.4)^2 = 2.2 - 1.96 = 0.24 = 6/25
- sigma_X = sqrt(0.24)

Step 3: Compute E(Y) and E(Y^2).
- E(Y) = (-2 * 0.3) + (-1 * 0.3) + (4 * 0.1) + (5 * 0.3) = -0.6 - 0.3 + 0.4 + 1.5 = 1.0
- E(Y^2) = ((-2)^2 * 0.3) + ((-1)^2 * 0.3) + (4^2 * 0.1) + (5^2 * 0.3) = (4 * 0.3) + (1 * 0.3) + (16 * 0.1) + (25 * 0.3) = 1.2 + 0.3 + 1.6 + 7.5 = 10.6
- Var(Y) = E(Y^2) - [E(Y)]^2 = 10.6 - (1.0)^2 = 9.6 = 48/5
- sigma_Y = sqrt(9.6)

Step 4: Compute E(XY).
- E(XY) = sum x y p(x,y)
- E(XY) = (1 * -2 * 0.1) + (1 * -1 * 0.2) + (1 * 4 * 0) + (1 * 5 * 0.3) + (2 * -2 * 0.2) + (2 * -1 * 0.1) + (2 * 4 * 0.1) + (2 * 5 * 0)
- E(XY) = -0.2 - 0.2 + 0 + 1.5 - 0.8 - 0.2 + 0.8 + 0 = 0.9 = 9/10

Step 5: Compute Covariance Cov(X,Y).
- Cov(X,Y) = E(XY) - E(X)E(Y) = 0.9 - (1.4 * 1.0) = 0.9 - 1.4 = -0.5 = -1/2

Step 6: Compute Correlation Coefficient rho(X,Y).
- rho(X,Y) = Cov(X,Y) / sqrt(Var(X) * Var(Y)) = -0.5 / sqrt(0.24 * 9.6) = -0.5 / sqrt(2.304) = -0.5 / 1.51789 = -0.3294
- In exact surd form: sqrt(0.24 * 9.6) = sqrt(6/25 * 48/5) = sqrt(288/125) = 12*sqrt(2) / (5*sqrt(5)), so rho = -0.5 / (12*sqrt(2) / (5*sqrt(5))) = -5*sqrt(10) / 48 approx -0.3294

**Answer:**
Marginal of X: **P(X=1) = 0.6, P(X=2) = 0.4**
Marginal of Y: **P(Y=-2) = 0.3, P(Y=-1) = 0.3, P(Y=4) = 0.1, P(Y=5) = 0.3**
Correlation Coefficient: **rho(X,Y) = -0.3294** (or **-5*sqrt(10)/48**)

**Check:** Total marginal probability sum = 0.6 + 0.4 = 1.0, and 0.3 + 0.3 + 0.1 + 0.3 = 1.0.

---

## Q.3 b) Find the unique fixed probability vector for the regular stochastic matrix A = [[0,1,0],[1/6,1/2,1/3],[0,2/3,1/3]]. [7 marks]

**Given:**
Stochastic matrix A = [[0, 1, 0], [1/6, 1/2, 1/3], [0, 2/3, 1/3]]

**Formula / Method:**
1. A probability vector is a row vector t = (a, b, c) where a >= 0, b >= 0, c >= 0 and a + b + c = 1.
2. A fixed probability vector satisfies t A = t.

**Solution:**

Step 1: Let t = (a, b, c) be the unique fixed probability vector such that a + b + c = 1.

Step 2: Write the vector-matrix equation t A = t:
[a, b, c] [[0, 1, 0], [1/6, 1/2, 1/3], [0, 2/3, 1/3]] = [a, b, c]

Step 3: Expand the matrix multiplication column by column to get linear equations:
1. Column 1: 0 * a + (1/6) b + 0 * c = a => a = (1/6) b
2. Column 2: 1 * a + (1/2) b + (2/3) c = b => a - (1/2) b + (2/3) c = 0
3. Column 3: 0 * a + (1/3) b + (1/3) c = c => (1/3) b = (2/3) c => c = (1/2) b

Step 4: Express a and c in terms of b:
- a = (1/6) b
- c = (1/2) b

Step 5: Substitute into the normalization condition a + b + c = 1:
(1/6) b + b + (1/2) b = 1
(1/6 + 1 + 3/6) b = 1
(10/6) b = 1 => (5/3) b = 1 => b = 3/5

Step 6: Compute a and c:
- a = (1/6) * (3/5) = 3/30 = 1/10
- c = (1/2) * (3/5) = 3/10

**Answer:**
Unique fixed probability vector is **t = (1/10, 3/5, 3/10)** (or **t = (0.1, 0.6, 0.3)**)

**Check:**
t A = (1/10, 3/5, 3/10) [[0, 1, 0], [1/6, 1/2, 1/3], [0, 2/3, 1/3]] = (0 + 3/30 + 0, 1/10 + 3/10 + 6/30, 0 + 3/15 + 3/30) = (1/10, 3/5, 3/10) = t. Matches!

---

## Q.3 c) Three boys A, B, C are throwing ball to each other. A always throws the ball to B and B always throws the ball to C. C is just as likely to throw the ball to B as to A. If C was the first person to throw the ball find the probabilities that after three throws : (i) A has the ball. (ii) B has the ball. (iii) C has the ball. [7 marks]

**Given:**
- States: A, B, C (in that order).
- Rules:
  - A always throws to B => Row A = (0, 1, 0)
  - B always throws to C => Row B = (0, 0, 1)
  - C is equally likely to throw to B or A => Row C = (1/2, 1/2, 0)
- C starts the game => initial state probability vector p(0) = (0, 0, 1).

**Formula / Method:**
1. Write the Transition Probability Matrix (TPM) P.
2. State probability vector after n steps: p(n) = p(n-1) P = p(0) P^n.

**Solution:**

Step 1: Write the Transition Probability Matrix P:
P = [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]]

Step 2: Find probability vector after 1st throw (p(1)):
p(1) = p(0) P = [0, 0, 1] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]] = [1/2, 1/2, 0]

Step 3: Find probability vector after 2nd throw (p(2)):
p(2) = p(1) P = [1/2, 1/2, 0] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]]
- First entry: (1/2)(0) + (1/2)(0) + 0(1/2) = 0
- Second entry: (1/2)(1) + (1/2)(0) + 0(1/2) = 1/2
- Third entry: (1/2)(0) + (1/2)(1) + 0(0) = 1/2
p(2) = [0, 1/2, 1/2]

Step 4: Find probability vector after 3rd throw (p(3)):
p(3) = p(2) P = [0, 1/2, 1/2] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]]
- First entry: 0(0) + (1/2)(0) + (1/2)(1/2) = 1/4
- Second entry: 0(1) + (1/2)(0) + (1/2)(1/2) = 1/4
- Third entry: 0(0) + (1/2)(1) + (1/2)(0) = 1/2
p(3) = [1/4, 1/4, 1/2]

**Answer:**
After three throws:
(i) Probability that A has the ball = **1/4**
(ii) Probability that B has the ball = **1/4**
(iii) Probability that C has the ball = **1/2**

**Check:** Total probability = 1/4 + 1/4 + 1/2 = 1.0.

---

## Q.4 a) The joint probability distribution of two discrete random variables x and y is given by f(x, y) = k(2x+y) where x and y are integers. Such that 0 <= x <= 2, 0 <= y <= 3. (i) Find the value of the constant K. (ii) Find the marginal probability distribution of X and Y. (iii) Show that the random variables X and Y are dependent. [6 marks]

**Given:**
f(x,y) = k(2x+y) for x in {0, 1, 2} and y in {0, 1, 2, 3}.

**Formula / Method:**
1. Sum of all joint probabilities must equal 1: sum_{x=0}^2 sum_{y=0}^3 f(x,y) = 1.
2. Marginal distribution P(X=x) = f(x) = sum_{y=0}^3 f(x,y) and P(Y=y) = g(y) = sum_{x=0}^2 f(x,y).
3. Random variables X and Y are independent if f(x,y) = P(X=x) * P(Y=y) for all x,y. If f(x,y) != P(X=x) * P(Y=y) for even one cell, they are dependent.

**Solution:**

Step 1: Compute values of (2x+y) for each cell (x,y):
- For x = 0:
  - y=0 => 2(0)+0 = 0
  - y=1 => 2(0)+1 = 1
  - y=2 => 2(0)+2 = 2
  - y=3 => 2(0)+3 = 3
  - Sum for x=0 is 0 + 1 + 2 + 3 = 6.

- For x = 1:
  - y=0 => 2(1)+0 = 2
  - y=1 => 2(1)+1 = 3
  - y=2 => 2(1)+2 = 4
  - y=3 => 2(1)+3 = 5
  - Sum for x=1 is 2 + 3 + 4 + 5 = 14.

- For x = 2:
  - y=0 => 2(2)+0 = 4
  - y=1 => 2(2)+1 = 5
  - y=2 => 2(2)+2 = 6
  - y=3 => 2(2)+3 = 7
  - Sum for x=2 is 4 + 5 + 6 + 7 = 22.

Total sum = 6 + 14 + 22 = 42.
Since sum_{x} sum_{y} f(x,y) = 42k = 1 => k = 1/42.

Step 2: Construct the joint probability table with marginals:

```
        Y = 0     Y = 1     Y = 2     Y = 3     Marginal P(X=x)
X = 0   0/42      1/42      2/42      3/42      6/42 = 1/7
X = 1   2/42      3/42      4/42      5/42      14/42 = 1/3
X = 2   4/42      5/42      6/42      7/42      22/42 = 11/21
--------------------------------------------------------------
P(Y=y)  6/42=1/7  9/42=3/14 12/42=2/7 15/42=5/14 Total = 1.0
```

Marginal distribution of X:
- P(X=0) = 1/7
- P(X=1) = 1/3
- P(X=2) = 11/21

Marginal distribution of Y:
- P(Y=0) = 1/7
- P(Y=1) = 3/14
- P(Y=2) = 2/7
- P(Y=3) = 5/14

Step 3: Test for independence at cell (x=0, y=0):
- f(0,0) = 0
- P(X=0) * P(Y=0) = (1/7) * (1/7) = 1/49
- Since f(0,0) = 0 != 1/49 = P(X=0) P(Y=0), X and Y are dependent random variables.

**Answer:**
(i) **k = 1/42**
(ii) Marginal of X: **P(X=0) = 1/7, P(X=1) = 1/3, P(X=2) = 11/21**
     Marginal of Y: **P(Y=0) = 1/7, P(Y=1) = 3/14, P(Y=2) = 2/7, P(Y=3) = 5/14**
(iii) **X and Y are dependent because f(0,0) = 0 != P(X=0)P(Y=0) = 1/49**.

**Check:** Total probabilities sum to 1/7 + 1/3 + 11/21 = (3 + 7 + 11)/21 = 21/21 = 1.0.

---

## Q.4 b) Find the unique fixed probability vector for the matrix P = [[0,1,0],[0,0,1],[1/2,1/2,0]]. [7 marks]

**Given:**
P = [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]]

**Formula / Method:**
Let t = (a, b, c) be a fixed probability vector such that t P = t and a + b + c = 1.

**Solution:**

Step 1: Write t P = t:
[a, b, c] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]] = [a, b, c]

Step 2: Equate column components:
1. Column 1: 0 * a + 0 * b + (1/2) c = a => a = (1/2) c
2. Column 2: 1 * a + 0 * b + (1/2) c = b => b = a + (1/2) c = (1/2) c + (1/2) c = c
3. Column 3: 0 * a + 1 * b + 0 * c = c => b = c

Step 3: Express a and b in terms of c:
- a = (1/2) c
- b = c

Step 4: Substitute into a + b + c = 1:
(1/2) c + c + c = 1 => (5/2) c = 1 => c = 2/5

Step 5: Calculate a and b:
- a = (1/2) * (2/5) = 1/5
- b = 2/5

**Answer:**
Unique fixed probability vector is **t = (1/5, 2/5, 2/5)** (or **t = (0.2, 0.4, 0.4)**)

**Check:**
t P = (1/5, 2/5, 2/5) [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]] = (2/10, 1/5 + 2/10, 2/5) = (1/5, 2/5, 2/5) = t. Matches!

---

## Q.4 c) Each year a man trades his car for a new car in 3 brands of the popular company. If he has a 'swift' he trades it for 'Dzire'. If he has a 'Dzire' he trades it for a 'Wagnor'. If he has a 'Wagnor' he is just as likely to trade it for a new 'Wagnor' or for a 'Dzire' or a 'Swift' one. In 2020 he bought his first car which was 'Wagnor'. Find the probability that he has (i) 2022 Wagnor. (ii) 2022 Swift. (iii) 2023 Dzire. (iv) 2023 Wagnor. [7 marks]

**Given:**
- States: 1: Swift, 2: Dzire, 3: Wagnor.
- Rules:
  - Swift => Dzire: row 1 = (0, 1, 0)
  - Dzire => Wagnor: row 2 = (0, 0, 1)
  - Wagnor => equal chance (1/3 each): row 3 = (1/3, 1/3, 1/3)
- Initial state in 2020: Wagnor => p(2020) = p(0) = (0, 0, 1).

**Formula / Method:**
p(n) = p(n-1) P, where 2021 is n=1, 2022 is n=2, and 2023 is n=3.

**Solution:**

Step 1: Write the Transition Probability Matrix P:
P = [[0, 1, 0], [0, 0, 1], [1/3, 1/3, 1/3]]

Step 2: Calculate state vector for 2021 (n=1 step):
p(1) = p(0) P = [0, 0, 1] [[0, 1, 0], [0, 0, 1], [1/3, 1/3, 1/3]] = [1/3, 1/3, 1/3]

Step 3: Calculate state vector for 2022 (n=2 steps):
p(2) = p(1) P = [1/3, 1/3, 1/3] [[0, 1, 0], [0, 0, 1], [1/3, 1/3, 1/3]]
- First entry (Swift): (1/3)(0) + (1/3)(0) + (1/3)(1/3) = 1/9
- Second entry (Dzire): (1/3)(1) + (1/3)(0) + (1/3)(1/3) = 1/3 + 1/9 = 4/9
- Third entry (Wagnor): (1/3)(0) + (1/3)(1) + (1/3)(1/3) = 1/3 + 1/9 = 4/9
p(2) = [1/9, 4/9, 4/9]

Step 4: Calculate state vector for 2023 (n=3 steps):
p(3) = p(2) P = [1/9, 4/9, 4/9] [[0, 1, 0], [0, 0, 1], [1/3, 1/3, 1/3]]
- First entry (Swift): (1/9)(0) + (4/9)(0) + (4/9)(1/3) = 4/27
- Second entry (Dzire): (1/9)(1) + (4/9)(0) + (4/9)(1/3) = 1/9 + 4/27 = 7/27
- Third entry (Wagnor): (1/9)(0) + (4/9)(1) + (4/9)(1/3) = 4/9 + 4/27 = 16/27
p(3) = [4/27, 7/27, 16/27]

**Answer:**
(i) Probability of 2022 Wagnor = **4/9**
(ii) Probability of 2022 Swift = **1/9**
(iii) Probability of 2023 Dzire = **7/27**
(iv) Probability of 2023 Wagnor = **16/27**

**Check:** Total probabilities for p(2) = 1/9 + 4/9 + 4/9 = 1.0, p(3) = 4/27 + 7/27 + 16/27 = 27/27 = 1.0.

---

### Paper 2 (June / July 2024)

## Q.3 a) Given the following joint distribution of the random variables X and Y. Find the corresponding marginal distribution. Also compute the covariance. Y: 1, 3, 9 ; X=2: 1/8, 1/24, 1/12 ; X=4: 1/4, 1/4, 0 ; X=6: 1/8, 1/24, 1/12. [6 marks]

**Given:**
Joint distribution table:
```
       Y = 1    Y = 3    Y = 9
X = 2   1/8      1/24     1/12
X = 4   1/4      1/4      0
X = 6   1/8      1/24     1/12
```

**Formula / Method:**
1. Marginal distribution of X: f(x_i) = sum_j p(x_i, y_j)
2. Marginal distribution of Y: g(y_j) = sum_i p(x_i, y_j)
3. E(X) = sum x f(x), E(Y) = sum y g(y), E(XY) = sum sum x y p(x,y)
4. Cov(X,Y) = E(XY) - E(X)E(Y)

**Solution:**

Step 1: Compute marginal distributions (row sums and column sums):
- Row X = 2: 1/8 + 1/24 + 1/12 = (3 + 1 + 2)/24 = 6/24 = 1/4
- Row X = 4: 1/4 + 1/4 + 0 = 2/4 = 1/2
- Row X = 6: 1/8 + 1/24 + 1/12 = 6/24 = 1/4

- Column Y = 1: 1/8 + 1/4 + 1/8 = 1/2
- Column Y = 3: 1/24 + 1/4 + 1/24 = 2/24 + 1/4 = 1/12 + 3/12 = 4/12 = 1/3
- Column Y = 9: 1/12 + 0 + 1/12 = 2/12 = 1/6

Joint distribution table with marginals:
```
        Y = 1    Y = 3    Y = 9    Marginal f(x)
X = 2    1/8      1/24     1/12     1/4
X = 4    1/4      1/4      0        1/2
X = 6    1/8      1/24     1/12     1/4
----------------------------------------------
g(y)     1/2      1/3      1/6      Total = 1.0
```

Marginal of X:
- P(X=2) = 1/4
- P(X=4) = 1/2
- P(X=6) = 1/4

Marginal of Y:
- P(Y=1) = 1/2
- P(Y=3) = 1/3
- P(Y=9) = 1/6

Step 2: Compute E(X):
- E(X) = (2 * 1/4) + (4 * 1/2) + (6 * 1/4) = 1/2 + 2 + 3/2 = 4

Step 3: Compute E(Y):
- E(Y) = (1 * 1/2) + (3 * 1/3) + (9 * 1/6) = 1/2 + 1 + 3/2 = 3

Step 4: Compute E(XY):
- E(XY) = (2 * 1 * 1/8) + (2 * 3 * 1/24) + (2 * 9 * 1/12) + (4 * 1 * 1/4) + (4 * 3 * 1/4) + (4 * 9 * 0) + (6 * 1 * 1/8) + (6 * 3 * 1/24) + (6 * 9 * 1/12)
- E(XY) = 2/8 + 6/24 + 18/12 + 4/4 + 12/4 + 0 + 6/8 + 18/24 + 54/12
- E(XY) = 1/4 + 1/4 + 3/2 + 1 + 3 + 0 + 3/4 + 3/4 + 9/2
- Summing terms:
  - 1/4 + 1/4 + 3/4 + 3/4 = 8/4 = 2
  - 3/2 + 9/2 = 12/2 = 6
  - 1 + 3 = 4
  - Total E(XY) = 2 + 6 + 4 = 12

Step 5: Compute Covariance:
- Cov(X,Y) = E(XY) - E(X)E(Y) = 12 - (4 * 3) = 12 - 12 = 0

**Answer:**
Marginal of X: **P(X=2) = 1/4, P(X=4) = 1/2, P(X=6) = 1/4**
Marginal of Y: **P(Y=1) = 1/2, P(Y=3) = 1/3, P(Y=9) = 1/6**
Covariance: **Cov(X,Y) = 0**

**Check:** Total marginal probability sum = 1/4 + 1/2 + 1/4 = 1.0 and 1/2 + 1/3 + 1/6 = 1.0.

---

## Q.3 b) A salesmen's territory consists of 3 cities A, B and C. He never sells in the same city for 2 consecutive days. If he sells in city A, then the next day he sells in city B. However if he sells in either B or C then the next day he is twice as likely to sell in city A as in the other city. In the long run how often does he sell in each of the cities. [7 marks]

**Given:**
- States: 1: City A, 2: City B, 3: City C.
- Rules:
  - From A: Always sells in B => Row A = (0, 1, 0)
  - From B: Never B, twice as likely A as C. Let prob of C be x, then prob of A is 2x. So 2x + x = 1 => x = 1/3. Thus Row B = (2/3, 0, 1/3)
  - From C: Never C, twice as likely A as B. Row C = (2/3, 1/3, 0)

**Formula / Method:**
Solve t P = t with t = (a, b, c) and a + b + c = 1.

**Solution:**

Step 1: Write the Transition Probability Matrix P:
P = [[0, 1, 0], [2/3, 0, 1/3], [2/3, 1/3, 0]]

Step 2: Set up equations t P = t:
[a, b, c] [[0, 1, 0], [2/3, 0, 1/3], [2/3, 1/3, 0]] = [a, b, c]

Step 3: Expand matrix multiplication:
1. Column 1: 0 * a + (2/3) b + (2/3) c = a => a = (2/3)(b + c)
2. Column 2: 1 * a + 0 * b + (1/3) c = b => b = a + (1/3) c
3. Column 3: 0 * a + (1/3) b + 0 * c = c => c = (1/3) b => b = 3c

Step 4: Express a, b, c in terms of c:
- Since b = 3c:
- a = (2/3)(3c + c) = (2/3)(4c) = (8/3) c

Step 5: Substitute into normalization condition a + b + c = 1:
(8/3) c + 3c + c = 1
(8/3 + 4) c = 1 => (20/3) c = 1 => c = 3/20

Step 6: Compute a and b:
- b = 3 * (3/20) = 9/20
- a = (8/3) * (3/20) = 8/20 = 2/5

**Answer:**
In the long run, he sells:
In City A: **2/5 = 40%** of the time.
In City B: **9/20 = 45%** of the time.
In City C: **3/20 = 15%** of the time.

**Check:**
a + b + c = 8/20 + 9/20 + 3/20 = 20/20 = 1.0.
t P = (8/20, 9/20, 3/20) [[0, 1, 0], [2/3, 0, 1/3], [2/3, 1/3, 0]] = (6/20 + 2/20, 8/20 + 1/20, 3/20) = (8/20, 9/20, 3/20) = t. Matches!

---

## Q.3 c) Show that P = [[0,1,0],[0,0,1],[1/2,1/2,0]] is a regular stochastic matrix. Also find the associated unique fixed probability vector. [7 marks]

**Given:**
P = [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]]

**Formula / Method:**
1. A stochastic matrix is regular if some power P^n contains only strictly positive entries (p_{ij}^{(n)} > 0 for all i,j).
2. Unique fixed probability vector satisfies t P = t and a + b + c = 1.

**Solution:**

Step 1: Compute powers of P to test for regularity:
P^2 = [[0, 0, 1], [1/2, 1/2, 0], [0, 1/2, 1/2]]
P^3 = [[1/2, 1/2, 0], [0, 1/2, 1/2], [1/4, 1/4, 1/2]]
P^4 = [[0, 1/2, 1/2], [1/4, 1/4, 1/2], [1/4, 1/2, 1/4]]
P^5 = [[1/4, 1/4, 1/2], [1/4, 1/2, 1/4], [1/8, 3/8, 1/2]]

Since all entries in P^5 are strictly positive (p_{ij}^{(5)} > 0 for all i,j), P is a **regular stochastic matrix**.

Step 2: Find unique fixed probability vector t = (a,b,c):
t P = t => [a, b, c] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]] = [a, b, c]
- (1/2) c = a => c = 2a
- a + (1/2) c = b => b = a + a = 2a
- b = c => b = 2a

Substitute into a + b + c = 1:
a + 2a + 2a = 1 => 5a = 1 => a = 1/5
Hence b = 2/5 and c = 2/5.

**Answer:**
**P^5 has all positive entries, so P is regular.**
Unique fixed probability vector: **t = (1/5, 2/5, 2/5)**

---

## Q.4 a) Define probability vector, regular stochastic matrix, fixed prob vector. [6 marks]

**Given:** Theory question on Markov Chain definitions.

**Formula / Method:** Definitions with 2 simple lines and tiny examples.

**Solution:**

1. **Probability Vector:**
   - A row vector u = (u_1, u_2, ..., u_n) with non-negative components (u_i >= 0) whose sum equals 1, i.e., sum u_i = 1.
   - Example: u = (0.3, 0.7) is a probability vector since 0.3 + 0.7 = 1.

2. **Stochastic Matrix:**
   - A square matrix P where every element is non-negative (p_{ij} >= 0) and the sum of elements in each row equals 1.
   - Example: P = [[0.4, 0.6], [0.2, 0.8]] is a stochastic matrix.

3. **Regular Stochastic Matrix:**
   - A stochastic matrix P is called regular if some positive integer power P^n contains only strictly positive entries (no zero entries).
   - Example: P = [[0, 1], [0.5, 0.5]] is regular because P^2 = [[0.5, 0.5], [0.25, 0.75]] has all positive entries.

4. **Fixed Probability Vector (Stationary Vector):**
   - A probability vector t is called a fixed probability vector of a stochastic matrix P if t P = t.
   - Example: For P = [[0.5, 0.5], [0.5, 0.5]], t = (0.5, 0.5) satisfies t P = (0.5, 0.5) = t.

**Answer:**
See definitions and examples above.

---

## Q.4 b) The joint probability distribution of two discrete random variables X and Y is f(x,y) = k(2x+y), where x and y are integers such that 0<=x<=2, 0<=y<=3. i) Find the value of the constant k. ii) Show that the random variables X and Y are dependent iii) Find P(X >= 1, Y <= 2). [7 marks]

**Given:**
f(x,y) = k(2x+y) for x in {0,1,2}, y in {0,1,2,3}.

**Formula / Method:**
Same joint PMF table as Paper 1 Q.4 a).
Part (iii): P(X >= 1, Y <= 2) = sum_{x=1}^2 sum_{y=0}^2 f(x,y).

**Solution:**

Step 1: From Paper 1 Q.4 a), sum_{x=0}^2 sum_{y=0}^3 (2x+y) = 42 => k = 1/42.

Step 2: Table of probabilities f(x,y) = (2x+y)/42:
```
        Y = 0    Y = 1    Y = 2    Y = 3    Marginal P(X=x)
X = 0   0/42     1/42     2/42     3/42     6/42 = 1/7
X = 1   2/42     3/42     4/42     5/42     14/42 = 1/3
X = 2   4/42     5/42     6/42     7/42     22/42 = 11/21
------------------------------------------------------------
P(Y=y)  1/7      3/14     2/7      5/14     Total = 1.0
```

Step 3: Show dependence:
f(0,0) = 0, but P(X=0)P(Y=0) = (1/7) * (1/7) = 1/49 != 0. Thus X and Y are dependent.

Step 4: Compute P(X >= 1, Y <= 2):
Sum values for x in {1, 2} and y in {0, 1, 2}:
- For x=1, y=0: 2/42
- For x=1, y=1: 3/42
- For x=1, y=2: 4/42
- For x=2, y=0: 4/42
- For x=2, y=1: 5/42
- For x=2, y=2: 6/42

Sum = (2 + 3 + 4 + 4 + 5 + 6)/42 = 24/42 = 4/7.

**Answer:**
(i) **k = 1/42**
(ii) **X and Y are dependent since f(0,0) = 0 != P(X=0)P(Y=0) = 1/49.**
(iii) **P(X >= 1, Y <= 2) = 24/42 = 4/7**

**Check:** 24/42 = 4/7.

---

## Q.4 c) A fair coin is tossed thrice. The random variables X and Y are defined as X = 0 or 1 according as head or tail occurs on the first toss, Y = number of heads. Compute E(X, Y) [i.e. find E(XY) / joint distribution / covariance]. [7 marks]

**Given:**
Experiment: Fair coin tossed 3 times. Sample space S has 2^3 = 8 equally likely outcomes, each with probability 1/8:
S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}
- Random variable X = 0 if Head on 1st toss, X = 1 if Tail on 1st toss.
- Random variable Y = total number of heads in 3 tosses.

**Formula / Method:**
1. List sample space outcomes and assign (X, Y) values to each.
2. Build joint probability table p(x,y).
3. Compute E(X), E(Y), E(XY), and Cov(X,Y) = E(XY) - E(X)E(Y).

**Solution:**

Step 1: Map all 8 outcomes to (X, Y) values:
1. HHH => X=0, Y=3 => P(0,3) = 1/8
2. HHT => X=0, Y=2 => P(0,2) = 1/8
3. HTH => X=0, Y=2 => P(0,2) total = 2/8
4. HTT => X=0, Y=1 => P(0,1) = 1/8
5. THH => X=1, Y=2 => P(1,2) = 1/8
6. THT => X=1, Y=1 => P(1,1) = 1/8
7. TTH => X=1, Y=1 => P(1,1) total = 2/8
8. TTT => X=1, Y=0 => P(1,0) = 1/8

Step 2: Construct the Joint Probability Distribution Table:

```
        Y = 0     Y = 1     Y = 2     Y = 3     Marginal P(X=x)
X = 0   0         1/8       2/8       1/8       4/8 = 1/2
X = 1   1/8       2/8       1/8       0         4/8 = 1/2
------------------------------------------------------------
P(Y=y)  1/8       3/8       3/8       1/8       Total = 1.0
```

Marginals:
- P(X=0) = 1/2, P(X=1) = 1/2
- P(Y=0) = 1/8, P(Y=1) = 3/8, P(Y=2) = 3/8, P(Y=3) = 1/8

Step 3: Compute E(X) and E(Y):
- E(X) = (0 * 1/2) + (1 * 1/2) = 1/2
- E(Y) = (0 * 1/8) + (1 * 3/8) + (2 * 3/8) + (3 * 1/8) = (0 + 3 + 6 + 3)/8 = 12/8 = 3/2

Step 4: Compute E(XY):
- E(XY) = sum x y p(x,y)
- For x=0, x y p(x,y) = 0.
- For x=1:
  - 1 * 0 * (1/8) = 0
  - 1 * 1 * (2/8) = 2/8
  - 1 * 2 * (1/8) = 2/8
  - 1 * 3 * 0 = 0
- E(XY) = 2/8 + 2/8 = 4/8 = 1/2

Step 5: Compute Covariance Cov(X,Y):
- Cov(X,Y) = E(XY) - E(X)E(Y) = 1/2 - (1/2 * 3/2) = 1/2 - 3/4 = -1/4

**Answer:**
Joint distribution table as given above.
Expectation: **E(XY) = 1/2**
Covariance: **Cov(X,Y) = -1/4**

**Check:** Total marginal sum = 1/2 + 1/2 = 1.0 and 1/8 + 3/8 + 3/8 + 1/8 = 1.0.

---

### Paper 3 (Dec 2024 / Jan 2025)

## Q.3 a) If the joint prob. distribution of x and y is given by f(x,y) = (x+y)/30 for x = 0,1,2,3 ; y = 0,1,2. Find (i) P(x <= 2, y = 1) (ii) P(x > y) [7 marks]

**Given:**
f(x,y) = (x+y)/30 for x in {0, 1, 2, 3}, y in {0, 1, 2}.

**Formula / Method:**
1. Check sum = 1: sum_{x=0}^3 sum_{y=0}^2 (x+y)/30 = 1.
2. List individual probabilities and sum appropriate cells.

**Solution:**

Step 1: Build full joint probability table f(x,y) = (x+y)/30:
```
        Y = 0     Y = 1     Y = 2     Marginal P(X=x)
X = 0   0/30      1/30      2/30      3/30
X = 1   1/30      2/30      3/30      6/30
X = 2   2/30      3/30      4/30      9/30
X = 3   3/30      4/30      5/30      12/30
---------------------------------------------------
P(Y=y)  6/30      10/30     14/30     Total = 30/30 = 1.0
```

Step 2: Find (i) P(X <= 2, Y = 1):
Sum for x in {0, 1, 2} at y = 1:
P(X <= 2, Y = 1) = f(0,1) + f(1,1) + f(2,1) = 1/30 + 2/30 + 3/30 = 6/30 = 1/5

Step 3: Find (ii) P(X > Y):
List all pairs (x,y) where x > y:
- (1,0) => f(1,0) = 1/30
- (2,0) => f(2,0) = 2/30
- (2,1) => f(2,1) = 3/30
- (3,0) => f(3,0) = 3/30
- (3,1) => f(3,1) = 4/30
- (3,2) => f(3,2) = 5/30

Sum = (1 + 2 + 3 + 3 + 4 + 5)/30 = 18/30 = 3/5.

**Answer:**
(i) **P(x <= 2, y = 1) = 6/30 = 1/5**
(ii) **P(x > y) = 18/30 = 3/5**

**Check:** Total table sum = (3+6+9+12)/30 = 30/30 = 1.0.

---

## Q.3 b) Find the unique fixed probability vector of P = [[0,1,0],[1/6,1/2,1/3],[0,2/3,1/3]]. [6 marks]

Same as Q.3 b) of Paper 1 above, answer: **unique fixed probability vector is t = (1/10, 3/5, 3/10)**.

---

## Q.3 c) Three boys A, B and C are throwing a ball to each other. A always throw the ball to B. B always throw the ball to A and C is just as likely to throw the ball to A as to B. Find the probability that C has the ball after three throws, if C starts the game. [7 marks]

**Given:**
- States: A, B, C.
- Rules (as printed):
  - A always throws to B => Row A = (0, 1, 0)
  - B always throws to A => Row B = (1, 0, 0)
  - C throws to A or B with equal probability => Row C = (1/2, 1/2, 0)
- C starts the game => p(0) = (0, 0, 1).

**Formula / Method:**
p(n) = p(n-1) P.

**Solution:**

Step 1: Write Transition Probability Matrix P:
P = [[0, 1, 0], [1, 0, 0], [1/2, 1/2, 0]]

Step 2: Calculate p(1) after 1st throw:
p(1) = p(0) P = [0, 0, 1] [[0, 1, 0], [1, 0, 0], [1/2, 1/2, 0]] = [1/2, 1/2, 0]

Step 3: Calculate p(2) after 2nd throw:
p(2) = p(1) P = [1/2, 1/2, 0] [[0, 1, 0], [1, 0, 0], [1/2, 1/2, 0]]
- Entry 1 (A): (1/2)(0) + (1/2)(1) + 0(1/2) = 1/2
- Entry 2 (B): (1/2)(1) + (1/2)(0) + 0(1/2) = 1/2
- Entry 3 (C): (1/2)(0) + (1/2)(0) + 0(0) = 0
p(2) = [1/2, 1/2, 0]

Step 4: Calculate p(3) after 3rd throw:
p(3) = p(2) P = [1/2, 1/2, 0] [[0, 1, 0], [1, 0, 0], [1/2, 1/2, 0]] = [1/2, 1/2, 0]

**Answer:**
Note: Solved using exact paper text where B always throws to A.
Probability vector after 3 throws: **p(3) = (1/2, 1/2, 0)**
Probability that C has the ball after three throws = **0**

---

## Q.4 a) The joint prob. distribution for the following data, find E(x) and E(y). Y: -2, -1, 4, 5 ; X=1: 0.1, 0.2, 0.0, 0.3 ; X=2: 0.2, 0.1, 0.1, 0. [7 marks]

Same joint distribution table as Q.3 a) of Paper 1 above, answer: **E(X) = 7/5 = 1.4, E(Y) = 1**.

---

## Q.4 b) Show that the matrix P = [[0,0,1],[1/2,0,1/2],[0,1,0]] is a regular stochastic matrix. [6 marks]

**Given:**
P = [[0, 0, 1], [1/2, 0, 1/2], [0, 1, 0]]

**Formula / Method:**
Compute powers P^2, P^3, P^4, P^5, ... until all matrix entries are strictly positive (p_{ij}^{(n)} > 0).

**Solution:**

Step 1: Compute P^2:
P^2 = [[0, 1, 0], [0, 1/2, 1/2], [1/2, 0, 1/2]]

Step 2: Compute P^3:
P^3 = P^2 P = [[1/2, 0, 1/2], [1/4, 1/2, 1/4], [0, 1/2, 1/2]]

Step 3: Compute P^4:
P^4 = P^3 P = [[0, 1/2, 1/2], [1/4, 1/4, 1/2], [1/4, 1/2, 1/4]]

Step 4: Compute P^5:
P^5 = P^4 P = [[1/4, 1/2, 1/4], [1/8, 1/2, 3/8], [1/4, 1/4, 1/2]]

Since all entries of P^5 are strictly positive (p_{ij}^{(5)} > 0 for all i,j), P is a **regular stochastic matrix**.

**Answer:**
**P^5 has all positive entries, hence P is a regular stochastic matrix.**

---

## Q.4 c) A gambler's luck follows pattern. If he wins a game the prob. of winning the next game is 0.6. However, if he loses a game, the prob. of losing the next game is 0.7. There is an even chance of the gambler winning the first game. What is the prob. of he winning the second game. [7 marks]

**Given:**
- States: 1: Win (W), 2: Lose (L).
- From W: P(W -> W) = 0.6 => P(W -> L) = 0.4. Row W = (0.6, 0.4).
- From L: P(L -> L) = 0.7 => P(L -> W) = 0.3. Row L = (0.3, 0.7).
- Initial probability vector (Game 1): even chance => p(1) = (0.5, 0.5).

**Formula / Method:**
Distribution for Game 2: p(2) = p(1) P.

**Solution:**

Step 1: Write the Transition Probability Matrix P:
P = [[0.6, 0.4], [0.3, 0.7]] = [[3/5, 2/5], [3/10, 7/10]]

Step 2: Calculate p(2) for the second game:
p(2) = p(1) P = [0.5, 0.5] [[0.6, 0.4], [0.3, 0.7]]
- Probability of winning 2nd game: 0.5(0.6) + 0.5(0.3) = 0.30 + 0.15 = 0.45 = 9/20
- Probability of losing 2nd game: 0.5(0.4) + 0.5(0.7) = 0.20 + 0.35 = 0.55 = 11/20

p(2) = [0.45, 0.55]

**Answer:**
Probability of winning the second game = **0.45** (or **9/20**)

**Check:** 0.45 + 0.55 = 1.0.

---

### Paper 4 (June / July 2025)

## Q.3 a) Define (i) Probability vector (ii) Regular stochastic matrix (iii) Absorbing state of Markov chain. [6 marks]

**Given:** Theory question on Markov Chain definitions.

**Solution:**

1. **Probability Vector:**
   - A non-negative row vector u = (u_1, u_2, ..., u_n) where u_i >= 0 and sum u_i = 1.
   - Example: u = (0.4, 0.6) is a probability vector.

2. **Regular Stochastic Matrix:**
   - A square matrix P with non-negative entries where each row sums to 1, such that some power P^n has all strictly positive entries.
   - Example: P = [[0, 1], [0.5, 0.5]] is regular because P^2 = [[0.5, 0.5], [0.25, 0.75]] > 0.

3. **Absorbing State:**
   - A state i in a Markov chain is called an absorbing state if once entered, it cannot be left, i.e., p_{ii} = 1 and p_{ij} = 0 for all j != i.
   - Example: Row i = (0, 1, 0) for state 2 means state 2 is absorbing.

**Answer:**
See definitions and examples above.

---

## Q.3 b) A students study habits are as follows: If he studies one night, he is 70% sure not to study the next night. On the other hand if he does not study one night, he is 60% sure not to study the next night. In the long run how often does he study? [7 marks]

**Given:**
- States: 1: Studies (S), 2: Does not study (N).
- Rules:
  - From S: 70% sure not to study => P(S -> N) = 0.7, P(S -> S) = 0.3. Row S = (0.3, 0.7).
  - From N: 60% sure not to study => P(N -> N) = 0.6, P(N -> S) = 0.4. Row N = (0.4, 0.6).

**Formula / Method:**
Solve fixed probability vector t P = t with t = (a, b) and a + b = 1.

**Solution:**

Step 1: Write Transition Probability Matrix P:
P = [[0.3, 0.7], [0.4, 0.6]] = [[3/10, 7/10], [4/10, 6/10]]

Step 2: Set up t P = t:
[a, b] [[0.3, 0.7], [0.4, 0.6]] = [a, b]

Step 3: Write equations:
- 0.3 a + 0.4 b = a => 0.4 b = 0.7 a => b = (7/4) a
- 0.7 a + 0.6 b = b => 0.7 a = 0.4 b => b = (7/4) a

Step 4: Substitute into a + b = 1:
a + (7/4) a = 1 => (11/4) a = 1 => a = 4/11
b = (7/4) * (4/11) = 7/11

**Answer:**
In the long run, he studies **4/11** of the time (approx **36.36%** of nights).

**Check:** a + b = 4/11 + 7/11 = 11/11 = 1.0.

---

## Q.3 c) The joint probability distribution for two random variables X and Y is given below: Y: -2, -1, 4, 5 ; X=1: 0.1, 0.2, 0, 0.3 ; X=2: 0.2, 0.1, 0.1, 0. Determine: (i) The marginal distribution of X and Y. (ii) E[X], E[Y], E[XY] (iii) COV(X, Y) [7 marks]

Same joint distribution table as Q.3 a) of Paper 1 above, answer: **Marginals P(X=1)=3/5, P(X=2)=2/5; P(Y=-2)=3/10, P(Y=-1)=3/10, P(Y=4)=1/10, P(Y=5)=3/10; E(X) = 7/5, E(Y) = 1, E(XY) = 9/10, Cov(X,Y) = -1/2**.

---

## Q.4 a) Find the fixed probability vector of the regular stochastic matrix P = [[0,1,0],[0,0,1],[1/2,1/2,0]]. [6 marks]

Same as Q.4 b) of Paper 1 above, answer: **unique fixed probability vector is t = (1/5, 2/5, 2/5)**.

---

## Q.4 b) A habitual gambler is a member of two clubs A and B. He visits either of the clubs every day for playing cards. He never visits club A on two consecutive days. But if he visits club B on a particular day then the next day he is as likely to visit club B or club A. If the person had visited club B on Monday, find the probability that he visits club A on Thursday. [7 marks]

**Given:**
- States: 1: Club A, 2: Club B.
- Rules:
  - From A: Never visits A on consecutive days => P(A -> B) = 1, P(A -> A) = 0. Row A = (0, 1).
  - From B: Equally likely A or B => P(B -> A) = 0.5, P(B -> B) = 0.5. Row B = (0.5, 0.5).
- Initial state on Monday (n=0): Club B => p(0) = (0, 1).
- Steps to Thursday: Monday (n=0), Tuesday (n=1), Wednesday (n=2), Thursday (n=3).

**Formula / Method:**
p(3) = p(0) P^3.

**Solution:**

Step 1: Write Transition Probability Matrix P:
P = [[0, 1], [1/2, 1/2]]

Step 2: Calculate p(1) for Tuesday:
p(1) = p(0) P = [0, 1] [[0, 1], [1/2, 1/2]] = [1/2, 1/2]

Step 3: Calculate p(2) for Wednesday:
p(2) = p(1) P = [1/2, 1/2] [[0, 1], [1/2, 1/2]] = [1/4, 3/4]

Step 4: Calculate p(3) for Thursday:
p(3) = p(2) P = [1/4, 3/4] [[0, 1], [1/2, 1/2]]
- Entry 1 (Club A): (1/4)(0) + (3/4)(1/2) = 3/8
- Entry 2 (Club B): (1/4)(1) + (3/4)(1/2) = 1/4 + 3/8 = 5/8
p(3) = [3/8, 5/8]

**Answer:**
Probability that he visits Club A on Thursday = **3/8** (or **0.375**)

**Check:** 3/8 + 5/8 = 1.0.

---

## Q.4 c) The joint probability distribution of two discrete random variable X and Y is given by, f(x, y) = K(2x+y) where x, y are integers such that 0<=x<=2, 0<=y<=2. Find (i) K (ii) Marginal probability distribution of X and Y (iii) P(X >= 1, Y <= 2) [7 marks]

**Given:**
f(x,y) = K(2x+y) for x in {0, 1, 2} and y in {0, 1, 2}.

**Formula / Method:**
1. Sum of all cells = 1.
2. Construct joint probability table.
3. Compute marginals and P(X >= 1, Y <= 2).

**Solution:**

Step 1: Compute values of (2x+y) for x,y in {0,1,2}:
- For x=0: y=0 => 0, y=1 => 1, y=2 => 2. Sum = 3.
- For x=1: y=0 => 2, y=1 => 3, y=2 => 4. Sum = 9.
- For x=2: y=0 => 4, y=1 => 5, y=2 => 6. Sum = 15.

Total sum = 3 + 9 + 15 = 27.
Since sum f(x,y) = 27K = 1 => K = 1/27.

Step 2: Build Joint Probability Table:
```
        Y = 0     Y = 1     Y = 2     Marginal P(X=x)
X = 0   0/27      1/27      2/27      3/27 = 1/9
X = 1   2/27      3/27      4/27      9/27 = 1/3
X = 2   4/27      5/27      6/27      15/27 = 5/9
---------------------------------------------------
P(Y=y)  6/27=2/9  9/27=1/3  12/27=4/9 Total = 27/27 = 1.0
```

Marginal of X:
- P(X=0) = 1/9
- P(X=1) = 1/3
- P(X=2) = 5/9

Marginal of Y:
- P(Y=0) = 2/9
- P(Y=1) = 1/3
- P(Y=2) = 4/9

Step 3: Compute P(X >= 1, Y <= 2):
Since all possible values of Y are <= 2, P(X >= 1, Y <= 2) = P(X >= 1) = P(X=1) + P(X=2) = 9/27 + 15/27 = 24/27 = 8/9.

**Answer:**
(i) **K = 1/27**
(ii) Marginal of X: **P(X=0) = 1/9, P(X=1) = 1/3, P(X=2) = 5/9**
     Marginal of Y: **P(Y=0) = 2/9, P(Y=1) = 1/3, P(Y=2) = 4/9**
(iii) **P(X >= 1, Y <= 2) = 24/27 = 8/9**

**Check:** Total marginal sum = 1/9 + 1/3 + 5/9 = 9/9 = 1.0.

---

### Paper 5 (Makeup)

## Q.3 a) The joint distribution of two random variables X and Y is as follows (rows X, cols Y): Y: -4, 2, 7 ; X=1: 1/8, 1/4, 1/8 ; X=5: 1/4, 1/8, 1/8. Compute the following: E(X), E(Y), E(XY), COV(X,Y). [6 marks]

**Given:**
Joint probability table:
```
       Y = -4    Y = 2    Y = 7
X = 1   1/8       1/4      1/8
X = 5   1/4       1/8      1/8
```

**Formula / Method:**
1. Compute marginals f(x) and g(y).
2. E(X) = sum x f(x), E(Y) = sum y g(y), E(XY) = sum sum x y p(x,y).
3. Cov(X,Y) = E(XY) - E(X)E(Y).

**Solution:**

Step 1: Compute marginals:
- Row X=1: 1/8 + 1/4 + 1/8 = 1/2
- Row X=5: 1/4 + 1/8 + 1/8 = 1/2

- Col Y=-4: 1/8 + 1/4 = 3/8
- Col Y=2: 1/4 + 1/8 = 3/8
- Col Y=7: 1/8 + 1/8 = 2/8 = 1/4

Table with marginals:
```
        Y = -4    Y = 2    Y = 7    Marginal f(x)
X = 1   1/8       1/4      1/8      1/2
X = 5   1/4       1/8      1/8      1/2
---------------------------------------------
g(y)    3/8       3/8      1/4      Total = 1.0
```

Marginals:
- P(X=1) = 1/2, P(X=5) = 1/2
- P(Y=-4) = 3/8, P(Y=2) = 3/8, P(Y=7) = 1/4

Step 2: Compute E(X):
- E(X) = (1 * 1/2) + (5 * 1/2) = 1/2 + 5/2 = 3

Step 3: Compute E(Y):
- E(Y) = (-4 * 3/8) + (2 * 3/8) + (7 * 1/4) = -12/8 + 6/8 + 14/8 = 8/8 = 1

Step 4: Compute E(XY):
- E(XY) = (1 * -4 * 1/8) + (1 * 2 * 1/4) + (1 * 7 * 1/8) + (5 * -4 * 1/4) + (5 * 2 * 1/8) + (5 * 7 * 1/8)
- E(XY) = -4/8 + 2/4 + 7/8 - 20/4 + 10/8 + 35/8
- E(XY) = -4/8 + 4/8 + 7/8 - 40/8 + 10/8 + 35/8
- E(XY) = (-4 + 4 + 7 - 40 + 10 + 35)/8 = 12/8 = 3/2

Step 5: Compute Covariance Cov(X,Y):
- Cov(X,Y) = E(XY) - E(X)E(Y) = 3/2 - (3 * 1) = 3/2 - 3 = -3/2

**Answer:**
**E(X) = 3**
**E(Y) = 1**
**E(XY) = 3/2**
**COV(X,Y) = -3/2**

**Check:** Total marginal sum = 1/2 + 1/2 = 1.0 and 3/8 + 3/8 + 1/4 = 1.0.

---

## Q.3 b) Prove that the Markov Chain whose t.p.m is P = [[0,2/3,1/3],[1/2,0,1/2],[1/2,1/2,0]] is irreducible. Find the corresponding stationary probability vector. [7 marks]

**Given:**
P = [[0, 2/3, 1/3], [1/2, 0, 1/2], [1/2, 1/2, 0]]

**Formula / Method:**
1. A Markov chain is irreducible if every state can be reached from every other state (it forms a single strongly connected component). Alternatively, show that P^2 has all positive entries.
2. Stationary vector t = (a,b,c) satisfies t P = t and a + b + c = 1.

**Solution:**

Step 1: Prove irreducibility:
- Transition paths between states:
  - From state 1: can reach state 2 (p_{12} = 2/3 > 0) and state 3 (p_{13} = 1/3 > 0).
  - From state 2: can reach state 1 (p_{21} = 1/2 > 0) and state 3 (p_{23} = 1/2 > 0).
  - From state 3: can reach state 1 (p_{31} = 1/2 > 0) and state 2 (p_{32} = 1/2 > 0).
- Since every state communicates directly with every other state, the chain is **irreducible**.
- Alternatively, computing P^2:
P^2 = [[1/2, 1/6, 1/3], [1/4, 7/12, 1/6], [1/4, 1/3, 5/12]]
Since P^2 > 0, the chain is regular and irreducible.

Step 2: Find stationary probability vector t = (a, b, c):
[a, b, c] [[0, 2/3, 1/3], [1/2, 0, 1/2], [1/2, 1/2, 0]] = [a, b, c]

Step 3: Write equations:
1. Column 1: (1/2) b + (1/2) c = a => b + c = 2a
2. Column 2: (2/3) a + (1/2) c = b => 4a + 3c = 6b
3. Column 3: (1/3) a + (1/2) b = c => 2a + 3b = 6c

Step 4: Solve system of equations:
From b + c = 2a => c = 2a - b.
Substitute c = 2a - b into 4a + 3c = 6b:
4a + 3(2a - b) = 6b => 4a + 6a - 3b = 6b => 10a = 9b => b = (10/9) a

Then c:
c = 2a - (10/9) a = (8/9) a

Step 5: Substitute into a + b + c = 1:
a + (10/9) a + (8/9) a = 1 => (27/9) a = 1 => 3a = 1 => a = 1/3
b = (10/9) * (1/3) = 10/27
c = (8/9) * (1/3) = 8/27

**Answer:**
**Every state communicates with every other state (P^2 > 0), so the chain is irreducible.**
Stationary vector: **t = (1/3, 10/27, 8/27)**

**Check:** a + b + c = 9/27 + 10/27 + 8/27 = 27/27 = 1.0.

---

## Q.3 c) Three boys A, B, C are throwing ball to each other. A always throws the ball to B and B always throws the ball to C. C is just as likely to throw the ball to B as to A. If C was the first person to throw the ball find the probabilities that after three throws, B has the ball. [7 marks]

Same as Q.3 c) of Paper 1 above, answer: **P(B has ball after 3 throws) = 1/4**.

---

## Q.4 a) Define: i) Probability Vector ii) Stochastic Matrix iii) Regular Stochastic Matrix. [6 marks]

**Given:** Theory question on definitions.

**Solution:**

1. **Probability Vector:** A non-negative row vector whose entries sum to 1. E.g., (0.2, 0.8).
2. **Stochastic Matrix:** A square matrix with non-negative entries where each row sums to 1. E.g., [[0.5, 0.5], [0.3, 0.7]].
3. **Regular Stochastic Matrix:** A stochastic matrix P where some power P^n has all strictly positive entries. E.g., [[0, 1], [0.5, 0.5]] since P^2 > 0.

**Answer:**
See definitions above.

---

## Q.4 b) The joint probability distribution of two discrete random variables X and Y is given by f(x, y) = K(2x + y). Where x and y are integers such that 0<=x<=2, 0<=y<=3. i) Find the value of K ii) P(X = 1, Y = 2) iii) P(X = 2, Y = 1) iv) P(X >= 1, Y <= 2) [7 marks]

**Given:**
f(x,y) = K(2x+y) for x in {0,1,2}, y in {0,1,2,3}.

**Formula / Method:**
From Paper 1 Q.4 a), K = 1/42 and f(x,y) = (2x+y)/42.

**Solution:**

Step 1: Compute (i) K = 1/42.

Step 2: Compute (ii) P(X=1, Y=2):
f(1,2) = (2(1)+2)/42 = 4/42 = 2/21

Step 3: Compute (iii) P(X=2, Y=1):
f(2,1) = (2(2)+1)/42 = 5/42

Step 4: Compute (iv) P(X >= 1, Y <= 2):
Sum for x in {1,2} and y in {0,1,2}:
(2 + 3 + 4 + 4 + 5 + 6)/42 = 24/42 = 4/7

**Answer:**
(i) **K = 1/42**
(ii) **P(X = 1, Y = 2) = 4/42 = 2/21**
(iii) **P(X = 2, Y = 1) = 5/42**
(iv) **P(X >= 1, Y <= 2) = 24/42 = 4/7**

---

## Q.4 c) The t.p.m of a Markov Chain is given by P = [[1/2,0,1/2],[1,0,0],[1/4,1/2,1/4]] and the initial probability distribution is P(0) = (1/2, 1/2, 0). Find P_1^(2) [= P(X2 = 1)]. [7 marks]

**Given:**
P = [[1/2, 0, 1/2], [1, 0, 0], [1/4, 1/2, 1/4]]
Initial distribution p(0) = (1/2, 1/2, 0).

**Formula / Method:**
1. Compute p(1) = p(0) P.
2. Compute p(2) = p(1) P.
3. Report first component P_1^(2) = p(2)_1.

**Solution:**

Step 1: Calculate p(1):
p(1) = p(0) P = [1/2, 1/2, 0] [[1/2, 0, 1/2], [1, 0, 0], [1/4, 1/2, 1/4]]
- Entry 1: (1/2)(1/2) + (1/2)(1) + 0(1/4) = 1/4 + 1/2 = 3/4
- Entry 2: (1/2)(0) + (1/2)(0) + 0(1/2) = 0
- Entry 3: (1/2)(1/2) + (1/2)(0) + 0(1/4) = 1/4
p(1) = [3/4, 0, 1/4]

Step 2: Calculate p(2):
p(2) = p(1) P = [3/4, 0, 1/4] [[1/2, 0, 1/2], [1, 0, 0], [1/4, 1/2, 1/4]]
- Entry 1 (P_1^(2)): (3/4)(1/2) + 0(1) + (1/4)(1/4) = 3/8 + 1/16 = (6 + 1)/16 = 7/16
- Entry 2: (3/4)(0) + 0(0) + (1/4)(1/2) = 1/8 = 2/16
- Entry 3: (3/4)(1/2) + 0(0) + (1/4)(1/4) = 3/8 + 1/16 = 7/16

p(2) = [7/16, 2/16, 7/16]

**Answer:**
**P_1^(2) = 7/16** (or **0.4375**)

**Check:** Total probability = 7/16 + 2/16 + 7/16 = 16/16 = 1.0.

---

### Paper 6 (Dec 2025 / Jan 2026)

## Q.3 a) The joint probability distribution of two random variables x and y is (rows x, cols y): y: -4, 2, 7 ; x=1: 1/8, 1/4, 1/8 ; x=5: 1/4, 1/8, 1/8. i) Find the marginal distribution of x and y. ii) Obtain the covariance of x and y. [6 marks]

Same joint distribution table as Q.3 a) of Paper 5 above, answer: **Marginals P(X=1)=1/2, P(X=5)=1/2; P(Y=-4)=3/8, P(Y=2)=3/8, P(Y=7)=1/4; Cov(X,Y) = -3/2**.

---

## Q.3 b) Find the unique fixed probability vector of P = [[0,1,0],[1/6,1/2,1/3],[0,2/3,1/3]]. [7 marks]

Same as Q.3 b) of Paper 1 above, answer: **unique fixed probability vector is t = (1/10, 3/5, 3/10)**.

---

## Q.3 c) A student study habit are as follows: If he studies one night, he is 70% sure of not studying next night, on the other hand if he does not study one night, he is 60% sure not to study the next night. In the long run how often does he study? [7 marks]

Same as Q.3 b) of Paper 4 above, answer: **long run fraction of studying is 4/11**.

---

## Q.4 a) Define the following: i) Probability vector ii) Regular stochastic matrix iii) Absorbing state. [6 marks]

Same as Q.3 a) of Paper 4 above, answer: **see definitions in Paper 4 Q.3 a)**.

---

## Q.4 b) If X and Y are two independent random variables with the following distribution. Find the joint probability distribution of X and Y and hence find the covariance. x: 1, 2 ; f(x): 0.7, 0.3 ; y: -2, 5, 3 ; g(y): 0.3, 0.5, 0.2 [7 marks]

**Given:**
X and Y are independent random variables.
- Marginal of X: P(X=1) = 0.7, P(X=2) = 0.3
- Marginal of Y: P(Y=-2) = 0.3, P(Y=5) = 0.5, P(Y=3) = 0.2

**Formula / Method:**
1. Since X and Y are independent, p(x,y) = f(x) g(y) for all x,y.
2. For independent random variables, Cov(X,Y) = 0.

**Solution:**

Step 1: Compute joint probabilities p(x,y) = f(x) g(y):
- For X = 1:
  - y = -2 => 0.7 * 0.3 = 0.21
  - y = 5 => 0.7 * 0.5 = 0.35
  - y = 3 => 0.7 * 0.2 = 0.14

- For X = 2:
  - y = -2 => 0.3 * 0.3 = 0.09
  - y = 5 => 0.3 * 0.5 = 0.15
  - y = 3 => 0.3 * 0.2 = 0.06

Step 2: Construct Joint Probability Distribution Table:

```
        Y = -2    Y = 5    Y = 3    Marginal f(x)
X = 1   0.21      0.35     0.14     0.70
X = 2   0.09      0.15     0.06     0.30
-----------------------------------------
g(y)    0.30      0.50     0.20     Total = 1.00
```

Step 3: Compute Covariance:
- E(X) = 1(0.7) + 2(0.3) = 0.7 + 0.6 = 1.3 = 13/10
- E(Y) = -2(0.3) + 5(0.5) + 3(0.2) = -0.6 + 2.5 + 0.6 = 2.5 = 5/2
- E(XY) = (1 * -2 * 0.21) + (1 * 5 * 0.35) + (1 * 3 * 0.14) + (2 * -2 * 0.09) + (2 * 5 * 0.15) + (2 * 3 * 0.06)
  - E(XY) = -0.42 + 1.75 + 0.42 - 0.36 + 1.50 + 0.36 = 3.25 = 13/4
- Cov(X,Y) = E(XY) - E(X)E(Y) = 3.25 - (1.3 * 2.5) = 3.25 - 3.25 = 0

**Answer:**
Joint distribution table as given above.
Covariance: **Cov(X,Y) = 0**

**Check:** Independence guarantees Cov(X,Y) = 0. Verified!

---

## Q.4 c) Three girls A, B, C are throwing the ball to each other. A always throws the ball to B, B always throws the ball to C. C is just as likely to throw the ball to B as to C. If C was the first person to throw the ball, find the probability that after 3 throws A, B, C has the ball. [7 marks]

Same as Q.3 c) of Paper 1 above (noting that "to B as to C" is a misprint for "to B as to A"), answer: **p3 = (1/4, 1/4, 1/2), so P(A)=1/4, P(B)=1/4, P(C)=1/2**.

---

### Paper 7 (Model Q-I)

## Q.3 a) The joint probability distribution of discrete random variables X & Y are as follows (rows X, cols Y): Y: -3, 2, 4 ; X=1: 0.1, 0.2, 0.2 ; X=2: 0.3, 0.1, 0.1. Then i) determine marginal distribution of X & Y, ii) show that X & Y are dependent. [6 marks]

**Given:**
Joint probability distribution table:
```
       Y = -3    Y = 2    Y = 4
X = 1   0.1       0.2      0.2
X = 2   0.3       0.1      0.1
```

**Formula / Method:**
1. Marginals are row sums f(x) and column sums g(y).
2. Show p(x,y) != f(x)g(y) for at least one cell.

**Solution:**

Step 1: Compute marginals:
- Row X=1: 0.1 + 0.2 + 0.2 = 0.5
- Row X=2: 0.3 + 0.1 + 0.1 = 0.5

- Col Y=-3: 0.1 + 0.3 = 0.4
- Col Y=2: 0.2 + 0.1 = 0.3
- Col Y=4: 0.2 + 0.1 = 0.3

Joint table with marginals:
```
        Y = -3    Y = 2    Y = 4    Marginal f(x)
X = 1   0.1       0.2      0.2      0.5
X = 2   0.3       0.1      0.1      0.5
-----------------------------------------
g(y)    0.4       0.3      0.3      Total = 1.0
```

Marginal of X:
- P(X=1) = 0.5, P(X=2) = 0.5

Marginal of Y:
- P(Y=-3) = 0.4, P(Y=2) = 0.3, P(Y=4) = 0.3

Step 2: Check dependence at cell (X=1, Y=-3):
- p(1, -3) = 0.1
- f(1) g(-3) = 0.5 * 0.4 = 0.20
- Since 0.1 != 0.20, X and Y are **dependent**.

**Answer:**
(i) Marginal of X: **P(X=1) = 0.5, P(X=2) = 0.5**
    Marginal of Y: **P(Y=-3) = 0.4, P(Y=2) = 0.3, P(Y=4) = 0.3**
(ii) **X and Y are dependent because P(1,-3) = 0.1 != P(X=1)P(Y=-3) = 0.20.**

---

## Q.3 b) Determine the value of k so that the function f(x, y) = k|x - y|, for x = -2, 0, 2; y = -2, 3 represents joint probability distribution of the random variables X and Y. Also determine cov(X, Y). [7 marks]

**Given:**
f(x,y) = k |x - y| for x in {-2, 0, 2} and y in {-2, 3}.

**Formula / Method:**
1. Sum over all cells equals 1.
2. Build joint table and compute E(X), E(Y), E(XY), and Cov(X,Y) = E(XY) - E(X)E(Y).

**Solution:**

Step 1: Compute |x - y| for each cell:
- x = -2:
  - y = -2 => |-2 - (-2)| = 0
  - y = 3 => |-2 - 3| = 5
- x = 0:
  - y = -2 => |0 - (-2)| = 2
  - y = 3 => |0 - 3| = 3
- x = 2:
  - y = -2 => |2 - (-2)| = 4
  - y = 3 => |2 - 3| = 1

Total sum = 0 + 5 + 2 + 3 + 4 + 1 = 15.
Since sum f(x,y) = 15k = 1 => k = 1/15.

Step 2: Build Joint Probability Table f(x,y) = |x-y|/15:

```
        Y = -2    Y = 3     Marginal f(x)
X = -2  0/15      5/15      5/15 = 1/3
X = 0   2/15      3/15      5/15 = 1/3
X = 2   4/15      1/15      5/15 = 1/3
----------------------------------------
g(y)    6/15=2/5  9/15=3/5  Total = 15/15 = 1.0
```

Marginal of X: P(X=-2) = 1/3, P(X=0) = 1/3, P(X=2) = 1/3.
Marginal of Y: P(Y=-2) = 2/5, P(Y=3) = 3/5.

Step 3: Compute E(X):
- E(X) = (-2 * 1/3) + (0 * 1/3) + (2 * 1/3) = 0

Step 4: Compute E(Y):
- E(Y) = (-2 * 2/5) + (3 * 3/5) = -4/5 + 9/5 = 5/5 = 1

Step 5: Compute E(XY):
- E(XY) = (-2 * -2 * 0) + (-2 * 3 * 5/15) + (0 * -2 * 2/15) + (0 * 3 * 3/15) + (2 * -2 * 4/15) + (2 * 3 * 1/15)
- E(XY) = 0 - 30/15 + 0 + 0 - 16/15 + 6/15 = -2 - 10/15 = -2 - 2/3 = -8/3

Step 6: Compute Covariance Cov(X,Y):
- Cov(X,Y) = E(XY) - E(X)E(Y) = -8/3 - (0 * 1) = -8/3

**Answer:**
**k = 1/15**
**Cov(X,Y) = -8/3**

**Check:** Total table sum = 15/15 = 1.0.

---

## Q.3 c) Three boys X, Y, Z are throwing a ball to each other. X always throws the ball to Y & Y always throws the ball to Z. But Z is just as likely to throw the ball to Y or as to X. Write TPM if Z is the first person to throw the ball, find the probability that X has the ball after fourth throw. [7 marks]

**Given:**
- States: 1: X, 2: Y, 3: Z.
- Rules:
  - X always throws to Y => Row X = (0, 1, 0)
  - Y always throws to Z => Row Y = (0, 0, 1)
  - Z equally likely to throw to Y or X => Row Z = (1/2, 1/2, 0)
- Z starts the game => p(0) = (0, 0, 1).

**Formula / Method:**
Calculate p(4) = p(0) P^4.

**Solution:**

Step 1: Write Transition Probability Matrix P:
P = [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]]

Step 2: Calculate p(1) (1st throw):
p(1) = p(0) P = [0, 0, 1] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]] = [1/2, 1/2, 0]

Step 3: Calculate p(2) (2nd throw):
p(2) = p(1) P = [1/2, 1/2, 0] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]] = [0, 1/2, 1/2]

Step 4: Calculate p(3) (3rd throw):
p(3) = p(2) P = [0, 1/2, 1/2] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]] = [1/4, 1/4, 1/2]

Step 5: Calculate p(4) (4th throw):
p(4) = p(3) P = [1/4, 1/4, 1/2] [[0, 1, 0], [0, 0, 1], [1/2, 1/2, 0]]
- Entry 1 (X): (1/4)(0) + (1/4)(0) + (1/2)(1/2) = 1/4
- Entry 2 (Y): (1/4)(1) + (1/4)(0) + (1/2)(1/2) = 1/4 + 1/4 = 1/2
- Entry 3 (Z): (1/4)(0) + (1/4)(1) + (1/2)(0) = 1/4

p(4) = [1/4, 1/2, 1/4]

**Answer:**
TPM P as given above.
Probability that X has the ball after the fourth throw = **1/4** (or **0.25**)

**Check:** Total probability = 1/4 + 1/2 + 1/4 = 1.0.

---

## Q.4 a) Given the following joint distribution of the random variable X & Y (X=1: -2:0.1, -1:0.2, 4:0, 5:0.3 ; X=2: -2:0.2, -1:0.1, 4:0.1, 5:0). Determine the marginal probability distributions of X & Y. Also compute i) Expectations of X, Y & XY, ii) Covariance of X & Y, iii) Correlation of X & Y. [6 marks]

Same joint distribution table as Q.3 a) of Paper 1 above, answer: **Marginals P(X=1)=3/5, P(X=2)=2/5; P(Y=-2)=3/10, P(Y=-1)=3/10, P(Y=4)=1/10, P(Y=5)=3/10; E(X) = 7/5, E(Y) = 1, E(XY) = 9/10, Cov(X,Y) = -1/2, rho = -5 / (4 sqrt(2)) ≈ -0.3294**.

---

## Q.4 b) The joint probability distribution of random variables X & Y are as follows: (rows x, cols y) y: -4, 2, 7 ; x=1: 1/8, 1/4, 1/8 ; x=5: 1/4, 1/8, 1/8. then determine i) marginal distribution of X & Y, ii) E(X), E(Y) & E(XY), iii) COV(X, Y), iv) rho(X, Y). [7 marks]

Same joint distribution table as Q.3 a) of Paper 5 above, answer: **Marginals P(X=1)=1/2, P(X=5)=1/2; P(Y=-4)=3/8, P(Y=2)=3/8, P(Y=7)=1/4; E(X) = 3, E(Y) = 1, E(XY) = 3/2, Cov(X,Y) = -3/2, rho = -1/(5 sqrt(3)) ≈ -0.1732**.

---

## Q.4 c) The students study habits are as follows; If he studies on one night, he is 60% sure not to study on next night. On the other hand, if he does not study on tonight, he is 80% sure to study next night. Write the transition probability matrix for his chain of study. In the long run how often does he study? Suppose he studies on Monday night, what is the probability that he does not study on Friday night? [7 marks]

**Given:**
- States: 1: Studies (S), 2: Does not study (N).
- Rules:
  - From S: 60% sure not to study => P(S -> N) = 0.6, P(S -> S) = 0.4. Row S = (0.4, 0.6).
  - From N: 80% sure to study => P(N -> S) = 0.8, P(N -> N) = 0.2. Row N = (0.8, 0.2).
- Monday night (n=0): Studies => p(0) = (1, 0).
- Days: Monday (n=0), Tuesday (n=1), Wednesday (n=2), Thursday (n=3), Friday (n=4).

**Formula / Method:**
1. Stationary vector t P = t with a + b = 1.
2. State vector on Friday: p(4) = p(0) P^4.

**Solution:**

Step 1: Write Transition Probability Matrix P:
P = [[0.4, 0.6], [0.8, 0.2]] = [[2/5, 3/5], [4/5, 1/5]]

Step 2: Find stationary probability vector t = (a, b):
[a, b] [[0.4, 0.6], [0.8, 0.2]] = [a, b]
- 0.4 a + 0.8 b = a => 0.8 b = 0.6 a => 4b = 3a => b = (3/4) a

Substitute into a + b = 1:
a + (3/4) a = 1 => (7/4) a = 1 => a = 4/7, b = 3/7

In the long run, he studies **4/7** of the time (approx **57.14%**).

Step 3: Calculate state probability vector day-by-day starting from Monday p(0) = (1, 0):

- **Tuesday (n=1):**
p(1) = p(0) P = [1, 0] [[0.4, 0.6], [0.8, 0.2]] = [0.4, 0.6] = [2/5, 3/5]

- **Wednesday (n=2):**
p(2) = p(1) P = [2/5, 3/5] [[2/5, 3/5], [4/5, 1/5]]
  - Entry 1 (S): (2/5)(2/5) + (3/5)(4/5) = (4 + 12)/25 = 16/25 = 0.64
  - Entry 2 (N): (2/5)(3/5) + (3/5)(1/5) = (6 + 3)/25 = 9/25 = 0.36
p(2) = [16/25, 9/25]

- **Thursday (n=3):**
p(3) = p(2) P = [16/25, 9/25] [[2/5, 3/5], [4/5, 1/5]]
  - Entry 1 (S): (16/25)(2/5) + (9/25)(4/5) = (32 + 36)/125 = 68/125 = 0.544
  - Entry 2 (N): (16/25)(3/5) + (9/25)(1/5) = (48 + 9)/125 = 57/125 = 0.456
p(3) = [68/125, 57/125]

- **Friday (n=4):**
p(4) = p(3) P = [68/125, 57/125] [[2/5, 3/5], [4/5, 1/5]]
  - Entry 1 (S): (68/125)(2/5) + (57/125)(4/5) = (136 + 228)/625 = 364/625 = 0.5824
  - Entry 2 (N): (68/125)(3/5) + (57/125)(1/5) = (204 + 57)/625 = 261/625 = 0.4176
p(4) = [364/625, 261/625]

Probability that he does **not** study on Friday night = Entry 2 of p(4) = 261/625 = 0.4176.

**Answer:**
TPM P as given above.
In the long run, he studies **4/7** of the time (approx **57.14%**).
Probability that he does not study on Friday night = **261/625** (or **0.4176**)

**Check:** Total probability for Friday = 364/625 + 261/625 = 625/625 = 1.0.

