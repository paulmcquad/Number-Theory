import math

def power(x, y, m):

	if (y == 0):
		return 1
	p = power(x, y // 2, m) % m
	p = (p * p) % m

	return p if(y % 2 == 0) else (x * p) % m

# Function to find modular
# inverse of a under modulo m
# Assumption: m is prime


def modInverse(a, m):

	if (math.gcd(a, m) != 1):
		print("Inverse doesn't exist")

	else:

		# If a and m are relatively prime, then
		# modulo inverse is a^(m-2) mode m
		print("Modular multiplicative inverse:",
			power(a, m - 2, m))

# Driver code

a = int(input("Enter A:\n"))
m = int(input("Enter M:\n"))

#a = 3
#m = 11
modInverse(a, m)