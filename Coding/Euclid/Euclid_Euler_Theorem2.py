# Python3 code to verify Euclid Euler Theorem
# A000396 - https://oeis.org/A000396

from sympy import divisor_sigma

def ok(n): return n > 0 and divisor_sigma(n) == 2*n

print([k for k in range(9999) if ok(k)]) # Michael S. Branicky, Mar 12 2022 