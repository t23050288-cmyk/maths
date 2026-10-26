# Mathematics for Computer Science (VTU 3rd sem)

Exam-ready answers for VTU 3rd semester Maths (the college syllabus: Module 1
Modular Arithmetic, Module 2 Statistics / Curve Fitting, Module 3 Probability
Distributions, Module 4 Joint Probability + Markov Chains, Module 5 Statistical
Inference including ANOVA).

Source material: the college class notes (Modular Arithmetic + Statistics +
Probability notes PDFs), the Maths Important Questions sheet, the Assignment 1
sheet, 7 BMATS101 (CSE stream) papers (Jan/Feb 2023 to June/July 2025) and
7 BCS301 papers (Dec 2023/Jan 2024 to Dec 2025/Jan 2026). Answers are written
in the same steps the notes use, and every number was recomputed and checked
by computer before writing. Where the notes themselves contain a slip, it is
marked in the answer with a WARNING so you do not copy it into your book.

## Contents

### Important Questions (the college IMP sheet)

| File | Covers |
|---|---|
| [Important-Questions/Imp-Questions-Answers.md](Important-Questions/Imp-Questions-Answers.md) | All 20 imp questions: Module 1 (last digits, remainders, Fermat, CRT, linear congruences, systems, products), Module 2 (straight line, parabola, power curve fitting with full tables), Module 3 (probability distributions, mean/variance, binomial derivation). Question first, then the answer, in order |

### Assignment 1

| File | Covers |
|---|---|
| [Assignment-1/Assignment-1-Answers.md](Assignment-1/Assignment-1-Answers.md) | All 10 questions: unit digit, last digit, remainder products, linear congruence with example, straight line / parabola / power curve fitting, correlation + regression with full working, mean & variance derivations for Binomial and Poisson |

### PYQ Answers (question and answer per paper, repeats marked)

| File | Covers |
|---|---|
| [PYQ-Answers/Module1-Modular-Arithmetic.md](PYQ-Answers/Module1-Modular-Arithmetic.md) | Q.7/Q.8 modular arithmetic from 7 BMATS101 CSE papers (Jan/Feb 2023, Jun/Jul 2023, Dec 2023/Jan 2024, Jun/Jul 2024 + Supplementary, Dec 2024/Jan 2025, Jun/Jul 2025): last digits, Fermat, Wilson, linear congruences, Diophantine equations, systems, CRT, RSA (STOP and p=3,q=11), polynomial congruences. Ends with a revision map of how questions repeat across papers |
| [PYQ-Answers/Module3-Probability-Distributions.md](PYQ-Answers/Module3-Probability-Distributions.md) | Probability, conditional probability, Bayes, random variables, discrete distributions, Binomial, Poisson, Exponential, Normal with table values (Module 1 of the BCS301 papers) |
| [PYQ-Answers/Module4-Joint-Prob-Markov-Chains.md](PYQ-Answers/Module4-Joint-Prob-Markov-Chains.md) | Joint distributions, marginals, covariance, correlation, independence, and Markov chains: TPM, fixed vectors, ball problems, car trading, study habits (Module 2 of the BCS301 papers) |
| [PYQ-Answers/Module5-ANOVA.md](PYQ-Answers/Module5-ANOVA.md) | One-way, two-way, Latin square and two-way with replication ANOVA, every ANOVA table recomputed (Module 5 of the BCS301 papers) |
| PYQ-Answers/Module5-Inference.md | Being verified, will be added: z tests, t, F, chi-square, CLT, confidence limits (Modules 3 and 4 of the BCS301 papers) |

### Verification

| Script | Checks |
|---|---|
| [verification/verify_M1_imp_assignment.py](verification/verify_M1_imp_assignment.py) | Every number in the Module 1 PYQ file, the imp questions and the assignment (run `python3 verification/verify_M1_imp_assignment.py`) |
| [verification/verify_M3.py](verification/verify_M3.py) | Every number in the probability PYQ file |
| [verification/verify_M4.py](verification/verify_M4.py) | Every number in the joint/Markov PYQ file |
| [verification/verify_anova.py](verification/verify_anova.py) | Every ANOVA table in the ANOVA file |

All four scripts print OK when run. `verification/mathlib.py` holds the shared
helper functions (phi area, ANOVA routines, Markov helpers).

## Syllabus note

The college syllabus (Modular Arithmetic and Statistics modules) and the
BCS301 papers (probability and inference) cover different halves of the
course. The PYQ folder is organised by the college syllabus modules:

- Module 1 PYQs come from the BMATS101 CSE papers (their Module 4 is modular
  arithmetic).
- Modules 3, 4, 5 PYQs come from the BCS301 papers (probability, joint/Markov,
  inference, ANOVA).
- Module 2 (Statistics / curve fitting, correlation, regression) does not
  appear in the uploaded papers. Its questions are covered fully in the imp
  questions and the assignment (straight line, parabola, power curve,
  correlation and regression with full tables).

## Notes errors found (read before copying from the notes)

1. Power curve (x = 2..5): the notes print log 2 = 0.6981, correct is 0.6931,
   so the notes' a = 7.27, b = 1.9406 are slightly off. Correct: a = 7.3799,
   b = 1.9302.
2. Euler's theorem example (23^130 mod 25): the notes use phi(25) = 16. Correct
   is phi(25) = 20, and 23^130 = 24 (mod 25).
3. The notes' CRT worked example with moduli 9 and 10 uses M = 180 and mixes
   one residue. Correct: M = 90 and x = 53 (mod 90).
4. The imp sheet's probability table (0, k, 2k, 2k, 3k, k^2, 7k2+k) prints 7
   entries. The real VTU question has 8 entries and k = 1/10. Solved with 8
   entries.
5. In the statistics notes: the parabola worked example 5 has a sign slip in
   the c term and a mis-added xy column, and one correlation worked example
   prints a wrong constant in the x-on-y line. These do not touch the imp
   questions above, but check any other worked example you copy.
