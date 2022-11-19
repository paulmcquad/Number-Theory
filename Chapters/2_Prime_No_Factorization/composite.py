# Composite number
# https://en.wikipedia.org/wiki/Composite_number

# A002808 -  The composite numbers: numbers n of the form x*y for x > 1 and y > 1. 
# https://oeis.org/A002808

from sympy import isprime

def ok(n): return n > 1 and not isprime(n)

print([k for k in range(255) if ok(k)]) # Michael S. Branicky, Nov 07 2021 