# Euler's totient function
# https://en.wikipedia.org/wiki/Euler%27s_totient_function

# https://www.youtube.com/watch?v=DwQ7-k9LkJ4

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
	print("∴ Φ(",n,") = ",
		phi(n), sep = "")

