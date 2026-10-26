# VTU BCS301 Module 5: Analysis of Variance (ANOVA) Exam Solutions

## Table of Contents

- [Paper 1](#paper-1)
  - [Paper 1 Q.9(a) [A1]: One-Way ANOVA - Three Kinds of Food on Rats](#paper-1-q9a-a1-one-way-anova---three-kinds-of-food-on-rats)
  - [Paper 1 Q.9(b) [A2]: Latin Square Design - Output of Wheat (4x4)](#paper-1-q9b-a2-latin-square-design---output-of-wheat-4x4)
  - [Paper 1 Q.10(a) [A3]: Two-Way ANOVA - Per Acre Production of Wheat Varieties](#paper-1-q10a-a3-two-way-anova---per-acre-production-of-wheat-varieties)
  - [Paper 1 Q.10(b) [A4]: Two-Way ANOVA with Replication - Drug Effectiveness on Blood Pressure](#paper-1-q10b-a4-two-way-anova-with-replication---drug-effectiveness-on-blood-pressure)
- [Paper 2](#paper-2)
  - [Paper 2 Q.9(a) [A5]: One-Way ANOVA - Production of Three Wheat Varieties on 12 Plots](#paper-2-q9a-a5-one-way-anova---production-of-three-wheat-varieties-on-12-plots)
  - [Paper 2 Q.9(b): Latin Square Design - Output of Wheat (4x4)](#paper-2-q9b-latin-square-design---output-of-wheat-4x4)
  - [Paper 2 Q.10(a) [A6]: Two-Way ANOVA - Doctors and Treatments Patient Recovery Days](#paper-2-q10a-a6-two-way-anova---doctors-and-treatments-patient-recovery-days)
  - [Paper 2 Q.10(b) [A7]: One-Way ANOVA - Anesthesia Types and Length of Hospital Stay](#paper-2-q10b-a7-one-way-anova---anesthesia-types-and-length-of-hospital-stay)
- [Paper 3](#paper-3)
  - [Paper 3 Q.9(a) [A8]: One-Way ANOVA - Wheat Varieties Yields in Four Plots](#paper-3-q9a-a8-one-way-anova---wheat-varieties-yields-in-four-plots)
  - [Paper 3 Q.9(b) [A9]: Latin Square Design - Five Fertilizers on Plots of Different Fertility (5x5)](#paper-3-q9b-a9-latin-square-design---five-fertilizers-on-plots-of-different-fertility-5x5)
  - [Paper 3 Q.10(a) [A10]: Two-Way ANOVA with Coding - Land Pieces and Treatments](#paper-3-q10a-a10-two-way-anova-with-coding---land-pieces-and-treatments)
  - [Paper 3 Q.10(b) [A11]: One-Way ANOVA with Coding - Brand Preferences of Power](#paper-3-q10b-a11-one-way-anova-with-coding---brand-preferences-of-power)
- [Paper 4](#paper-4)
  - [Paper 4 Q.9(a): Two-Way ANOVA with Replication - Drug Effectiveness on Blood Pressure](#paper-4-q9a-two-way-anova-with-replication---drug-effectiveness-on-blood-pressure)
  - [Paper 4 Q.9(b) [A12]: Latin Square Design - Five Fertilizers (5x5)](#paper-4-q9b-a12-latin-square-design---five-fertilizers-5x5)
  - [Paper 4 Q.10(a) [A13]: One-Way ANOVA - Comparison of Deaths in Three Hospitals](#paper-4-q10a-a13-one-way-anova---comparison-of-deaths-in-three-hospitals)
  - [Paper 4 Q.10(b): Latin Square Design - Output of Wheat (4x4)](#paper-4-q10b-latin-square-design---output-of-wheat-4x4)
- [Paper 5](#paper-5)
  - [Paper 5 Q.9(a) [A14]: One-Way ANOVA - Three Types of Fertilizers on Plant Growth](#paper-5-q9a-a14-one-way-anova---three-types-of-fertilizers-on-plant-growth)
  - [Paper 5 Q.9(b) [A15]: Two-Way ANOVA - Muskrats Quarantined Worms](#paper-5-q9b-a15-two-way-anova---muskrats-quarantined-worms)
  - [Paper 5 Q.10(a) [A16]: One-Way ANOVA - Weight Loss Across Four Diets](#paper-5-q10a-a16-one-way-anova---weight-loss-across-four-diets)
  - [Paper 5 Q.10(b): Latin Square Design - Output of Wheat (4x4)](#paper-5-q10b-latin-square-design---output-of-wheat-4x4)
- [Paper 6](#paper-6)
  - [Paper 6 Q.9(a) [A17]: One-Way ANOVA - Production Output of Three Machines](#paper-6-q9a-a17-one-way-anova---production-output-of-three-machines)
  - [Paper 6 Q.9(b) [A18]: Two-Way ANOVA - Varieties of Fertilizers Design](#paper-6-q9b-a18-two-way-anova---varieties-of-fertilizers-design)
  - [Paper 6 Q.10(a) [A19]: Two-Way ANOVA - Per Acre Production Data for 3 Varieties of Wheat](#paper-6-q10a-a19-two-way-anova---per-acre-production-data-for-3-varieties-of-wheat)
  - [Paper 6 Q.10(b) [A20]: Latin Square Design - Output of Wheat (4x4)](#paper-6-q10b-a20-latin-square-design---output-of-wheat-4x4)
- [Paper 7](#paper-7)
  - [Paper 7 Q.9(a) [A22]: One-Way ANOVA - Production Output of Three Machines](#paper-7-q9a-a22-one-way-anova---production-output-of-three-machines)
  - [Paper 7 Q.9(b): Two-Way ANOVA - Production of Three Varieties of Wheat](#paper-7-q9b-two-way-anova---production-of-three-varieties-of-wheat)
  - [Paper 7 Q.10(a): Two-Way ANOVA - Varieties of Fertilizers Design](#paper-7-q10a-two-way-anova---varieties-of-fertilizers-design)
  - [Paper 7 Q.10(b) [A21]: Latin Square Design - Yields of Paddy Cultivation Methods (4x4)](#paper-7-q10b-a21-latin-square-design---yields-of-paddy-cultivation-methods-4x4)

---

# Paper 1

## Paper 1 Q.9(a) [A1]: One-Way ANOVA - Three Kinds of Food on Rats

**Given:** Three different kinds of food are tested on three groups of rats for 5 weeks.
- Food 1: 8, 12, 19, 8, 6, 11
- Food 2: 4, 5, 4, 6, 9, 7
- Food 3: 11, 8, 7, 13, 7, 9
- Level of significance: alpha = 0.05
- Critical table value: F0.05(2, 15) = 3.68

**Formula / Method:**
- Null hypothesis H0: mu1 = mu2 = mu3 (Mean weight gains for all three foods are equal).
- Alternative hypothesis H1: At least two food means are not equal.
- Grand total T = sum x, total observations N = 18.
- Correction factor CF = T^2 / N.
- Total sum of squares SST = sum x^2 - CF.
- Sum of squares between samples SSB = sum (Ti^2 / ni) - CF.
- Error sum of squares SSE = SST - SSB.
- F = MSB / MSE = (SSB / (k-1)) / (SSE / (N-k)).

**Solution:**

**Step 1: Compute column totals and sum of squares of observations.**

Table of data and x^2 values:
```
  Food 1 (x1)   x1^2   |   Food 2 (x2)   x2^2   |   Food 3 (x3)   x3^2
-----------------------+-----------------------+-----------------------
       8         64    |        4         16    |       11        121
      12        144    |        5         25    |        8         64
      19        361    |        4         16    |        7         49
       8         64    |        6         36    |       13        169
       6         36    |        9         81    |        7         49
      11        121    |        7         49    |        9         81
-----------------------+-----------------------+-----------------------
 Total T1 = 64  sum=790 |  Total T2 = 35  sum=223 |  Total T3 = 55  sum=533
```

- Total observations N = 6 + 6 + 6 = 18.
- Grand total T = T1 + T2 + T3 = 64 + 35 + 55 = 154.
- Total sum of squares of all items sum x^2 = 790 + 223 + 533 = 1546.

**Step 2: Calculate Correction Factor (CF) and Sums of Squares.**

- CF = T^2 / N = 154^2 / 18 = 23716 / 18 = 1317.56.
- SST = sum x^2 - CF = 1546 - 1317.56 = 228.44.
- SSB = (64^2 / 6 + 35^2 / 6 + 55^2 / 6) - CF = (4096 + 1225 + 3025) / 6 - 1317.56 = 8346 / 6 - 1317.56 = 1391 - 1317.56 = 73.44.
- SSE = SST - SSB = 228.44 - 73.44 = 155.00.

**Step 3: Degrees of freedom and Mean Squares.**
- Degrees of freedom between groups dfB = k - 1 = 3 - 1 = 2.
- Degrees of freedom error dfE = N - k = 18 - 3 = 15.
- Mean square between groups MSB = SSB / dfB = 73.44 / 2 = 36.72.
- Mean square error MSE = SSE / dfE = 155.00 / 15 = 10.33.

**Step 4: Compute test statistic F.**
- F = MSB / MSE = 36.72 / 10.33 = 3.55.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Foods (SSB) |        73.44        |   2  |      36.72       |     3.55
Within Foods (SSE)  |       155.00        |  15  |      10.33       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       228.44        |  17  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 3.55 is less than the critical table value F0.05(2, 15) = 3.68.
- Therefore, we accept the null hypothesis H0 at 5% significance level.
- There is no significant difference in the mean weight gain of rats among the three kinds of food.

**Answer:** **Accept H0. Calculated F = 3.55 < Table F = 3.68. Food types do not produce significantly different weight gains.**

**Check:** scipy.stats.f_oneway gives F = 3.5538, p-value = 0.0545 > 0.05.


## Paper 1 Q.9(b) [A2]: Latin Square Design - Output of Wheat (4x4)

**Given:** Statistics concerning output of wheat per field obtained under a 4x4 Latin square design with four wheat varieties A, B, C, D:
```
  C25  B23  A20  D20
  A19  D19  C21  B18
  B19  A14  D17  C20
  D17  C20  B21  A15
```
- Significance level: 5%
- Critical table value: F0.05(3, 6) = 4.76

**Formula / Method:**
- Rows (n=4), Columns (n=4), Treatments (n=4). Total N = n^2 = 16.
- Null hypotheses:
  - H0R: No significant difference among row yields (fields/rows).
  - H0C: No significant difference among column yields.
  - H0Tr: No significant difference among wheat variety yields (A, B, C, D).
- CF = T^2 / N.
- SST = sum sum x^2 - CF.
- Row sum of squares SSR = sum(Ri^2) / n - CF.
- Column sum of squares SSC = sum(Cj^2) / n - CF.
- Treatment sum of squares SSTr = sum(Trk^2) / n - CF.
- Error sum of squares SSE = SST - SSR - SSC - SSTr.
- dfR = dfC = dfTr = n - 1 = 3, dfE = (n-1)(n-2) = 3 * 2 = 6.

**Solution:**

**Step 1: Compute Row, Column, and Treatment Totals.**

Data grid with row and column totals:
```
           Col 1   Col 2   Col 3   Col 4   | Row Total
-------------------------------------------+----------
Row 1    |  C25     B23     A20     D20    |   88
Row 2    |  A19     D19     C21     B18    |   77
Row 3    |  B19     A14     D17     C20    |   70
Row 4    |  D17     C20     B21     A15    |   73
-------------------------------------------+----------
Col Total|   80      76      79      73    | Grand T = 308
```

Treatment Totals (Sum of observations for each letter):
- Variety A: 20 + 19 + 14 + 15 = 68
- Variety B: 23 + 18 + 19 + 21 = 81
- Variety C: 25 + 21 + 20 + 20 = 86
- Variety D: 20 + 19 + 17 + 17 = 73
- Check total: 68 + 81 + 86 + 73 = 308 = T.

Sum of squares of all 16 items:
sum x^2 = 25^2 + 23^2 + 20^2 + 20^2 + 19^2 + 19^2 + 21^2 + 18^2 + 19^2 + 14^2 + 17^2 + 20^2 + 17^2 + 20^2 + 21^2 + 15^2
sum x^2 = 625 + 529 + 400 + 400 + 361 + 361 + 441 + 324 + 361 + 196 + 289 + 400 + 289 + 400 + 441 + 225 = 6042.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 308^2 / 16 = 94864 / 16 = 5929.00.
- SST = sum x^2 - CF = 6042 - 5929 = 113.00.
- SSR = (88^2 + 77^2 + 70^2 + 73^2) / 4 - CF = (7744 + 5929 + 4900 + 5329) / 4 - 5929 = 23902 / 4 - 5929 = 5975.50 - 5929 = 46.50.
- SSC = (80^2 + 76^2 + 79^2 + 73^2) / 4 - CF = (6400 + 5776 + 6241 + 5329) / 4 - 5929 = 23746 / 4 - 5929 = 5936.50 - 5929 = 7.50.
- SSTr = (68^2 + 81^2 + 86^2 + 73^2) / 4 - CF = (4624 + 6561 + 7396 + 5329) / 4 - 5929 = 23910 / 4 - 5929 = 5977.50 - 5929 = 48.50.
- SSE = SST - SSR - SSC - SSTr = 113.00 - 46.50 - 7.50 - 48.50 = 10.50.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfR = n - 1 = 3 => MSR = 46.50 / 3 = 15.50.
- dfC = n - 1 = 3 => MSC = 7.50 / 3 = 2.50.
- dfTr = n - 1 = 3 => MSTr = 48.50 / 3 = 16.17.
- dfE = (n-1)(n-2) = 6 => MSE = 10.50 / 6 = 1.75.

**Step 4: Compute F ratios.**
- FR = MSR / MSE = 15.50 / 1.75 = 8.86.
- FC = MSC / MSE = 2.50 / 1.75 = 1.43.
- FTr = MSTr / MSE = 16.17 / 1.75 = 9.24.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Rows / Fields (SSR) |        46.50        |   3  |      15.50       |     8.86
Columns (SSC)       |         7.50        |   3  |       2.50       |     1.43
Varieties (SSTr)    |        48.50        |   3  |      16.17       |     9.24
Error (SSE)         |        10.50        |   6  |       1.75       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       113.00        |  15  |                  |
```

**Step 6: Conclusions.**
- Critical table value is F0.05(3, 6) = 4.76.
- For Rows: Calculated FR = 8.86 > 4.76. Reject H0R. Rows (fields) show significant variation in output.
- For Columns: Calculated FC = 1.43 < 4.76. Accept H0C. Columns show no significant variation.
- For Varieties: Calculated FTr = 9.24 > 4.76. Reject H0Tr. Wheat varieties A, B, C, D produce significantly different yields.

**Answer:** **Varieties F = 9.24 > 4.76 (Significant differences among varieties). Rows F = 8.86 > 4.76 (Significant row differences). Columns F = 1.43 < 4.76 (No column differences).**

**Check:** Sum of SS: 46.50 + 7.50 + 48.50 + 10.50 = 113.00.


## Paper 1 Q.10(a) [A3]: Two-Way ANOVA - Per Acre Production of Wheat Varieties

**Given:** Per acre production data for 3 varieties of wheat (A, B, C) each grown on 4 plots (Plot 1, 2, 3, 4):
- Plot 1: A=6, B=5, C=5
- Plot 2: A=7, B=5, C=4
- Plot 3: A=3, B=3, C=3
- Plot 4: A=8, B=7, C=4
- Level of significance: 5%
- Critical table values given: F0.05(2, 9) = 4.26 for varieties; also F0.05(3, 6) = 4.76 for plots.

**Formula / Method:**
- Rows = Plots (r=4), Columns = Wheat Varieties (c=3). Total N = r * c = 12.
- H0C: No significant difference among wheat varieties (Columns).
- H0R: No significant difference among plots (Rows).
- CF = T^2 / N.
- SST = sum sum x^2 - CF.
- SSC = sum(Cj^2) / r - CF.
- SSR = sum(Ri^2) / c - CF.
- SSE = SST - SSC - SSR.
- dfC = c - 1 = 2, dfR = r - 1 = 3, dfE = (r-1)(c-1) = 6.

**Solution:**

**Step 1: Data Table with Row and Column Totals.**

```
Plot / Row  | Variety A | Variety B | Variety C | Row Total (Ri)
------------+-----------+-----------+-----------+---------------
Plot 1      |     6     |     5     |     5     |      16
Plot 2      |     7     |     5     |     4     |      16
Plot 3      |     3     |     3     |     3     |       9
Plot 4      |     8     |     7     |     4     |      19
------------+-----------+-----------+-----------+---------------
Col Total Cj|    24     |    20     |    16     | Grand T = 60
```

Sum of squares of all 12 observations:
sum sum x^2 = 6^2 + 5^2 + 5^2 + 7^2 + 5^2 + 4^2 + 3^2 + 3^2 + 3^2 + 8^2 + 7^2 + 4^2
= 36 + 25 + 25 + 49 + 25 + 16 + 9 + 9 + 9 + 64 + 49 + 16 = 332.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 60^2 / 12 = 3600 / 12 = 300.00.
- SST = sum sum x^2 - CF = 332 - 300 = 32.00.
- SSC (Varieties) = (24^2 + 20^2 + 16^2) / 4 - CF = (576 + 400 + 256) / 4 - 300 = 1232 / 4 - 300 = 308 - 300 = 8.00.
- SSR (Plots) = (16^2 + 16^2 + 9^2 + 19^2) / 3 - CF = (256 + 256 + 81 + 361) / 3 - 300 = 954 / 3 - 300 = 318 - 300 = 18.00.
- SSE = SST - SSC - SSR = 32.00 - 8.00 - 18.00 = 6.00.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfC = 3 - 1 = 2 => MSC = 8.00 / 2 = 4.00.
- dfR = 4 - 1 = 3 => MSR = 18.00 / 3 = 6.00.
- dfE = 2 * 3 = 6 => MSE = 6.00 / 6 = 1.00.

**Step 4: Compute F Ratios.**
- F_varieties = MSC / MSE = 4.00 / 1.00 = 4.00.
- F_plots = MSR / MSE = 6.00 / 1.00 = 6.00.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Varieties (SSC)     |         8.00        |   2  |       4.00       |     4.00
Plots (SSR)         |        18.00        |   3  |       6.00       |     6.00
Error (SSE)         |         6.00        |   6  |       1.00       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        32.00        |  11  |                  |
```

**Step 6: Conclusions.**
- For Varieties: Calculated F = 4.00. Comparing with table value F0.05(2, 9) = 4.26 (or F0.05(2,6) = 5.14), calculated F = 4.00 < 4.26. Accept H0C. Variety differences are not significant at 5% level.
- For Plots: Calculated F = 6.00 > F0.05(3, 6) = 4.76. Reject H0R. Plot differences are significant at 5% level.

**Answer:** **Accept H0 for varieties (Calculated F = 4.00 < Table F = 4.26/5.14). Variety differences are not significant. Plot differences are significant (F = 6.00 > 4.76).**

**Check:** SST = 8 + 18 + 6 = 32.


## Paper 1 Q.10(b) [A4]: Two-Way ANOVA with Replication - Drug Effectiveness on Blood Pressure

**Given:** Effectiveness in reducing blood pressure for 3 drugs (X, Y, Z) tested across 3 groups of people (A, B, C) with 2 observations per cell (r=2 replicates):
- Group A: X(14, 15); Y(10, 9); Z(11, 11)
- Group B: X(12, 11); Y(7, 8); Z(10, 11)
- Group C: X(10, 11); Y(11, 11); Z(8, 7)
- Significance level: 5%
- Critical values given: F(2, 9) = 4.26, F(4, 9) = 3.63

**Formula / Method:**
- Factors: Groups (a=3), Drugs (b=3), Replicates (r=2). Total observations N = 3 * 3 * 2 = 18.
- Null hypotheses:
  1. H0A: No significant difference among groups of people.
  2. H0B: No significant difference among drugs.
  3. H0AB: No significant interaction effect between groups and drugs.
- CF = T^2 / N.
- SST = sum sum sum x^2 - CF.
- SSA = sum(Ri^2) / (b * r) - CF.
- SSB = sum(Cj^2) / (a * r) - CF.
- SScells = sum(CellTotal_ij^2) / r - CF.
- SSAB = SScells - SSA - SSB.
- SSE = SST - SScells.

**Solution:**

**Step 1: Cell Totals, Row Totals, Column Totals, and Sum of Squares.**

Cell Totals (Sum of r=2 replicates):
```
Group / Drug  |   Drug X    |   Drug Y    |   Drug Z    | Row Total (Ri)
--------------+-------------+-------------+-------------+---------------
Group A       | 14+15 = 29  | 10+9  = 19  | 11+11 = 22  |      70
Group B       | 12+11 = 23  | 7+8   = 15  | 10+11 = 21  |      59
Group C       | 10+11 = 21  | 11+11 = 22  | 8+7   = 15  |      58
--------------+-------------+-------------+-------------+---------------
Col Total (Cj)|     73      |     56      |     58      | Grand T = 187
```

Sum of squares of all 18 observations:
sum x^2 = (14^2+15^2+10^2+9^2+11^2+11^2) + (12^2+11^2+7^2+8^2+10^2+11^2) + (10^2+11^2+11^2+11^2+8^2+7^2)
= (196+225+100+81+121+121) + (144+121+49+64+100+121) + (100+121+121+121+64+49) = 944 + 599 + 476 = 2019.

**Step 2: Compute Correction Factor and Sums of Squares.**
- CF = T^2 / N = 187^2 / 18 = 34969 / 18 = 1942.72.
- SST = 2019 - 1942.72 = 76.28.
- SSA (Groups) = (70^2 + 59^2 + 58^2) / 6 - CF = (4900 + 3481 + 3364) / 6 - 1942.72 = 11745 / 6 - 1942.72 = 1957.50 - 1942.72 = 14.78.
- SSB (Drugs) = (73^2 + 56^2 + 58^2) / 6 - CF = (5329 + 3136 + 3364) / 6 - 1942.72 = 11829 / 6 - 1942.72 = 1971.50 - 1942.72 = 28.78.
- SScells = (29^2 + 19^2 + 22^2 + 23^2 + 15^2 + 21^2 + 21^2 + 22^2 + 15^2) / 2 - CF = (841 + 361 + 484 + 529 + 225 + 441 + 441 + 484 + 225) / 2 - CF = 4031 / 2 - 1942.72 = 2015.50 - 1942.72 = 72.78.
- SSAB (Interaction) = SScells - SSA - SSB = 72.78 - 14.78 - 28.78 = 29.22.
- SSE (Error) = SST - SScells = 76.28 - 72.78 = 3.50.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfA = a - 1 = 2 => MSA = 14.78 / 2 = 7.39.
- dfB = b - 1 = 2 => MSB = 28.78 / 2 = 14.39.
- dfAB = (a-1)(b-1) = 4 => MSAB = 29.22 / 4 = 7.31.
- dfE = a * b * (r-1) = 3 * 3 * 1 = 9 => MSE = 3.50 / 9 = 0.39.

**Step 4: Compute F ratios.**
- FA (Groups) = MSA / MSE = 7.3889 / 0.3889 = 19.00.
- FB (Drugs) = MSB / MSE = 14.3889 / 0.3889 = 37.00.
- FAB (Interaction) = MSAB / MSE = 7.3056 / 0.3889 = 18.79.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Groups (SSA)        |        14.78        |   2  |       7.39       |    19.00
Drugs (SSB)         |        28.78        |   2  |      14.39       |    37.00
Interaction (SSAB)  |        29.22        |   4  |       7.31       |    18.79
Error (SSE)         |         3.50        |   9  |       0.39       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        76.28        |  17  |                  |
```

**Step 6: Answers to Questions Asked.**
1. **Do the drugs act differently?**
   Calculated FB = 37.00 > F0.05(2, 9) = 4.26. Yes, drugs act significantly differently.
2. **Are the different groups of people affected differently?**
   Calculated FA = 19.00 > F0.05(2, 9) = 4.26. Yes, different groups of people are affected significantly differently.
3. **Is the interaction term significant?**
   Calculated FAB = 18.79 > F0.05(4, 9) = 3.63. Yes, the interaction term is significant.

**Answer:** **1) Drugs act differently (F = 37.00 > 4.26). 2) Groups affected differently (F = 19.00 > 4.26). 3) Interaction is significant (F = 18.79 > 3.63).**

**Check:** SSA + SSB + SSAB + SSE = 14.78 + 28.78 + 29.22 + 3.50 = 76.28 = SST.

# Paper 2

## Paper 2 Q.9(a) [A5]: One-Way ANOVA - Production of Three Wheat Varieties on 12 Plots

**Given:** Production in kgs of three wheat varieties A, B, C sown on 12 plots:
- Variety A (3 plots): 14, 16, 18
- Variety B (4 plots): 14, 13, 15, 22
- Variety C (5 plots): 18, 16, 19, 19, 22
- Significance level: 5%
- Critical table value: F0.05(2, 9) = 4.26

**Formula / Method:**
- H0: muA = muB = muC (No significant difference in production among the three varieties).
- Total observations N = 3 + 4 + 5 = 12, k = 3 groups.
- CF = T^2 / N.
- SST = sum x^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.
- F = MSB / MSE.

**Solution:**

**Step 1: Compute sample totals, sizes, and sums of squares.**

```
Variety  |  Observations (x)  | ni | Sample Total Ti | sum x_i^2
---------+--------------------+----+-----------------+-----------
A        | 14, 16, 18         |  3 |       48        | 196+256+324 = 776
B        | 14, 13, 15, 22     |  4 |       64        | 196+169+225+484 = 1074
C        | 18, 16, 19, 19, 22 |  5 |       94        | 324+256+361+361+484 = 1786
---------+--------------------+----+-----------------+-----------
Total    |                    | 12 | Grand T = 206   | sum x^2 = 3636
```

- T = 48 + 64 + 94 = 206.
- N = 12.
- Total sum x^2 = 776 + 1074 + 1786 = 3636.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 206^2 / 12 = 42436 / 12 = 3536.33.
- SST = 3636 - 3536.33 = 99.67.
- SSB = (48^2 / 3 + 64^2 / 4 + 94^2 / 5) - CF = (768 + 1024 + 1767.20) - 3536.33 = 3559.20 - 3536.33 = 22.87.
- SSE = SST - SSB = 99.67 - 22.87 = 76.80.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = k - 1 = 3 - 1 = 2 => MSB = 22.87 / 2 = 11.43.
- dfE = N - k = 12 - 3 = 9 => MSE = 76.80 / 9 = 8.53.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 11.4333 / 8.5333 = 1.34.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Varieties   |        22.87        |   2  |      11.43       |     1.34
Within Varieties    |        76.80        |   9  |       8.53       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        99.67        |  11  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 1.34 is less than the critical table value F0.05(2, 9) = 4.26.
- Accept H0. There is no significant difference in the mean production among the three varieties of wheat at 5% level.

**Answer:** **Accept H0. Calculated F = 1.34 < Table F = 4.26. Variety production differences are not significant.**

**Check:** scipy.stats.f_oneway gives F = 1.34.


## Paper 2 Q.9(b): Latin Square Design - Output of Wheat (4x4)

**Given:** Same statistics concerning output of wheat per field obtained under a 4x4 Latin square design with varieties A, B, C, D as in Paper 1 Q.9(b).

**Answer:** **Same as Paper 1 Q.9(b) [A2] answer: Varieties F = 9.24 > 4.76 (Significant differences among varieties). Rows F = 8.86 > 4.76 (Significant row differences). Columns F = 1.43 < 4.76 (No column differences).**


## Paper 2 Q.10(a) [A6]: Two-Way ANOVA - Doctors and Treatments Patient Recovery Days

**Given:** Four doctors each test four treatments for a certain disease and observe the recovery days of patients:
```
Doctor / Treatment | T1 | T2 | T3 | T4
-------------------+----+----+----+----
D1                 | 10 | 14 | 19 | 20
D2                 | 11 | 15 | 17 | 21
D3                 |  9 | 12 | 16 | 19
D4                 |  8 | 13 | 17 | 20
```
- Significance level: 5%
- Critical table value: F0.05(3, 9) = 3.86 for both doctors and treatments.

**Formula / Method:**
- Rows = Doctors (r=4), Columns = Treatments (c=4). Total N = 16.
- H0C: No significant difference among treatments.
- H0R: No significant difference among doctors.
- CF = T^2 / N.
- SST = sum sum x^2 - CF.
- SSC = sum(Cj^2) / r - CF.
- SSR = sum(Ri^2) / c - CF.
- SSE = SST - SSC - SSR.

**Solution:**

**Step 1: Compute Row and Column Totals.**

```
Doctor / Treatment | T1 | T2 | T3 | T4 | Row Total (Ri)
-------------------+----+----+----+----+---------------
D1                 | 10 | 14 | 19 | 20 |      63
D2                 | 11 | 15 | 17 | 21 |      64
D3                 |  9 | 12 | 16 | 19 |      56
D4                 |  8 | 13 | 17 | 20 |      58
-------------------+----+----+----+----+---------------
Col Total (Cj)     | 38 | 54 | 69 | 80 | Grand T = 241
```

Sum of squares of all 16 items:
sum sum x^2 = (10^2+14^2+19^2+20^2) + (11^2+15^2+17^2+21^2) + (9^2+12^2+16^2+19^2) + (8^2+13^2+17^2+20^2)
= 1057 + 1076 + 842 + 922 = 3897.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 241^2 / 16 = 58081 / 16 = 3630.0625.
- SST = 3897 - 3630.0625 = 266.94.
- SSC (Treatments) = (38^2 + 54^2 + 69^2 + 80^2) / 4 - CF = 15521 / 4 - 3630.0625 = 3880.25 - 3630.0625 = 250.19.
- SSR (Doctors) = (63^2 + 64^2 + 56^2 + 58^2) / 4 - CF = 14565 / 4 - 3630.0625 = 3641.25 - 3630.0625 = 11.19.
- SSE = SST - SSC - SSR = 266.9375 - 250.1875 - 11.1875 = 5.56.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfC = 4 - 1 = 3 => MSC = 250.1875 / 3 = 83.40.
- dfR = 4 - 1 = 3 => MSR = 11.1875 / 3 = 3.73.
- dfE = (4-1)(4-1) = 9 => MSE = 5.5625 / 9 = 0.62.

**Step 4: Compute F Ratios.**
- F_treatments = MSC / MSE = 83.3958 / 0.6181 = 134.93.
- F_doctors = MSR / MSE = 3.7292 / 0.6181 = 6.03.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Treatments (SSC)    |       250.19        |   3  |      83.40       |    134.93
Doctors (SSR)       |        11.19        |   3  |       3.73       |      6.03
Error (SSE)         |         5.56        |   9  |       0.62       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       266.94        |  15  |                  |
```

**Step 6: Conclusions.**
- Critical table value is F0.05(3, 9) = 3.86.
- For Treatments: Calculated F = 134.93 > 3.86. Reject H0C. There is a significant difference among treatments.
- For Doctors: Calculated F = 6.03 > 3.86. Reject H0R. There is a significant difference among doctors.

**Answer:** **Treatments F = 134.93 > 3.86 (Significant difference among treatments). Doctors F = 6.03 > 3.86 (Significant difference among doctors).**

**Check:** 250.1875 + 11.1875 + 5.5625 = 266.9375 = SST.


## Paper 2 Q.10(b) [A7]: One-Way ANOVA - Anesthesia Types and Length of Hospital Stay

**Given:** Frequency distribution of post-operative hospital stay (in days) for cesarean patients across four anesthesia groups (A, B, C, D):
- Group A (Epidural MS): stay 3 days => 6 patients; stay 4 days => 14 patients. (Total nA = 20)
- Group B (Epidural): stay 4 days => 18 patients; stay 5 days => 2 patients. (Total nB = 20)
- Group C (Spinal): stay 4 days => 10 patients; stay 5 days => 9 patients; stay 6 days => 1 patient. (Total nC = 20)
- Group D (General): stay 4 days => 8 patients; stay 5 days => 12 patients. (Total nD = 20)
- Significance level: alpha = 0.01
- Critical table value: F0.01(3, 76) = 4.13

**Formula / Method:**
- Expand frequency distribution into N = 20 * 4 = 80 total observations across k = 4 groups.
- H0: muA = muB = muC = muD (No effect due to anesthesia type).
- CF = T^2 / N.
- SST = sum x^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.

**Solution:**

**Step 1: Compute group totals and sum of squares for each group.**

- Group A: TA = (3 * 6) + (4 * 14) = 18 + 56 = 74.
  sum xA^2 = (3^2 * 6) + (4^2 * 14) = 54 + 224 = 278.
- Group B: TB = (4 * 18) + (5 * 2) = 72 + 10 = 82.
  sum xB^2 = (4^2 * 18) + (5^2 * 2) = 288 + 50 = 338.
- Group C: TC = (4 * 10) + (5 * 9) + (6 * 1) = 40 + 45 + 6 = 91.
  sum xC^2 = (4^2 * 10) + (5^2 * 9) + (6^2 * 1) = 160 + 225 + 36 = 421.
- Group D: TD = (4 * 8) + (5 * 12) = 32 + 60 = 92.
  sum xD^2 = (4^2 * 8) + (5^2 * 12) = 128 + 300 = 428.

Summary of totals:
- Grand Total T = 74 + 82 + 91 + 92 = 339.
- Total observations N = 20 + 20 + 20 + 20 = 80.
- Total sum of squares sum x^2 = 278 + 338 + 421 + 428 = 1465.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 339^2 / 80 = 114921 / 80 = 1436.5125.
- SST = 1465 - 1436.5125 = 28.49.
- SSB = (74^2 + 82^2 + 91^2 + 92^2) / 20 - CF = 28945 / 20 - 1436.5125 = 1447.25 - 1436.5125 = 10.74.
- SSE = SST - SSB = 28.4875 - 10.7375 = 17.75.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = k - 1 = 4 - 1 = 3 => MSB = 10.7375 / 3 = 3.58.
- dfE = N - k = 80 - 4 = 76 => MSE = 17.75 / 76 = 0.23.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 3.579167 / 0.233553 = 15.32.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Groups (SSB)|        10.74        |   3  |       3.58       |    15.32
Within Groups (SSE) |        17.75        |  76  |       0.23       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        28.49        |  79  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 15.32 is much greater than the critical table value F0.01(3, 76) = 4.13.
- Reject H0 at 1% significance level.
- There exists a highly significant effect on the length of hospital stay due to the anesthesia type.

**Answer:** **Reject H0. Calculated F = 15.32 > Table F = 4.13. Significant effect due to anesthesia type.**

**Check:** Total N=80, SST = 10.7375 + 17.7500 = 28.4875.

# Paper 3

## Paper 3 Q.9(a) [A8]: One-Way ANOVA - Wheat Varieties Yields in Four Plots

**Given:** Yields in quintals per acre of 3 wheat varieties (A, B, C) grown in 4 plots each:
- Variety A: 8, 4, 6, 7
- Variety B: 7, 6, 5, 3
- Variety C: 2, 5, 4, 4
- Level of significance: 5%
- Critical table value: F0.05(2, 9) = 4.26

**Formula / Method:**
- H0: muA = muB = muC (No significant difference between variety yields).
- Direct method for one-way ANOVA. N = 3 * 4 = 12, k = 3.
- CF = T^2 / N.
- SST = sum x^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.

**Solution:**

**Step 1: Compute sample totals and sum of squares.**

```
Variety (x) | Observations (x) | ni | Sample Total Ti | sum x_i^2
------------+------------------+----+-----------------+-----------
A           | 8, 4, 6, 7       |  4 |       25        | 64+16+36+49 = 165
B           | 7, 6, 5, 3       |  4 |       21        | 49+36+25+9  = 119
C           | 2, 5, 4, 4       |  4 |       15        | 4+25+16+16  =  61
------------+------------------+----+-----------------+-----------
Total       |                  | 12 | Grand T = 61    | sum x^2 = 345
```

- T = 25 + 21 + 15 = 61.
- N = 12.
- Total sum x^2 = 165 + 119 + 61 = 345.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 61^2 / 12 = 3721 / 12 = 310.08.
- SST = 345 - 310.08 = 34.92.
- SSB = (25^2 + 21^2 + 15^2) / 4 - CF = 1291 / 4 - 310.08 = 322.75 - 310.08 = 12.67.
- SSE = SST - SSB = 34.92 - 12.67 = 22.25.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = 3 - 1 = 2 => MSB = 12.67 / 2 = 6.33.
- dfE = 12 - 3 = 9 => MSE = 22.25 / 9 = 2.47.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 6.3333 / 2.4722 = 2.56.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Varieties   |        12.67        |   2  |       6.33       |     2.56
Within Varieties    |        22.25        |   9  |       2.47       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        34.92        |  11  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 2.56 is less than the critical table value F0.05(2, 9) = 4.26.
- Accept H0. There is no significant difference between the yields of the three wheat varieties.

**Answer:** **Accept H0. Calculated F = 2.56 < Table F = 4.26. Variety yield differences are not significant.**

**Check:** scipy.stats.f_oneway yields F = 2.56.


## Paper 3 Q.9(b) [A9]: Latin Square Design - Five Fertilizers on Plots of Different Fertility (5x5)

**Given:** Results of a 5x5 Latin square design experiment conducted in respect of five fertilizers (A, B, C, D, E) used on plots of different fertility:
```
  A(16)  B(10)  C(11)  D(9)   E(9)
  E(10)  C(9)   A(14)  B(12)  D(11)
  B(15)  D(8)   E(8)   C(10)  A(18)
  D(12)  E(6)   B(13)  A(13)  C(12)
  C(13)  A(11)  D(10)  E(7)   B(14)
```
- Significance level: 5%
- Critical table value: F0.05(4, 12) = 3.26

**Formula / Method:**
- Rows (n=5), Columns (n=5), Treatments (n=5). Total N = n^2 = 25.
- Null hypotheses:
  - H0R: No significant difference among row fertility levels.
  - H0C: No significant difference among columns.
  - H0Tr: No significant difference among fertilizer treatments (A, B, C, D, E).
- CF = T^2 / N.
- SST = sum sum x^2 - CF.
- SSR = sum(Ri^2) / n - CF, SSC = sum(Cj^2) / n - CF, SSTr = sum(Trk^2) / n - CF.
- SSE = SST - SSR - SSC - SSTr.
- dfR = dfC = dfTr = 4, dfE = (5-1)(5-2) = 12.

**Solution:**

**Step 1: Compute Row, Column, and Treatment Totals.**

Data grid with row totals and column totals:
```
         Col 1   Col 2   Col 3   Col 4   Col 5   | Row Total
-------------------------------------------------+----------
Row 1  | A(16)   B(10)   C(11)   D(9)    E(9)    |    55
Row 2  | E(10)   C(9)    A(14)   B(12)   D(11)   |    56
Row 3  | B(15)   D(8)    E(8)    C(10)   A(18)   |    59
Row 4  | D(12)   E(6)    B(13)   A(13)   C(12)   |    56
Row 5  | C(13)   A(11)   D(10)   E(7)    B(14)   |    55
-------------------------------------------------+----------
Col T  |   66      44      56      51      64    | Grand T = 281
```

Treatment Totals (Sum for each letter):
- Fertilizer A: 16 + 14 + 18 + 13 + 11 = 72
- Fertilizer B: 10 + 12 + 15 + 13 + 14 = 64
- Fertilizer C: 11 + 9 + 10 + 12 + 13 = 55
- Fertilizer D: 9 + 11 + 8 + 12 + 10 = 50
- Fertilizer E: 9 + 10 + 8 + 6 + 7 = 40
- Check total: 72 + 64 + 55 + 50 + 40 = 281 = T.

Sum of squares of all 25 items:
sum sum x^2 = (16^2+10^2+11^2+9^2+9^2) + (10^2+9^2+14^2+12^2+11^2) + (15^2+8^2+8^2+10^2+18^2) + (12^2+6^2+13^2+13^2+12^2) + (13^2+11^2+10^2+7^2+14^2)
= 627 + 583 + 837 + 662 + 646 = 3355.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 281^2 / 25 = 78961 / 25 = 3158.44.
- SST = 3355 - 3158.44 = 196.56.
- SSR = (55^2 + 56^2 + 59^2 + 56^2 + 55^2) / 5 - CF = 15803 / 5 - 3158.44 = 3160.60 - 3158.44 = 2.16.
- SSC = (66^2 + 44^2 + 56^2 + 51^2 + 64^2) / 5 - CF = 16125 / 5 - 3158.44 = 3225.00 - 3158.44 = 66.56.
- SSTr = (72^2 + 64^2 + 55^2 + 50^2 + 40^2) / 5 - CF = 16405 / 5 - 3158.44 = 3281.00 - 3158.44 = 122.56.
- SSE = SST - SSR - SSC - SSTr = 196.56 - 2.16 - 66.56 - 122.56 = 5.28.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfR = 4 => MSR = 2.16 / 4 = 0.54.
- dfC = 4 => MSC = 66.56 / 4 = 16.64.
- dfTr = 4 => MSTr = 122.56 / 4 = 30.64.
- dfE = 12 => MSE = 5.28 / 12 = 0.44.

**Step 4: Compute F ratios.**
- FR (Rows) = MSR / MSE = 0.54 / 0.44 = 1.23.
- FC (Columns) = MSC / MSE = 16.64 / 0.44 = 37.82.
- FTr (Fertilizers) = MSTr / MSE = 30.64 / 0.44 = 69.64.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Rows (SSR)          |         2.16        |   4  |       0.54       |     1.23
Columns (SSC)       |        66.56        |   4  |      16.64       |    37.82
Fertilizers (SSTr)  |       122.56        |   4  |      30.64       |    69.64
Error (SSE)         |         5.28        |  12  |       0.44       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       196.56        |  24  |                  |
```

**Step 6: Conclusions.**
- Critical table value is F0.05(4, 12) = 3.26.
- Fertilizers: Calculated FTr = 69.64 > 3.26. Highly significant difference among fertilizers.
- Columns: Calculated FC = 37.82 > 3.26. Significant difference among columns.
- Rows: Calculated FR = 1.23 < 3.26. No significant difference among row fertility levels.

**Answer:** **Fertilizers F = 69.64 > 3.26 (Fertilizer differences are significant). Columns F = 37.82 > 3.26 (Significant). Rows F = 1.23 < 3.26 (Not significant).**

**Check:** 2.16 + 66.56 + 122.56 + 5.28 = 196.56 = SST.


## Paper 3 Q.10(a) [A10]: Two-Way ANOVA with Coding - Land Pieces and Treatments

**Given:** Yield data for four treatments (A, B, C, D) across three pieces of land (P, Q, R):
- Land P: A=45, B=40, C=38, D=37
- Land Q: A=43, B=41, C=45, D=38
- Land R: A=39, B=39, C=41, D=41
- Required method: Coding method subtracting 40 from all observations (u_ij = x_ij - 40).
- Critical table values: For treatments F0.05(3, 6) = 4.76; for land F0.05(2, 6) = 5.14.

**Formula / Method:**
- Shifting origin by subtracting a constant c=40 does not change the ANOVA sums of squares, mean squares, or F ratios.
- Rows = Pieces of land (r=3), Columns = Treatments (c=4). Total N = 12.
- CF = Tu^2 / N.
- SST = sum sum u^2 - CF.
- SSC = sum(Cj^2) / r - CF, SSR = sum(Ri^2) / c - CF.
- SSE = SST - SSC - SSR.

**Solution:**

**Step 1: Code the data by subtracting 40 from each observation.**

Original Data:
```
Land / Treatment |  A  |  B  |  C  |  D
-----------------+-----+-----+-----+----
P                | 45  | 40  | 38  | 37
Q                | 43  | 41  | 45  | 38
R                | 39  | 39  | 41  | 41
```

Coded Data (u_ij = x_ij - 40):
```
Land / Treatment |  A  |  B  |  C  |  D  | Row Total (Ri)
-----------------+-----+-----+-----+-----+---------------
P                |  5  |  0  | -2  | -3  |       0
Q                |  3  |  1  |  5  | -2  |       7
R                | -1  | -1  |  1  |  1  |       0
-----------------+-----+-----+-----+-----+---------------
Col Total (Cj)   |  7  |  0  |  4  | -4  | Grand Tu = 7
```

Sum of squares of coded items sum sum u^2:
- Row P: 5^2 + 0^2 + (-2)^2 + (-3)^2 = 25 + 0 + 4 + 9 = 38
- Row Q: 3^2 + 1^2 + 5^2 + (-2)^2 = 9 + 1 + 25 + 4 = 39
- Row R: (-1)^2 + (-1)^2 + 1^2 + 1^2 = 1 + 1 + 1 + 1 = 4
- Total sum sum u^2 = 38 + 39 + 4 = 81.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = Tu^2 / N = 7^2 / 12 = 49 / 12 = 4.0833.
- SST = 81 - 4.0833 = 76.92.
- SSC (Treatments) = (7^2 + 0^2 + 4^2 + (-4)^2) / 3 - CF = 81 / 3 - 4.0833 = 27.00 - 4.0833 = 22.92.
- SSR (Land) = (0^2 + 7^2 + 0^2) / 4 - CF = 49 / 4 - 4.0833 = 12.25 - 4.0833 = 8.17.
- SSE = SST - SSC - SSR = 76.9167 - 22.9167 - 8.1667 = 45.83.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfC = 4 - 1 = 3 => MSC = 22.9167 / 3 = 7.64.
- dfR = 3 - 1 = 2 => MSR = 8.1667 / 2 = 4.08.
- dfE = (3-1)(4-1) = 6 => MSE = 45.8333 / 6 = 7.64.

**Step 4: Compute F Ratios.**
- F_treatments = MSC / MSE = 7.6389 / 7.6389 = 1.00.
- F_land = MSR / MSE = 4.0833 / 7.6389 = 0.53.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Treatments (SSC)    |        22.92        |   3  |       7.64       |     1.00
Land Pieces (SSR)   |         8.17        |   2  |       4.08       |     0.53
Error (SSE)         |        45.83        |   6  |       7.64       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        76.92        |  11  |                  |
```

**Step 6: Conclusions.**
- For Treatments: Calculated F = 1.00 < F0.05(3, 6) = 4.76. Accept H0. Treatment differences are not significant.
- For Land Pieces: Calculated F = 0.53 < F0.05(2, 6) = 5.14. Accept H0. Differences among land pieces are not significant.

**Answer:** **Accept H0 for both. Treatments F = 1.00 < 4.76; Land F = 0.53 < 5.14. Neither treatment nor land differences are significant.**

**Check:** 22.9167 + 8.1667 + 45.8333 = 76.9167 = SST.


## Paper 3 Q.10(b) [A11]: One-Way ANOVA with Coding - Brand Preferences of Power

**Given:** Sales of three main brands of power (Brand I, Brand II, Brand III) examined across four groups (A, B, C, D):
- Brand I: A=0, B=4, C=8, D=15
- Brand II: A=5, B=8, C=13, D=6
- Brand III: A=18, B=19, C=11, D=13
- Required method: Subtract 10 as code value (u = x - 10) and apply one-way ANOVA across the 3 brands (samples with ni = 4 each).
- Level of significance: 5%
- Critical table value: F0.05(2, 9) = 4.26

**Formula / Method:**
- Three brands are the three treatment groups (k=3), each with ni = 4 observations. N = 12.
- Code u_ij = x_ij - 10.
- H0: muI = muII = muIII (No significant difference in brand preferences).
- CF = Tu^2 / N.
- SST = sum u^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.

**Solution:**

**Step 1: Subtract 10 from each observation to get coded data.**

Coded Observations (u = x - 10):
- Brand I: 0-10 = -10, 4-10 = -6, 8-10 = -2, 15-10 = 5.
  T1 = -10 - 6 - 2 + 5 = -13.
  sum u1^2 = (-10)^2 + (-6)^2 + (-2)^2 + 5^2 = 100 + 36 + 4 + 25 = 165.
- Brand II: 5-10 = -5, 8-10 = -2, 13-10 = 3, 6-10 = -4.
  T2 = -5 - 2 + 3 - 4 = -8.
  sum u2^2 = (-5)^2 + (-2)^2 + 3^2 + (-4)^2 = 25 + 4 + 9 + 16 = 54.
- Brand III: 18-10 = 8, 19-10 = 9, 11-10 = 1, 13-10 = 3.
  T3 = 8 + 9 + 1 + 3 = 21.
  sum u3^2 = 8^2 + 9^2 + 1^2 + 3^2 = 64 + 81 + 1 + 9 = 155.

Summary:
- Grand Coded Total Tu = T1 + T2 + T3 = -13 - 8 + 21 = 0.
- Total N = 12.
- Total sum of squared coded items sum u^2 = 165 + 54 + 155 = 374.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = Tu^2 / N = 0^2 / 12 = 0.00.
- SST = 374 - 0 = 374.00.
- SSB = ((-13)^2 + (-8)^2 + 21^2) / 4 - 0 = (169 + 64 + 441) / 4 = 674 / 4 = 168.50.
- SSE = SST - SSB = 374.00 - 168.50 = 205.50.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = k - 1 = 3 - 1 = 2 => MSB = 168.50 / 2 = 84.25.
- dfE = N - k = 12 - 3 = 9 => MSE = 205.50 / 9 = 22.83.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 84.25 / 22.8333 = 3.69.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Brands (SSB)|       168.50        |   2  |      84.25       |     3.69
Within Brands (SSE) |       205.50        |   9  |      22.83       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       374.00        |  11  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 3.69 is less than the critical table value F0.05(2, 9) = 4.26.
- Accept H0 at 5% significance level.
- There is no significant difference in brand preferences.

**Answer:** **Accept H0. Calculated F = 3.69 < Table F = 4.26. Brand preferences do not differ significantly.**

**Check:** scipy.stats.f_oneway gives F = 3.6898.

# Paper 4

## Paper 4 Q.9(a): Two-Way ANOVA with Replication - Drug Effectiveness on Blood Pressure

**Given:** Same information relating to three drugs testing effectiveness in reducing blood pressure across three groups of people with 2 replicates per cell as in Paper 1 Q.10(b).

**Answer:** **Same as Paper 1 Q.10(b) [A4] answer: 1) Drugs act differently (F = 37.00 > 4.26). 2) Groups affected differently (F = 19.00 > 4.26). 3) Interaction is significant (F = 18.79 > 3.63).**


## Paper 4 Q.9(b) [A12]: Latin Square Design - Five Fertilizers (5x5)

**Given:** Same 5x5 Latin square design results for five fertilizers on plots of different fertility as in Paper 3 Q.9(b).

**Answer:** **Same as Paper 3 Q.9(b) [A9] answer: Fertilizers F = 69.64 > 3.26 (Fertilizer differences are significant). Columns F = 37.82 > 3.26 (Significant). Rows F = 1.23 < 3.26 (Not significant).**


## Paper 4 Q.10(a) [A13]: One-Way ANOVA - Comparison of Deaths in Three Hospitals

**Given:** Number of deaths per month in three hospitals A, B, C:
- Hospital A: 3, 4, 3, 5, 0
- Hospital B: 6, 3, 3, 4, 4
- Hospital C: 7, 3, 4, 6, 5
- Significance level: 5%
- Critical table value: F0.05(2, 12) = 3.89

**Formula / Method:**
- H0: muA = muB = muC (No significant difference in average deaths per month among the three hospitals).
- One-way ANOVA with k=3 groups, nA = nB = nC = 5, N = 15.
- CF = T^2 / N.
- SST = sum x^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.

**Solution:**

**Step 1: Compute sample totals and sum of squares.**

```
Hospital | Observations (x) | ni | Sample Total Ti | sum x_i^2
---------+------------------+----+-----------------+-----------
A        | 3, 4, 3, 5, 0    |  5 |       15        | 9+16+9+25+0  =  59
B        | 6, 3, 3, 4, 4    |  5 |       20        | 36+9+9+16+16 =  86
C        | 7, 3, 4, 6, 5    |  5 |       25        | 49+9+16+36+25 = 135
---------+------------------+----+-----------------+-----------
Total    |                  | 15 | Grand T = 60    | sum x^2 = 280
```

- T = 15 + 20 + 25 = 60.
- N = 15.
- Total sum x^2 = 59 + 86 + 135 = 280.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 60^2 / 15 = 3600 / 15 = 240.00.
- SST = 280 - 240 = 40.00.
- SSB = (15^2 + 20^2 + 25^2) / 5 - CF = 1250 / 5 - 240 = 250 - 240 = 10.00.
- SSE = SST - SSB = 40.00 - 10.00 = 30.00.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = k - 1 = 3 - 1 = 2 => MSB = 10.00 / 2 = 5.00.
- dfE = N - k = 15 - 3 = 12 => MSE = 30.00 / 12 = 2.50.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 5.00 / 2.50 = 2.00.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Hospitals   |        10.00        |   2  |       5.00       |     2.00
Within Hospitals    |        30.00        |  12  |       2.50       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        40.00        |  14  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 2.00 is less than the critical table value F0.05(2, 12) = 3.89.
- Accept H0 at 5% significance level.
- There is no significant difference in the mean number of deaths per month among the three hospitals.

**Answer:** **Accept H0. Calculated F = 2.00 < Table F = 3.89. Differences in hospital deaths are not significant.**

**Check:** scipy.stats.f_oneway gives F = 2.00.


## Paper 4 Q.10(b): Latin Square Design - Output of Wheat (4x4)

**Given:** Same statistics concerning output of wheat per field obtained under a 4x4 Latin square design as in Paper 1 Q.9(b).

**Answer:** **Same as Paper 1 Q.9(b) [A2] answer: Varieties F = 9.24 > 4.76 (Significant differences among varieties). Rows F = 8.86 > 4.76 (Significant row differences). Columns F = 1.43 < 4.76 (No column differences).**


# Paper 5

## Paper 5 Q.9(a) [A14]: One-Way ANOVA - Three Types of Fertilizers on Plant Growth

**Given:** Growth of plants (for 6 weeks) tested under three types of fertilizers:
- Fertilizer 1: 6, 8, 4, 5, 3, 4
- Fertilizer 2: 8, 12, 9, 11, 6, 8
- Fertilizer 3: 13, 9, 11, 8, 7, 12
- Level of significance: 5%
- Critical table value: F0.05(2, 15) = 3.68

**Formula / Method:**
- H0: mu1 = mu2 = mu3 (No significant difference in mean plant growth among fertilizers).
- k = 3, n1 = n2 = n3 = 6, N = 18.
- CF = T^2 / N.
- SST = sum x^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.

**Solution:**

**Step 1: Compute sample totals and sum of squares.**

```
Fertilizer | Observations (x)  | ni | Sample Total Ti | sum x_i^2
-----------+-------------------+----+-----------------+-----------
F1         | 6, 8, 4, 5, 3, 4  |  6 |       30        | 36+64+16+25+9+16 = 166
F2         | 8, 12, 9, 11, 6, 8|  6 |       54        | 64+144+81+121+36+64 = 510
F3         | 13, 9, 11, 8, 7,12|  6 |       60        | 169+81+121+64+49+144 = 628
-----------+-------------------+----+-----------------+-----------
Total      |                   | 18 | Grand T = 144   | sum x^2 = 1304
```

- T = 30 + 54 + 60 = 144.
- N = 18.
- Total sum x^2 = 166 + 510 + 628 = 1304.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 144^2 / 18 = 20736 / 18 = 1152.00.
- SST = 1304 - 1152 = 152.00.
- SSB = (30^2 + 54^2 + 60^2) / 6 - CF = 7416 / 6 - 1152 = 1236 - 1152 = 84.00.
- SSE = SST - SSB = 152.00 - 84.00 = 68.00.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = 3 - 1 = 2 => MSB = 84.00 / 2 = 42.00.
- dfE = 18 - 3 = 15 => MSE = 68.00 / 15 = 4.53.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 42.00 / 4.5333 = 9.26.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Fertilizers |        84.00        |   2  |      42.00       |     9.26
Within Fertilizers  |        68.00        |  15  |       4.53       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       152.00        |  17  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 9.26 is greater than the critical table value F0.05(2, 15) = 3.68.
- Reject H0 at 5% significance level.
- There is a significant difference in mean plant growth among the three fertilizers.

**Answer:** **Reject H0. Calculated F = 9.26 > Table F = 3.68. Mean plant growth differs significantly across fertilizers.**

**Check:** scipy.stats.f_oneway gives F = 9.26.


## Paper 5 Q.9(b) [A15]: Two-Way ANOVA - Muskrats Quarantined Worms

**Given:** Number of worms quarantined from areas of four groups of muskrats (Columns I, II, III, IV) across five rows:
```
Row / Col | Col I | Col II | Col III | Col IV
----------+-------+--------+---------+-------
Row 1     |  33   |   41   |   12    |   38
Row 2     |  32   |   38   |   35    |   43
Row 3     |  26   |   40   |   46    |   25
Row 4     |  14   |   23   |   22    |   13
Row 5     |  30   |   21   |   11    |   26
```
- Level of significance: 5%
- Critical table values given: F0.05(4, 12) = 3.26 for rows; F0.05(3, 12) = 3.49 for columns.

**Formula / Method:**
- Rows (r=5), Columns (c=4). Total N = 5 * 4 = 20.
- H0R: No significant difference among rows.
- H0C: No significant difference among columns (muskrat groups).
- CF = T^2 / N.
- SST = sum sum x^2 - CF.
- SSR = sum(Ri^2) / c - CF, SSC = sum(Cj^2) / r - CF.
- SSE = SST - SSR - SSC.

**Solution:**

**Step 1: Compute Row and Column Totals.**

```
Row / Col | Col I | Col II | Col III | Col IV | Row Total (Ri)
----------+-------+--------+---------+--------+---------------
Row 1     |  33   |   41   |   12    |   38   |     124
Row 2     |  32   |   38   |   35    |   43   |     148
Row 3     |  26   |   40   |   46    |   25   |     137
Row 4     |  14   |   23   |   22    |   13   |      72
Row 5     |  30   |   21   |   11    |   26   |      88
----------+-------+--------+---------+--------+---------------
Col T (Cj)| 135   |  163   |  126    |  145   | Grand T = 569
```

Sum of squares of all 20 items:
sum sum x^2 = (33^2+41^2+12^2+38^2) + (32^2+38^2+35^2+43^2) + (26^2+40^2+46^2+25^2) + (14^2+23^2+22^2+13^2) + (30^2+21^2+11^2+26^2)
= 4338 + 5542 + 5017 + 1378 + 2163 = 18433.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 569^2 / 20 = 323761 / 20 = 16188.05.
- SST = 18433 - 16188.05 = 2244.95.
- SSR (Rows) = (124^2 + 148^2 + 137^2 + 72^2 + 88^2) / 4 - CF = 68977 / 4 - 16188.05 = 17244.25 - 16188.05 = 1056.20.
- SSC (Columns) = (135^2 + 163^2 + 126^2 + 145^2) / 5 - CF = 81695 / 5 - 16188.05 = 16339.00 - 16188.05 = 150.95.
- SSE = SST - SSR - SSC = 2244.95 - 1056.20 - 150.95 = 1037.80.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfR = 5 - 1 = 4 => MSR = 1056.20 / 4 = 264.05.
- dfC = 4 - 1 = 3 => MSC = 150.95 / 3 = 50.32.
- dfE = (5-1)(4-1) = 12 => MSE = 1037.80 / 12 = 86.48.

**Step 4: Compute F Ratios.**
- F_rows = MSR / MSE = 264.05 / 86.4833 = 3.05.
- F_cols = MSC / MSE = 50.3167 / 86.4833 = 0.58.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Rows (SSR)          |       1056.20       |   4  |      264.05      |     3.05
Columns (SSC)       |        150.95       |   3  |       50.32      |     0.58
Error (SSE)         |       1037.80       |  12  |       86.48      |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       2244.95       |  19  |                  |
```

**Step 6: Conclusions.**
- For Rows (df = 4, 12): Calculated FR = 3.05 < F0.05(4, 12) = 3.26. Accept H0R. Row differences are not significant.
- For Columns (df = 3, 12): Calculated FC = 0.58 < F0.05(3, 12) = 3.49. Accept H0C. Column differences are not significant.

**Answer:** **Accept H0 for both. Rows F = 3.05 < 3.26; Columns F = 0.58 < 3.49. Neither row nor column differences are significant.**

**Check:** 1056.20 + 150.95 + 1037.80 = 2244.95 = SST.


## Paper 5 Q.10(a) [A16]: One-Way ANOVA - Weight Loss Across Four Diets

**Given:** Trial to check the effects of four different diets on weight loss:
- Low fat: 8, 9, 6, 7, 3
- Low calorie: 2, 4, 3, 5, 1
- Low protein: 3, 5, 4, 2, 3
- Low carbohydrate: 2, 2, -1, 0, 3
- Level of significance: 5%
- Critical table value: F0.05(3, 16) = 3.24

**Formula / Method:**
- H0: mu1 = mu2 = mu3 = mu4 (Average weight loss is equal across all four diets).
- k = 4, ni = 5 for each group, N = 20.
- CF = T^2 / N.
- SST = sum x^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.

**Solution:**

**Step 1: Compute group totals and sum of squares.**

```
Diet Group        | Observations (x)   | ni | Sample Total Ti | sum x_i^2
------------------+--------------------+----+-----------------+-----------
Low fat           | 8, 9, 6, 7, 3      |  5 |       33        | 64+81+36+49+9 = 239
Low calorie       | 2, 4, 3, 5, 1      |  5 |       15        | 4+16+9+25+1 = 55
Low protein       | 3, 5, 4, 2, 3      |  5 |       17        | 9+25+16+4+9 = 63
Low carbohydrate  | 2, 2, -1, 0, 3     |  5 |        6        | 4+4+1+0+9 = 18
------------------+--------------------+----+-----------------+-----------
Total             |                    | 20 | Grand T = 71    | sum x^2 = 375
```

- T = 33 + 15 + 17 + 6 = 71.
- N = 20.
- Total sum x^2 = 239 + 55 + 63 + 18 = 375.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 71^2 / 20 = 5041 / 20 = 252.05.
- SST = 375 - 252.05 = 122.95.
- SSB = (33^2 + 15^2 + 17^2 + 6^2) / 5 - CF = 1639 / 5 - 252.05 = 327.80 - 252.05 = 75.75.
- SSE = SST - SSB = 122.95 - 75.75 = 47.20.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = k - 1 = 4 - 1 = 3 => MSB = 75.75 / 3 = 25.25.
- dfE = N - k = 20 - 4 = 16 => MSE = 47.20 / 16 = 2.95.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 25.25 / 2.95 = 8.56.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Diets (SSB) |        75.75        |   3  |      25.25       |     8.56
Within Diets (SSE)  |        47.20        |  16  |       2.95       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       122.95        |  19  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 8.56 is greater than the critical table value F0.05(3, 16) = 3.24.
- Reject H0 at 5% significance level.
- There is a significant difference in average weight loss among the four diets.

**Answer:** **Reject H0. Calculated F = 8.56 > Table F = 3.24. Weight loss differs significantly across diets.**

**Check:** scipy.stats.f_oneway gives F = 8.56.


## Paper 5 Q.10(b): Latin Square Design - Output of Wheat (4x4)

**Given:** Same statistics concerning output of wheat per field obtained under a 4x4 Latin square design as in Paper 1 Q.9(b).

**Answer:** **Same as Paper 1 Q.9(b) [A2] answer: Varieties F = 9.24 > 4.76 (Significant differences among varieties). Rows F = 8.86 > 4.76 (Significant row differences). Columns F = 1.43 < 4.76 (No column differences).**

# Paper 6

## Paper 6 Q.9(a) [A17]: One-Way ANOVA - Production Output of Three Machines

**Given:** Hourly production figures observed from three machines of different makes:
- Machine A: 25, 30, 36, 38, 31
- Machine B: 31, 39, 38, 42, 35
- Machine C: 24, 30, 28, 25, 28
- Level of significance: 5%
- Critical table value: F0.05(2, 12) = 3.89

**Formula / Method:**
- H0: muA = muB = muC (No significant difference in mean hourly production among machines).
- One-way ANOVA with k = 3 groups, nA = nB = nC = 5, N = 15.
- CF = T^2 / N.
- SST = sum x^2 - CF.
- SSB = sum (Ti^2 / ni) - CF.
- SSE = SST - SSB.

**Solution:**

**Step 1: Compute sample totals and sum of squares.**

```
Machine | Observations (x)   | ni | Sample Total Ti | sum x_i^2
--------+--------------------+----+-----------------+-----------
A       | 25, 30, 36, 38, 31 |  5 |       160       | 625+900+1296+1444+961 = 5226
B       | 31, 39, 38, 42, 35 |  5 |       185       | 961+1521+1444+1764+1225 = 6915
C       | 24, 30, 28, 25, 28 |  5 |       135       | 576+900+784+625+784 = 3669
--------+--------------------+----+-----------------+-----------
Total   |                    | 15 | Grand T = 480   | sum x^2 = 15810
```

- T = 160 + 185 + 135 = 480.
- N = 15.
- Total sum x^2 = 5226 + 6915 + 3669 = 15810.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = T^2 / N = 480^2 / 15 = 230400 / 15 = 15360.00.
- SST = 15810 - 15360 = 450.00.
- SSB = (160^2 + 185^2 + 135^2) / 5 - CF = 78050 / 5 - 15360 = 15610 - 15360 = 250.00.
- SSE = SST - SSB = 450.00 - 250.00 = 200.00.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfB = k - 1 = 3 - 1 = 2 => MSB = 250.00 / 2 = 125.00.
- dfE = N - k = 15 - 3 = 12 => MSE = 200.00 / 12 = 16.67.

**Step 4: Compute F ratio.**
- F = MSB / MSE = 125.00 / 16.6667 = 7.50.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Between Machines    |       250.00        |   2  |      125.00      |     7.50
Within Machines     |       200.00        |  12  |       16.67      |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |       450.00        |  14  |                  |
```

**Step 6: Conclusion.**
- The calculated F = 7.50 is greater than the critical table value F0.05(2, 12) = 3.89.
- Reject H0 at 5% significance level.
- One of the machines is significantly faster than the others.

**Answer:** **Reject H0. Calculated F = 7.50 > Table F = 3.89. Production speeds differ significantly among machines.**

**Check:** scipy.stats.f_oneway gives F = 7.50.


## Paper 6 Q.9(b) [A18]: Two-Way ANOVA - Varieties of Fertilizers Design

**Given:** Two-way design results for varieties of fertilizers W, X, Y, Z on varieties A, B, C (same data matrix as Paper 1 Q.10(a) / Paper 6 Q.10(a)).

**Answer:** **Same as Paper 1 Q.10(a) [A3] answer: Accept H0 for varieties (Calculated F = 4.00 < Table F = 4.26/5.14). Variety differences are not significant. Plot differences are significant (F = 6.00 > 4.76).**


## Paper 6 Q.10(a) [A19]: Two-Way ANOVA - Per Acre Production Data for 3 Varieties of Wheat

**Given:** Per acre production data for 3 varieties of wheat each grown on 4 plots (same data as Paper 1 Q.10(a)).

**Answer:** **Same as Paper 1 Q.10(a) [A3] answer: Accept H0 for varieties (Calculated F = 4.00 < Table F = 4.26/5.14). Variety differences are not significant. Plot differences are significant (F = 6.00 > 4.76).**


## Paper 6 Q.10(b) [A20]: Latin Square Design - Output of Wheat (4x4)

**Given:** Same statistics concerning output of wheat per field obtained under a 4x4 Latin square design as in Paper 1 Q.9(b).

**Answer:** **Same as Paper 1 Q.9(b) [A2] answer: Varieties F = 9.24 > 4.76 (Significant differences among varieties). Rows F = 8.86 > 4.76 (Significant row differences). Columns F = 1.43 < 4.76 (No column differences).**


# Paper 7

## Paper 7 Q.9(a) [A22]: One-Way ANOVA - Production Output of Three Machines

**Given:** Same hourly production figures for three machines A, B, C as in Paper 6 Q.9(a).

**Answer:** **Same as Paper 6 Q.9(a) [A17] answer: Reject H0. Calculated F = 7.50 > Table F = 3.89. Production speeds differ significantly among machines.**


## Paper 7 Q.9(b): Two-Way ANOVA - Production of Three Varieties of Wheat

**Given:** Same per acre production data for three varieties of wheat grown on four plots as in Paper 1 Q.10(a).

**Answer:** **Same as Paper 1 Q.10(a) [A3] answer: Accept H0 for varieties (Calculated F = 4.00 < Table F = 4.26/5.14). Variety differences are not significant. Plot differences are significant (F = 6.00 > 4.76).**


## Paper 7 Q.10(a): Two-Way ANOVA - Varieties of Fertilizers Design

**Given:** Same two-way design results for varieties of fertilizers as in Paper 1 Q.10(a).

**Answer:** **Same as Paper 1 Q.10(a) [A3] answer: Accept H0 for varieties (Calculated F = 4.00 < Table F = 4.26/5.14). Variety differences are not significant. Plot differences are significant (F = 6.00 > 4.76).**


## Paper 7 Q.10(b) [A21]: Latin Square Design - Yields of Paddy Cultivation Methods (4x4)

**Given:** Yields in kgs of Paddy under a 4x4 Latin square design where A, B, C, D denote different methods of cultivation:
```
  D-122  A-121  C-123  B-122
  B-124  C-123  A-122  D-125
  A-120  B-119  D-120  C-121
  C-122  D-123  B-121  A-122
```
- Significance level: 5%
- Critical table value: F0.05(3, 6) = 4.76
- Coding method: Subtract 120 from all yield observations (u = x - 120) to ease calculations.

**Formula / Method:**
- Rows (n=4), Columns (n=4), Treatments (n=4). Total N = 16.
- Code u_ij = x_ij - 120. Shifting origin does not alter ANOVA sum of squares or F ratios.
- CF = Tu^2 / N.
- SST = sum sum u^2 - CF.
- SSR = sum(Ri^2) / n - CF, SSC = sum(Cj^2) / n - CF, SSTr = sum(Trk^2) / n - CF.
- SSE = SST - SSR - SSC - SSTr.
- dfR = dfC = dfTr = 3, dfE = (4-1)(4-2) = 6.

**Solution:**

**Step 1: Code the data by subtracting 120 from each observation.**

Coded Data Grid (u = x - 120):
```
           Col 1   Col 2   Col 3   Col 4   | Row Total (Ri)
-------------------------------------------+---------------
Row 1    |  D-2     A-1     C-3     B-2    |       8
Row 2    |  B-4     C-3     A-2     D-5    |      14
Row 3    |  A-0     B--1    D-0     C-1    |       0
Row 4    |  C-2     D-3     B-1     A-2    |       8
-------------------------------------------+---------------
Col Total|   8       6       6      10     | Grand Tu = 30
```

Coded Treatment Totals:
- Method A: 1 + 2 + 0 + 2 = 5
- Method B: 2 + 4 + (-1) + 1 = 6
- Method C: 3 + 3 + 1 + 2 = 9
- Method D: 2 + 5 + 0 + 3 = 10
- Check total: 5 + 6 + 9 + 10 = 30 = Tu.

Sum of squares of all 16 coded items sum sum u^2:
- Row 1: 2^2 + 1^2 + 3^2 + 2^2 = 4 + 1 + 9 + 4 = 18
- Row 2: 4^2 + 3^2 + 2^2 + 5^2 = 16 + 9 + 4 + 25 = 54
- Row 3: 0^2 + (-1)^2 + 0^2 + 1^2 = 0 + 1 + 0 + 1 = 2
- Row 4: 2^2 + 3^2 + 1^2 + 2^2 = 4 + 9 + 1 + 4 = 18
- Total sum sum u^2 = 18 + 54 + 2 + 18 = 92.

**Step 2: Calculate Correction Factor and Sums of Squares.**
- CF = Tu^2 / N = 30^2 / 16 = 900 / 16 = 56.25.
- SST = 92 - 56.25 = 35.75.
- SSR (Rows) = (8^2 + 14^2 + 0^2 + 8^2) / 4 - CF = (64 + 196 + 0 + 64) / 4 - 56.25 = 324 / 4 - 56.25 = 81.00 - 56.25 = 24.75.
- SSC (Columns) = (8^2 + 6^2 + 6^2 + 10^2) / 4 - CF = (64 + 36 + 36 + 100) / 4 - 56.25 = 236 / 4 - 56.25 = 59.00 - 56.25 = 2.75.
- SSTr (Methods) = (5^2 + 6^2 + 9^2 + 10^2) / 4 - CF = (25 + 36 + 81 + 100) / 4 - 56.25 = 242 / 4 - 56.25 = 60.50 - 56.25 = 4.25.
- SSE = SST - SSR - SSC - SSTr = 35.75 - 24.75 - 2.75 - 4.25 = 4.00.

**Step 3: Degrees of Freedom and Mean Squares.**
- dfR = 3 => MSR = 24.75 / 3 = 8.25.
- dfC = 3 => MSC = 2.75 / 3 = 0.92.
- dfTr = 3 => MSTr = 4.25 / 3 = 1.42.
- dfE = 6 => MSE = 4.00 / 6 = 0.67.

**Step 4: Compute F Ratios.**
- F_rows = MSR / MSE = 8.25 / 0.6667 = 12.38.
- F_cols = MSC / MSE = 0.9167 / 0.6667 = 1.38.
- F_methods = MSTr / MSE = 1.4167 / 0.6667 = 2.13.

**Step 5: ANOVA Table.**

```
Source of Variation | Sum of Squares (SS) | d.f. | Mean Square (MS) | Calculated F
--------------------+---------------------+------+------------------+--------------
Rows (SSR)          |        24.75        |   3  |       8.25       |    12.38
Columns (SSC)       |         2.75        |   3  |       0.92       |     1.38
Methods (SSTr)      |         4.25        |   3  |       1.42       |     2.13
Error (SSE)         |         4.00        |   6  |       0.67       |
--------------------+---------------------+------+------------------+--------------
Total (SST)         |        35.75        |  15  |                  |
```

**Step 6: Conclusions.**
- Critical table value is F0.05(3, 6) = 4.76.
- Cultivation Methods (Treatments): Calculated FTr = 2.13 < 4.76. Accept H0. Different cultivation methods do not give significantly different results.
- Rows: Calculated FR = 12.38 > 4.76. Reject H0R. Significant row variation exists.
- Columns: Calculated FC = 1.38 < 4.76. Accept H0C. No significant column variation.

**Answer:** **Accept H0 for methods. Calculated F = 2.13 < Table F = 4.76. Cultivation methods do not give significantly different results.**

**Check:** 24.75 + 2.75 + 4.25 + 4.00 = 35.75 = SST.
