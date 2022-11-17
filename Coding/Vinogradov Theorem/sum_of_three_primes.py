#!/usr/bin/python
# -*- coding: utf-8 -*-

# A068307 -	From Goldbach problem: number of decompositions of n into a sum of three primes.
	
from sympy import isprime, primerange, floor

def A068307(n):

    s = 0
    for p in primerange((n + 2) // 3, n - 3):
        for q in primerange((n - p + 1) // 2, min(n - p - 2, p) + 1):
            if isprime(n - p - q):
                s += 1
    return s

print([A068307(n) for n in range(1, 101)])
