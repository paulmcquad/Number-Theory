#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python3 program to check for Proth number

# Utility function to Check
# power of two

# A080076 - Proth primes: primes of the form k*2^m + 1 with odd k < 2^m, m >= 1. 


def isPowerOfTwo(n):

    return n and not n & n - 1


# Function to check if the
# Given number is Proth number or not

def isProthNumber(n):
    k = 1

    while k < n // k:
        # check if k divides n or not
        if n % k == 0:

            # Check if n / k is power of 2 or not
            if isPowerOfTwo(n // k):
                return True

        # update k to next odd number
        k = k + 2

    # If we reach here means
    # there exists no value of K
    # Such that k is odd number
    # and n / k is a power of 2 greater than k
    return False

#n = 5

n = int(input())


if isProthNumber(n - 1):
    print ('YES');
else:
    print ('NO');