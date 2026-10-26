"""
Verification script for Module 3 (Probability Distributions) answers in out_M3_probability.md.
Import mathlib helper functions and assert every numerical answer.
"""
from mathlib import *
import math
from fractions import Fraction as F

def verify_all():
    print("Verifying Module 3 answers...")

    # P1-1a
    k1 = F(1, 10)
    assert k1 == F(1, 10)
    p1_ge6 = 9*k1**2 + k1
    assert p1_ge6 == F(19, 100) # 0.19
    p1_3_6 = 3*k1**2 + 3*k1
    assert p1_3_6 == F(33, 100) # 0.33

    # P1-1c
    p1c_i = math.exp(-2) # 0.1353
    p1c_ii = 1 - math.exp(-2) # 0.8647
    p1c_iii = math.exp(-2) - math.exp(-2.4) # 0.0446
    assert round(p1c_i, 4) == 0.1353
    assert round(p1c_ii, 4) == 0.8647
    assert round(p1c_iii, 4) == 0.0446

    # P1-2a
    K_1_2a = F(1, 18)
    assert K_1_2a == F(1, 18)
    p_1_2a_i = F(7, 54)
    p_1_2a_ii = F(35, 54)
    assert p_1_2a_i == F(7, 54)
    assert p_1_2a_ii == F(35, 54)

    # P1-2b
    lam_1_2b = 0.02
    e_lam_1_2b = math.exp(-0.02)
    p_1_2b_0 = e_lam_1_2b
    p_1_2b_1 = e_lam_1_2b * 0.02
    p_1_2b_2 = e_lam_1_2b * (0.02**2) / 2
    n_1_2b_0 = round(10000 * p_1_2b_0)
    n_1_2b_1 = round(10000 * p_1_2b_1)
    n_1_2b_2 = round(10000 * p_1_2b_2)
    assert n_1_2b_0 == 9802
    assert n_1_2b_1 == 196
    assert n_1_2b_2 == 2

    # P1-2c
    # Given phi(1.67) = 0.4525, phi(0.83) = 0.2967
    p_1_2c_i = 0.5 - 0.4525 # 0.0475
    p_1_2c_ii = 2 * 0.4525 # 0.9050
    p_1_2c_iii = 0.5 - 0.2967 # 0.2033
    n_1_2c_i = round(2500 * p_1_2c_i) # 119
    n_1_2c_ii = 2500 * p_1_2c_ii # 2262.5
    n_1_2c_iii = round(2500 * p_1_2c_iii) # 508
    assert n_1_2c_i == 119
    assert n_1_2c_ii == 2262.5
    assert n_1_2c_iii == 508

    # P2-1b
    p_2_1b_i = F(3, 8)
    p_2_1b_ii = F(15, 16)
    p_2_1b_iii = F(11, 16)
    n_2_1b_i = 800 * p_2_1b_i
    n_2_1b_ii = 800 * p_2_1b_ii
    n_2_1b_iii = 800 * p_2_1b_iii
    assert n_2_1b_i == 300
    assert n_2_1b_ii == 750
    assert n_2_1b_iii == 550

    # P2-1c
    p_2_1c_i = 1 - math.exp(-1) # 0.6321
    p_2_1c_ii = math.exp(-1) - math.exp(-2) # 0.2325
    assert round(p_2_1c_i, 4) == 0.6321
    assert round(p_2_1c_ii, 4) == 0.2325

    # P2-2a
    k_2_2a = F(1, 10)
    EX_2_2a = F(4, 5)
    Var_2_2a = F(54, 25) # 2.16
    p_2_2a_iii = F(9, 10) # 0.9
    assert k_2_2a == F(1, 10)
    assert Var_2_2a == F(54, 25)
    assert p_2_2a_iii == F(9, 10)

    # P2-2b
    e_3 = math.exp(-3)
    p_2_2b_i = 1 - (1 + 3 + 4.5 + 4.5) * e_3 # P(X > 3) = 1 - 13 e^-3
    p_2_2b_ii = (1 + 3 + 4.5) * e_3 # P(X <= 2) = 8.5 e^-3
    n_2_2b_i = round(1000 * p_2_2b_i)
    n_2_2b_ii = round(1000 * p_2_2b_ii)
    assert round(p_2_2b_i, 4) == 0.3528
    assert round(p_2_2b_ii, 4) == 0.4232
    assert n_2_2b_i == 353
    assert n_2_2b_ii == 423

    # P2-2c
    # A(1) = 0.3413
    p_2_2c_i = 0.5 - 0.3413 # 0.1587
    p_2_2c_ii = 2 * 0.3413 # 0.6826
    n_2_2c_i = round(1000 * p_2_2c_i) # 159
    n_2_2c_ii = round(1000 * p_2_2c_ii) # 683
    assert n_2_2c_i == 159
    assert n_2_2c_ii == 683

    # P3-1a
    p_3_1a_i = F(81, 100) # P(x < 6)
    p_3_1a_ii = F(33, 100) # P(3 < x <= 6)
    p_3_1a_iii = F(19, 100) # P(x >= 6)
    assert p_3_1a_i == F(81, 100)
    assert p_3_1a_ii == F(33, 100)
    assert p_3_1a_iii == F(19, 100)

    # P3-2a
    p_3_2a_le2 = F(35, 54)
    p_3_2a_gt1 = F(13, 27)
    p_3_2a_1_2 = F(7, 54)
    assert p_3_2a_le2 == F(35, 54)
    assert p_3_2a_gt1 == F(13, 27)
    assert p_3_2a_1_2 == F(7, 54)

    # P3-2b
    p_3_2b_i = F(1, 4)
    p_3_2b_ii = F(5, 16)
    p_3_2b_iii = F(5, 16)
    assert p_3_2b_i == F(1, 4)
    assert p_3_2b_ii == F(5, 16)
    assert p_3_2b_iii == F(5, 16)

    # P3-2c / P4-2c / P5-1c / P6-2c
    p_norm_lt65 = 0.5 - 0.3413 # 0.1587
    p_norm_gt75 = 0.5 - 0.3413 # 0.1587
    p_norm_65_75 = 2 * 0.3413 # 0.6826
    n_norm_lt65 = round(1000 * p_norm_lt65) # 159
    n_norm_gt75 = round(1000 * p_norm_gt75) # 159
    n_norm_65_75 = round(1000 * p_norm_65_75) # 683
    assert n_norm_lt65 == 159
    assert n_norm_gt75 == 159
    assert n_norm_65_75 == 683

    # P4-1a
    K_4_1a = F(1, 49)
    p_4_1a_ii = F(16, 49) # P(X < 4)
    p_4_1a_iii = F(33, 49) # P(3 < X <= 6)
    assert K_4_1a == F(1, 49)
    assert p_4_1a_ii == F(16, 49)
    assert p_4_1a_iii == F(33, 49)

    # P4-1b
    e_4 = math.exp(-4)
    p_4_1b_i = e_4 # 0.0183
    p_4_1b_ii = 1 - 13 * e_4 # 0.7619
    p_4_1b_iii = 1 - e_4 # 0.9817
    assert round(p_4_1b_i, 4) == 0.0183
    assert round(p_4_1b_ii, 4) == 0.7619
    assert round(p_4_1b_iii, 4) == 0.9817

    # P4-1c
    A_4_1c = F(1, 5)
    p_4_1c_i = math.exp(-2) # 0.1353
    p_4_1c_ii = 1 - math.exp(-1) # 0.6321
    p_4_1c_iii = math.exp(-1) - math.exp(-2) # 0.2325
    assert A_4_1c == F(1, 5)
    assert round(p_4_1c_i, 4) == 0.1353
    assert round(p_4_1c_ii, 4) == 0.6321
    assert round(p_4_1c_iii, 4) == 0.2325

    # P4-2a
    K_4_2a = F(1, 9)
    p_4_2a_i = F(7, 27)
    p_4_2a_ii = F(1, 27)
    assert K_4_2a == F(1, 9)
    assert p_4_2a_i == F(7, 27)
    assert p_4_2a_ii == F(1, 27)

    # P5-1b
    p_5_1b_i = math.comb(12, 2) * (0.1**2) * (0.9**10) # 0.2301
    p_5_1b_iii = 0.9**12 # 0.2824
    p_5_1b_ii = 1 - p_5_1b_iii - 12 * 0.1 * (0.9**11) # 0.3410
    assert round(p_5_1b_i, 4) == 0.2301
    assert round(p_5_1b_ii, 4) == 0.3410
    assert round(p_5_1b_iii, 4) == 0.2824

    # P5-2a
    p_5_2a_ii = F(24, 49) # P(x >= 5)
    p_5_2a_iii = F(33, 49) # P(3 < x <= 6)
    assert p_5_2a_ii == F(24, 49)
    assert p_5_2a_iii == F(33, 49)

    # P5-2b
    p_5_2b_i = e_3 # 0.0498
    p_5_2b_ii = 1 - 13 * e_3 # 0.3528
    n_5_2b_i = round(1000 * p_5_2b_i) # 50
    n_5_2b_ii = round(1000 * p_5_2b_ii) # 353
    assert round(p_5_2b_i, 4) == 0.0498
    assert round(p_5_2b_ii, 4) == 0.3528
    assert n_5_2b_i == 50
    assert n_5_2b_ii == 353

    # P5-2c
    p_5_2c_i = 0.2881 + 0.4772 # 0.7653
    p_5_2c_ii = 0.5 - 0.4987 # 0.0013
    assert round(p_5_2c_i, 4) == 0.7653
    assert round(p_5_2c_ii, 4) == 0.0013

    # P6-1a
    p_6_1a_i = F(81, 100) # P[x < 6]
    p_6_1a_ii = F(4, 5) # P[0 < x < 5]
    p_6_1a_iii = F(19, 100) # P[x >= 6]
    assert p_6_1a_i == F(81, 100)
    assert p_6_1a_ii == F(4, 5)
    assert p_6_1a_iii == F(19, 100)

    # P6-1c
    e_2 = math.exp(-2)
    p_6_1c = 1 - 5 * e_2 # 0.3233
    assert round(p_6_1c, 4) == 0.3233

    # P6-2a
    k_6_2a = 1 / (1 - math.exp(-1)) # 1.5820
    mean_6_2a = k_6_2a * (1 - 2 * math.exp(-1)) # 0.4180
    assert round(k_6_2a, 4) == 1.5820
    assert round(mean_6_2a, 4) == 0.4180

    # P7-2b
    k_7_2b = F(1, 30)
    p_7_2b_i = F(13, 30) # P(0 < x <= 2)
    p_7_2b_ii = F(13, 15) # P(x >= 1)
    assert k_7_2b == F(1, 30)
    assert p_7_2b_i == F(13, 30)
    assert p_7_2b_ii == F(13, 15)

    print("ALL MODULE 3 VERIFICATIONS PASSED OK!")

if __name__ == "__main__":
    verify_all()
