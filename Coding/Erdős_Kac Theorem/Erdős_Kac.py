# Erdős–Kac theorem
# https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Kac_theorem

# standard normal distribution. ( ω ( n ) \omega (n) is sequence A001221 in the OEIS.) 

# Number of distinct primes dividing n (also called omega(n)). 
from sympy.ntheory import primefactors

print([len(primefactors(n)) for n in range(1, 1001)])
