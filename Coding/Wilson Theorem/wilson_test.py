# Python3 implementation to check if a number is
# prime or not using Wilson Primality Test

# Function to calculate the factorial
def fact(p):
	
	if (p <= 1):
		return 1

	return p * fact(p - 1)

# Function to check if the
# number is prime or not
def isPrime(p):
	
	if (p == 4):
		return 0
		
	return (fact(p >> 1) % p)


n = int(input())

if (isPrime(n) == 0):
	print(0)
else:
	print(1)