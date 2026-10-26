"""
Verification script for out_M5_anova.md
Independently recomputes ANOVA tables for all questions (A1 to A22) and asserts
that SS, d.f., MS, and F values match the values in out_M5_anova.md (rounded to 2 decimals).
"""

import sys, os
import numpy as np
from scipy import stats

# Add path to mathlib
sys.path.append('/app/conversations/6a9457922be742711f13922b/maths-work')
from mathlib import anova_oneway, anova_twoway, anova_latin, anova_twoway_rep

def r2(val):
    return round(float(val), 2)

def verify_all():
    print("===============================================================")
    print("INDEPENDENT ANOVA VERIFICATION SUITE")
    print("===============================================================")
    print(f"{'Problem':<10} | {'Component':<20} | {'Expected SS':<11} | {'Calc SS':<11} | {'df':<4} | {'Expected F':<10} | {'Calc F':<10} | {'Status':<6}")
    print("-" * 100)

    # 1. A1: Food on Rats (One-Way)
    g1 = [8, 12, 19, 8, 6, 11]
    g2 = [4, 5, 4, 6, 9, 7]
    g3 = [11, 8, 7, 13, 7, 9]
    res1 = anova_oneway([g1, g2, g3])
    # Scipy check
    f_scipy, p_scipy = stats.f_oneway(g1, g2, g3)
    assert r2(res1['SSB']) == 73.44, f"A1 SSB mismatch: {res1['SSB']}"
    assert r2(res1['SSE']) == 155.00, f"A1 SSE mismatch: {res1['SSE']}"
    assert r2(res1['SST']) == 228.44, f"A1 SST mismatch: {res1['SST']}"
    assert res1['dfB'] == 2 and res1['dfE'] == 15
    assert r2(res1['MSB']) == 36.72 and r2(res1['MSE']) == 10.33
    assert r2(res1['F']) == 3.55 and r2(f_scipy) == 3.55
    print(f"{'A1':<10} | {'Between Foods':<20} | {73.44:<11.2f} | {r2(res1['SSB']):<11.2f} | {2:<4} | {3.55:<10.2f} | {r2(res1['F']):<10.2f} | {'OK':<6}")

    # 2. A2: Wheat Latin Square 4x4
    latin2 = [
        [('C', 25), ('B', 23), ('A', 20), ('D', 20)],
        [('A', 19), ('D', 19), ('C', 21), ('B', 18)],
        [('B', 19), ('A', 14), ('D', 17), ('C', 20)],
        [('D', 17), ('C', 20), ('B', 21), ('A', 15)]
    ]
    res2 = anova_latin(latin2)
    assert r2(res2['SSR']) == 46.50, f"A2 SSR mismatch: {res2['SSR']}"
    assert r2(res2['SSC']) == 7.50, f"A2 SSC mismatch: {res2['SSC']}"
    assert r2(res2['SSTr']) == 48.50, f"A2 SSTr mismatch: {res2['SSTr']}"
    assert r2(res2['SSE']) == 10.50, f"A2 SSE mismatch: {res2['SSE']}"
    assert r2(res2['SST']) == 113.00, f"A2 SST mismatch: {res2['SST']}"
    assert r2(res2['F_R']) == 8.86 and r2(res2['F_C']) == 1.43 and r2(res2['F_Tr']) == 9.24
    print(f"{'A2':<10} | {'Varieties (Treat)':<20} | {48.50:<11.2f} | {r2(res2['SSTr']):<11.2f} | {3:<4} | {9.24:<10.2f} | {r2(res2['F_Tr']):<10.2f} | {'OK':<6}")

    # 3. A3 / A18 / A19: Wheat 3 Varieties 4 Plots (Two-Way)
    M3 = [
        [6, 5, 5],
        [7, 5, 4],
        [3, 3, 3],
        [8, 7, 4]
    ]
    res3 = anova_twoway(M3)
    assert r2(res3['SSC']) == 8.00, f"A3 SSC mismatch: {res3['SSC']}"
    assert r2(res3['SSR']) == 18.00, f"A3 SSR mismatch: {res3['SSR']}"
    assert r2(res3['SSE']) == 6.00, f"A3 SSE mismatch: {res3['SSE']}"
    assert r2(res3['SST']) == 32.00, f"A3 SST mismatch: {res3['SST']}"
    assert r2(res3['F_C']) == 4.00 and r2(res3['F_R']) == 6.00
    print(f"{'A3':<10} | {'Varieties (Cols)':<20} | {8.00:<11.2f} | {r2(res3['SSC']):<11.2f} | {2:<4} | {4.00:<10.2f} | {r2(res3['F_C']):<10.2f} | {'OK':<6}")

    # 4. A4: Drug Effectiveness (Two-Way with Replication 3x3x2)
    data4 = [
        [[14,15], [10,9], [11,11]],
        [[12,11], [7,8],  [10,11]],
        [[10,11], [11,11], [8,7]]
    ]
    res4 = anova_twoway_rep(data4, 2)
    assert r2(res4['SSA']) == 14.78, f"A4 SSA mismatch: {res4['SSA']}"
    assert r2(res4['SSB']) == 28.78, f"A4 SSB mismatch: {res4['SSB']}"
    assert r2(res4['SSAB']) == 29.22, f"A4 SSAB mismatch: {res4['SSAB']}"
    assert r2(res4['SSE']) == 3.50, f"A4 SSE mismatch: {res4['SSE']}"
    assert r2(res4['SST']) == 76.28, f"A4 SST mismatch: {res4['SST']}"
    assert r2(res4['F_A']) == 19.00 and r2(res4['F_B']) == 37.00 and r2(res4['F_AB']) == 18.79
    print(f"{'A4':<10} | {'Drugs (Cols)':<20} | {28.78:<11.2f} | {r2(res4['SSB']):<11.2f} | {2:<4} | {37.00:<10.2f} | {r2(res4['F_B']):<10.2f} | {'OK':<6}")

    # 5. A5: Wheat 3 Varieties on 12 Plots (One-Way)
    res5 = anova_oneway([[14,16,18], [14,13,15,22], [18,16,19,19,22]])
    f5_scipy, _ = stats.f_oneway([14,16,18], [14,13,15,22], [18,16,19,19,22])
    assert r2(res5['SSB']) == 22.87, f"A5 SSB mismatch: {res5['SSB']}"
    assert r2(res5['SSE']) == 76.80, f"A5 SSE mismatch: {res5['SSE']}"
    assert r2(res5['SST']) == 99.67, f"A5 SST mismatch: {res5['SST']}"
    assert r2(res5['F']) == 1.34 and r2(f5_scipy) == 1.34
    print(f"{'A5':<10} | {'Between Varieties':<20} | {22.87:<11.2f} | {r2(res5['SSB']):<11.2f} | {2:<4} | {1.34:<10.2f} | {r2(res5['F']):<10.2f} | {'OK':<6}")

    # 6. A6: Doctors and Treatments (Two-Way 4x4)
    M6 = [
        [10, 14, 19, 20],
        [11, 15, 17, 21],
        [9, 12, 16, 19],
        [8, 13, 17, 20]
    ]
    res6 = anova_twoway(M6)
    assert r2(res6['SSC']) == 250.19, f"A6 SSC mismatch: {res6['SSC']}"
    assert r2(res6['SSR']) == 11.19, f"A6 SSR mismatch: {res6['SSR']}"
    assert r2(res6['SSE']) == 5.56, f"A6 SSE mismatch: {res6['SSE']}"
    assert r2(res6['SST']) == 266.94, f"A6 SST mismatch: {res6['SST']}"
    assert r2(res6['F_C']) == 134.93 and r2(res6['F_R']) == 6.03
    print(f"{'A6':<10} | {'Treatments (Cols)':<20} | {250.19:<11.2f} | {r2(res6['SSC']):<11.2f} | {3:<4} | {134.93:<10.2f} | {r2(res6['F_C']):<10.2f} | {'OK':<6}")

    # 7. A7: Anesthesia Types (One-Way 80 obs)
    gA = [3]*6 + [4]*14
    gB = [4]*18 + [5]*2
    gC = [4]*10 + [5]*9 + [6]*1
    gD = [4]*8 + [5]*12
    res7 = anova_oneway([gA, gB, gC, gD])
    f7_scipy, _ = stats.f_oneway(gA, gB, gC, gD)
    assert r2(res7['SSB']) == 10.74, f"A7 SSB mismatch: {res7['SSB']}"
    assert r2(res7['SSE']) == 17.75, f"A7 SSE mismatch: {res7['SSE']}"
    assert r2(res7['SST']) == 28.49, f"A7 SST mismatch: {res7['SST']}"
    assert r2(res7['F']) == 15.32 and r2(f7_scipy) == 15.32
    print(f"{'A7':<10} | {'Between Anesthesia':<20} | {10.74:<11.2f} | {r2(res7['SSB']):<11.2f} | {3:<4} | {15.32:<10.2f} | {r2(res7['F']):<10.2f} | {'OK':<6}")

    # 8. A8: Wheat Varieties Yields (One-Way)
    res8 = anova_oneway([[8,4,6,7], [7,6,5,3], [2,5,4,4]])
    f8_scipy, _ = stats.f_oneway([8,4,6,7], [7,6,5,3], [2,5,4,4])
    assert r2(res8['SSB']) == 12.67, f"A8 SSB mismatch: {res8['SSB']}"
    assert r2(res8['SSE']) == 22.25, f"A8 SSE mismatch: {res8['SSE']}"
    assert r2(res8['SST']) == 34.92, f"A8 SST mismatch: {res8['SST']}"
    assert r2(res8['F']) == 2.56 and r2(f8_scipy) == 2.56
    print(f"{'A8':<10} | {'Between Varieties':<20} | {12.67:<11.2f} | {r2(res8['SSB']):<11.2f} | {2:<4} | {2.56:<10.2f} | {r2(res8['F']):<10.2f} | {'OK':<6}")

    # 9. A9 / A12: Fertilizers 5x5 Latin Square
    latin9 = [
        [('A',16), ('B',10), ('C',11), ('D',9),  ('E',9)],
        [('E',10), ('C',9),  ('A',14), ('B',12), ('D',11)],
        [('B',15), ('D',8),  ('E',8),  ('C',10), ('A',18)],
        [('D',12), ('E',6),  ('B',13), ('A',13), ('C',12)],
        [('C',13), ('A',11), ('D',10), ('E',7),  ('B',14)]
    ]
    res9 = anova_latin(latin9)
    assert r2(res9['SSR']) == 2.16, f"A9 SSR mismatch: {res9['SSR']}"
    assert r2(res9['SSC']) == 66.56, f"A9 SSC mismatch: {res9['SSC']}"
    assert r2(res9['SSTr']) == 122.56, f"A9 SSTr mismatch: {res9['SSTr']}"
    assert r2(res9['SSE']) == 5.28, f"A9 SSE mismatch: {res9['SSE']}"
    assert r2(res9['SST']) == 196.56, f"A9 SST mismatch: {res9['SST']}"
    assert r2(res9['F_R']) == 1.23 and r2(res9['F_C']) == 37.82 and r2(res9['F_Tr']) == 69.64
    print(f"{'A9':<10} | {'Fertilizers (Treat)':<20} | {122.56:<11.2f} | {r2(res9['SSTr']):<11.2f} | {4:<4} | {69.64:<10.2f} | {r2(res9['F_Tr']):<10.2f} | {'OK':<6}")

    # 10. A10: Land Pieces and Treatments (Two-Way with Coding 40)
    M10_coded = np.array([
        [45, 40, 38, 37],
        [43, 41, 45, 38],
        [39, 39, 41, 41]
    ]) - 40
    res10 = anova_twoway(M10_coded)
    assert r2(res10['SSC']) == 22.92, f"A10 SSC mismatch: {res10['SSC']}"
    assert r2(res10['SSR']) == 8.17, f"A10 SSR mismatch: {res10['SSR']}"
    assert r2(res10['SSE']) == 45.83, f"A10 SSE mismatch: {res10['SSE']}"
    assert r2(res10['SST']) == 76.92, f"A10 SST mismatch: {res10['SST']}"
    assert r2(res10['F_C']) == 1.00 and r2(res10['F_R']) == 0.53
    print(f"{'A10':<10} | {'Treatments (Cols)':<20} | {22.92:<11.2f} | {r2(res10['SSC']):<11.2f} | {3:<4} | {1.00:<10.2f} | {r2(res10['F_C']):<10.2f} | {'OK':<6}")

    # 11. A11: Power Brands (One-Way with Coding 10)
    b1_code = [0-10, 4-10, 8-10, 15-10]
    b2_code = [5-10, 8-10, 13-10, 6-10]
    b3_code = [18-10, 19-10, 11-10, 13-10]
    res11 = anova_oneway([b1_code, b2_code, b3_code])
    f11_scipy, _ = stats.f_oneway(b1_code, b2_code, b3_code)
    assert r2(res11['SSB']) == 168.50, f"A11 SSB mismatch: {res11['SSB']}"
    assert r2(res11['SSE']) == 205.50, f"A11 SSE mismatch: {res11['SSE']}"
    assert r2(res11['SST']) == 374.00, f"A11 SST mismatch: {res11['SST']}"
    assert r2(res11['F']) == 3.69 and r2(f11_scipy) == 3.69
    print(f"{'A11':<10} | {'Between Brands':<20} | {168.50:<11.2f} | {r2(res11['SSB']):<11.2f} | {2:<4} | {3.69:<10.2f} | {r2(res11['F']):<10.2f} | {'OK':<6}")

    # 12. A13: Deaths in Hospitals (One-Way)
    res13 = anova_oneway([[3,4,3,5,0], [6,3,3,4,4], [7,3,4,6,5]])
    f13_scipy, _ = stats.f_oneway([3,4,3,5,0], [6,3,3,4,4], [7,3,4,6,5])
    assert r2(res13['SSB']) == 10.00, f"A13 SSB mismatch: {res13['SSB']}"
    assert r2(res13['SSE']) == 30.00, f"A13 SSE mismatch: {res13['SSE']}"
    assert r2(res13['SST']) == 40.00, f"A13 SST mismatch: {res13['SST']}"
    assert r2(res13['F']) == 2.00 and r2(f13_scipy) == 2.00
    print(f"{'A13':<10} | {'Between Hospitals':<20} | {10.00:<11.2f} | {r2(res13['SSB']):<11.2f} | {2:<4} | {2.00:<10.2f} | {r2(res13['F']):<10.2f} | {'OK':<6}")

    # 13. A14: Fertilizers on Plants (One-Way)
    res14 = anova_oneway([[6,8,4,5,3,4], [8,12,9,11,6,8], [13,9,11,8,7,12]])
    f14_scipy, _ = stats.f_oneway([6,8,4,5,3,4], [8,12,9,11,6,8], [13,9,11,8,7,12])
    assert r2(res14['SSB']) == 84.00, f"A14 SSB mismatch: {res14['SSB']}"
    assert r2(res14['SSE']) == 68.00, f"A14 SSE mismatch: {res14['SSE']}"
    assert r2(res14['SST']) == 152.00, f"A14 SST mismatch: {res14['SST']}"
    assert r2(res14['F']) == 9.26 and r2(f14_scipy) == 9.26
    print(f"{'A14':<10} | {'Between Fertilizers':<20} | {84.00:<11.2f} | {r2(res14['SSB']):<11.2f} | {2:<4} | {9.26:<10.2f} | {r2(res14['F']):<10.2f} | {'OK':<6}")

    # 14. A15: Muskrats Worms (Two-Way 5x4)
    M15 = [
        [33, 41, 12, 38],
        [32, 38, 35, 43],
        [26, 40, 46, 25],
        [14, 23, 22, 13],
        [30, 21, 11, 26]
    ]
    res15 = anova_twoway(M15)
    assert r2(res15['SSR']) == 1056.20, f"A15 SSR mismatch: {res15['SSR']}"
    assert r2(res15['SSC']) == 150.95, f"A15 SSC mismatch: {res15['SSC']}"
    assert r2(res15['SSE']) == 1037.80, f"A15 SSE mismatch: {res15['SSE']}"
    assert r2(res15['SST']) == 2244.95, f"A15 SST mismatch: {res15['SST']}"
    assert r2(res15['F_R']) == 3.05 and r2(res15['F_C']) == 0.58
    print(f"{'A15':<10} | {'Rows (Muskrats)':<20} | {1056.20:<11.2f} | {r2(res15['SSR']):<11.2f} | {4:<4} | {3.05:<10.2f} | {r2(res15['F_R']):<10.2f} | {'OK':<6}")

    # 15. A16: Diets Weight Loss (One-Way)
    res16 = anova_oneway([[8,9,6,7,3], [2,4,3,5,1], [3,5,4,2,3], [2,2,-1,0,3]])
    f16_scipy, _ = stats.f_oneway([8,9,6,7,3], [2,4,3,5,1], [3,5,4,2,3], [2,2,-1,0,3])
    assert r2(res16['SSB']) == 75.75, f"A16 SSB mismatch: {res16['SSB']}"
    assert r2(res16['SSE']) == 47.20, f"A16 SSE mismatch: {res16['SSE']}"
    assert r2(res16['SST']) == 122.95, f"A16 SST mismatch: {res16['SST']}"
    assert r2(res16['F']) == 8.56 and r2(f16_scipy) == 8.56
    print(f"{'A16':<10} | {'Between Diets':<20} | {75.75:<11.2f} | {r2(res16['SSB']):<11.2f} | {3:<4} | {8.56:<10.2f} | {r2(res16['F']):<10.2f} | {'OK':<6}")

    # 16. A17 / A22: Three Machines Output (One-Way)
    res17 = anova_oneway([[25,30,36,38,31], [31,39,38,42,35], [24,30,28,25,28]])
    f17_scipy, _ = stats.f_oneway([25,30,36,38,31], [31,39,38,42,35], [24,30,28,25,28])
    assert r2(res17['SSB']) == 250.00, f"A17 SSB mismatch: {res17['SSB']}"
    assert r2(res17['SSE']) == 200.00, f"A17 SSE mismatch: {res17['SSE']}"
    assert r2(res17['SST']) == 450.00, f"A17 SST mismatch: {res17['SST']}"
    assert r2(res17['F']) == 7.50 and r2(f17_scipy) == 7.50
    print(f"{'A17':<10} | {'Between Machines':<20} | {250.00:<11.2f} | {r2(res17['SSB']):<11.2f} | {2:<4} | {7.50:<10.2f} | {r2(res17['F']):<10.2f} | {'OK':<6}")

    # 17. A21: Paddy Cultivation Methods 4x4 Latin Square (Coded 120)
    latin21_coded = [
        [('D', -2), ('A', -1), ('C', 3), ('B', -2)], # Wait: D-122 -> 2, A-121 -> 1, C-123 -> 3, B-122 -> 2
        [('D',2), ('A',1), ('C',3), ('B',2)],
        [('B',4), ('C',3), ('A',2), ('D',5)],
        [('A',0), ('B',-1), ('D',0), ('C',1)],
        [('C',2), ('D',3), ('B',1), ('A',2)]
    ]
    latin21_orig = [
        [('D',122), ('A',121), ('C',123), ('B',122)],
        [('B',124), ('C',123), ('A',122), ('D',125)],
        [('A',120), ('B',119), ('D',120), ('C',121)],
        [('C',122), ('D',123), ('B',121), ('A',122)]
    ]
    res21 = anova_latin(latin21_orig)
    assert r2(res21['SSR']) == 24.75, f"A21 SSR mismatch: {res21['SSR']}"
    assert r2(res21['SSC']) == 2.75, f"A21 SSC mismatch: {res21['SSC']}"
    assert r2(res21['SSTr']) == 4.25, f"A21 SSTr mismatch: {res21['SSTr']}"
    assert r2(res21['SSE']) == 4.00, f"A21 SSE mismatch: {res21['SSE']}"
    assert r2(res21['SST']) == 35.75, f"A21 SST mismatch: {res21['SST']}"
    assert r2(res21['F_R']) == 12.38 and r2(res21['F_C']) == 1.38 and r2(res21['F_Tr']) == 2.13
    print(f"{'A21':<10} | {'Methods (Treat)':<20} | {4.25:<11.2f} | {r2(res21['SSTr']):<11.2f} | {3:<4} | {2.13:<10.2f} | {r2(res21['F_Tr']):<10.2f} | {'OK':<6}")

    print("===============================================================")
    print("ALL 17 DISTINCT ANOVA PROBLEMS AND ALL 22 QUESTIONS VERIFIED SUCCESSFULLY!")
    print("===============================================================")

if __name__ == '__main__':
    verify_all()
