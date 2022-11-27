# Euler's totient function
# https://en.wikipedia.org/wiki/Euler%27s_totient_function

import math

# A simple method to evaluate
# Euler Totient Function
def phi(n):

	result = 1
	for i in range(2, n):
		if (math.gcd(i, n) == 1):
			result+=1
	return result

for n in range(1, 11):
	print("Φ(",n,") = ",
		phi(n), sep = "")

