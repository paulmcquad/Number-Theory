# Python3 implementation of the
# above approach

# A080076 - Proth primes: primes of the form k*2^m + 1 with odd k < 2^m, m >= 1. 

import math as mt

prime = [0 for i in range(1000000)]

# Calculate all primes upto n.
def SieveOfEratosthenes(n):
	
	# Initialize all entries it as true.
	# A value in prime[i] will finally
	# false if i is Not a prime, else true.
	for i in range(1, n + 2):
		prime[i] = True

	prime[1] = False

	for p in range(2, mt.ceil(n**(0.5))):

		# If prime[p] is not changed,
		# then it is a prime
		if (prime[p] == True):

			# Update all multiples of p
			# greater than or equal to
			# the square of it numbers
			# which are multiple of p and are
			# less than p^2 are already been marked.
			for i in range(p * p, n + 1, p):
				prime[i] = False

# Utility function to check power of two
def isPowerOfTwo(n):
	return (n and (n & (n - 1)) == False)

# Function to check if the Given
# number is Proth number or not
def isProthNumber(n):
	
	k = 1
	while (k < (n // k)):

		# check if k divides n or not
		if (n % k == 0):

			# Check if n/k is power of 2 or not
			if (isPowerOfTwo(n // k)):
				return True
		
		# update k to next odd number
		k = k + 2
	
	# If we reach here means there
	# exists no value of K such
	# that k is odd number and n/k
	# is a power of 2 greater than k
	return False

# Function to check whether the given
# number is Proth Prime or Not.
def isProthPrime(n):

	# Check n for Proth Number
	if (isProthNumber(n - 1)):

		# if number is prime, return true
		if (prime[n]):
			return True
		else:
			return False
	
	else:
		return False

# Driver Code

#n = 41

n = int(input())


# if number is proth number,
# calculate primes upto n
SieveOfEratosthenes(n)

for i in range(1, n + 1):
	
	# Check n for Proth Prime
	if isProthPrime(i) == True:
		print(i, end=", ")
		
# This code is contributed by
# Mohit kumar 29
