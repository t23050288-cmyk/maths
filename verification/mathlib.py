"""Shared helpers. Every answer number must come from code. Import with: from mathlib import *"""
import math, itertools
from fractions import Fraction as F
import numpy as np
from scipy import stats

def phi_area(z):
    """A(z) = area under standard normal curve from 0 to z  (VTU 'phi(z)' / 'A(z)')."""
    return stats.norm.cdf(z) - 0.5

def binom_pmf(n, p, r):
    return math.comb(n, r) * p**r * (1-p)**(n-r)

def poisson_pmf(lam, r):
    return math.exp(-lam) * lam**r / math.factorial(r)

def fixed_vector(P):
    """unique fixed probability vector of a regular stochastic matrix P (list of lists of Fractions)."""
    import sympy as sp
    n = len(P)
    M = sp.Matrix(P)
    xs = sp.symbols('x0:%d' % n)
    eqs = list(sp.Matrix([xs]) * M - sp.Matrix([xs]))
    eqs = [e for e in eqs] + [sum(xs) - 1]
    return sp.solve(eqs, xs)

def matpow(P, k):
    import sympy as sp
    return sp.Matrix(P) ** k

def joint_table(rows, cols, tab):
    """returns marginals, E(X),E(Y),E(XY),cov, rho (exact fractions if input are Fractions)."""
    px = [sum(r) for r in tab]
    py = [sum(tab[i][j] for i in range(len(rows))) for j in range(len(cols))]
    EX = sum(x*p for x, p in zip(rows, px)); EY = sum(y*p for y, p in zip(cols, py))
    EXY = sum(rows[i]*cols[j]*tab[i][j] for i in range(len(rows)) for j in range(len(cols)))
    cov = EXY - EX*EY
    VX = sum(x*x*p for x, p in zip(rows, px)) - EX**2
    VY = sum(y*y*p for y, p in zip(cols, py)) - EY**2
    rho = float(cov) / math.sqrt(float(VX)*float(VY)) if VX > 0 and VY > 0 else None
    return dict(px=px, py=py, EX=EX, EY=EY, EXY=EXY, cov=cov, VX=VX, VY=VY, rho=rho)

def z_two_prop(x1, n1, x2, n2):
    p1, p2 = x1/n1, x2/n2
    P = (x1+x2)/(n1+n2)
    Q = 1-P
    se = math.sqrt(P*Q*(1/n1+1/n2))
    return (p1-p2)/se, P, se

def anova_oneway(groups):
    allv = [v for g in groups for v in g]
    N = len(allv); T = sum(allv); CF = T*T/N
    SST = sum(v*v for v in allv) - CF
    SSB = sum(sum(g)**2/len(g) for g in groups) - CF
    SSE = SST - SSB
    k = len(groups)
    MSB = SSB/(k-1); MSE = SSE/(N-k)
    return dict(N=N, T=T, CF=CF, SST=SST, SSB=SSB, SSE=SSE, dfB=k-1, dfE=N-k, MSB=MSB, MSE=MSE, F=MSB/MSE,
                totals=[sum(g) for g in groups], Fcrit05=stats.f.ppf(0.95, k-1, N-k))

def anova_twoway(M):
    """M = list of rows (blocks) x columns (treatments), one observation per cell."""
    M = np.array(M, float); r, c = M.shape
    T = M.sum(); N = r*c; CF = T*T/N
    SST = (M**2).sum() - CF
    SSC = (M.sum(axis=0)**2).sum()/r - CF   # columns (treatments)
    SSR = (M.sum(axis=1)**2).sum()/c - CF   # rows (blocks)
    SSE = SST - SSC - SSR
    dfC, dfR, dfE = c-1, r-1, (r-1)*(c-1)
    return dict(r=r, c=c, T=T, N=N, CF=CF, SST=SST, SSC=SSC, SSR=SSR, SSE=SSE, dfC=dfC, dfR=dfR, dfE=dfE,
                MSC=SSC/dfC, MSR=SSR/dfR, MSE=SSE/dfE, F_C=(SSC/dfC)/(SSE/dfE), F_R=(SSR/dfR)/(SSE/dfE),
                colT=M.sum(axis=0).tolist(), rowT=M.sum(axis=1).tolist(),
                F_C_crit=stats.f.ppf(.95, dfC, dfE), F_R_crit=stats.f.ppf(.95, dfR, dfE))

def anova_latin(L):
    """L = list of rows of (treatment_label, value)."""
    n = len(L)
    vals = np.array([[v for (t, v) in row] for row in L], float)
    T = vals.sum(); N = n*n; CF = T*T/N
    SST = (vals**2).sum() - CF
    SSR = (vals.sum(axis=1)**2).sum()/n - CF
    SSC = (vals.sum(axis=0)**2).sum()/n - CF
    tt = {}
    for row in L:
        for (t, v) in row: tt[t] = tt.get(t, 0) + v
    SSTr = sum(x*x for x in tt.values())/n - CF
    SSE = SST - SSR - SSC - SSTr
    df = n-1; dfE = (n-1)*(n-2)
    return dict(n=n, T=T, CF=CF, SST=SST, SSR=SSR, SSC=SSC, SSTr=SSTr, SSE=SSE, df=df, dfE=dfE,
                MSR=SSR/df, MSC=SSC/df, MSTr=SSTr/df, MSE=SSE/dfE,
                F_R=(SSR/df)/(SSE/dfE), F_C=(SSC/df)/(SSE/dfE), F_Tr=(SSTr/df)/(SSE/dfE),
                rowT=vals.sum(axis=1).tolist(), colT=vals.sum(axis=0).tolist(), trT=tt,
                Fcrit=stats.f.ppf(.95, df, dfE))

def anova_twoway_rep(data, reps):
    """data[i][j] = list of replicates for row-group i, column-treatment j."""
    a = len(data); b = len(data[0]); r = reps
    allv = [v for i in range(a) for j in range(b) for v in data[i][j]]
    N = len(allv); T = sum(allv); CF = T*T/N
    SST = sum(v*v for v in allv) - CF
    SSA = sum(sum(v for j in range(b) for v in data[i][j])**2 for i in range(a))/(b*r) - CF
    SSB = sum(sum(v for i in range(a) for v in data[i][j])**2 for j in range(b))/(a*r) - CF
    SScell = sum(sum(data[i][j])**2 for i in range(a) for j in range(b))/r - CF
    SSAB = SScell - SSA - SSB
    SSE = SST - SScell
    dfA, dfB, dfAB, dfE = a-1, b-1, (a-1)*(b-1), a*b*(r-1)
    MSE = SSE/dfE
    return dict(N=N, T=T, CF=CF, SST=SST, SSA=SSA, SSB=SSB, SSAB=SSAB, SSE=SSE, dfA=dfA, dfB=dfB, dfAB=dfAB, dfE=dfE,
                F_A=(SSA/dfA)/MSE, F_B=(SSB/dfB)/MSE, F_AB=(SSAB/dfAB)/MSE, MSE=MSE,
                MSA=SSA/dfA, MSB=SSB/dfB, MSAB=SSAB/dfAB,
                Fcrit_A=stats.f.ppf(.95, dfA, dfE), Fcrit_B=stats.f.ppf(.95, dfB, dfE), Fcrit_AB=stats.f.ppf(.95, dfAB, dfE))

def r4(x): return round(float(x), 4)
