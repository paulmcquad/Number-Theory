# Python3 implementation of the above approach
from math import gcd, sqrt

# Utility function to check
# whether two numbers is
# co-prime or not
def coprime(a, b) :
	
	if (gcd(a, b) == 1) :
		return True;
		
	else :
		return False;

# Utility function to check
# whether a number is prime
# or not
def isPrime(n) :

	# Corner case
	if (n <= 1) :
		return False;

	if (n == 2 or n == 3) :
		return True;

	# Check from 2 to sqrt(n)
	for i in range(2, int(sqrt(n)) + 1) :
		if (n % i == 0) :
			return False;

	return True;

# finding the Prime numbers
def findNumbers(a, b, n) :

	possible = True;

	# Checking whether given
	# numbers are co-prime
	# or not
	if (not coprime(a, b)) :
		possible = False;

	c1 = 1;
	c2 = 1;

	num1 = 0;
	num2 = 0;

	# To store the N primes
	st = set();
	
	# If 'possible' is true
	if (possible) :

		# Printing n numbers
		# of prime
		while (len(st) != n) :

			# checking the form of a+nb
			num1 = a + (c1 * b);
			
			if (isPrime(num1)):
				
				st.add(num1);
				
			c1 += 1;

			# Checking the form of b+na
			num2 = b + (c2 * a);
			
			if (isPrime(num2)):
				st.add(num2);
	
			c2 += 1;

		for i in st :
			print(i, end = " ");

	# If 'possible' is false
	# return -1
	else :
		print("-1");

# Driver Code
if __name__ == "__main__" :

	a = 2;
	b = 1;
	n = 10;

	findNumbers(a, b, n);

# This code is contributed by AnkitRai01
