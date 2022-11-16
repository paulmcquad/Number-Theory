# Python3 program to check
# Chen Prime number
# A109611 - Chen primes: primes p such that p + 2 is either a prime or a semiprime.

#https://oeis.org/A109611
import math
		
# Utility function to Check
# Semi-prime number

def isSemiPrime(num):
	cnt = 0

	for i in range(2, int(math.sqrt(num)) + 1):
		while num % i == 0:
			num /= i
			cnt += 1 # Increment count
					# of prime number

		# If count is greater than 2,
		# break loop
		if cnt >= 2:
			break
	# If number is greater than 1, add it to
	# the count variable as it indicates the
	# number remain is prime number
	if(num > 1):
		cnt += 1

	# Return '1' if count is equal to '2' else
	# return '0'
	return cnt == 2



# Utility function to check
# if a number is prime or not
def isPrime(n) :
	# Corner cases
	if (n <= 1) :
		return False
	if (n <= 3) :
		return True
	
	# This is checked so that we can skip
	# middle five numbers in below loop
	if (n % 2 == 0 or n % 3 == 0) :
		return False
	
	i = 5
	while(i * i <= n) :
		if (n % i == 0 or n % (i + 2) == 0) :
			return False
		i = i + 6
	
	return True

# Function to check if the
# Given number is Chen prime number or not
		
def isChenPrime( n):

	if(isPrime(n) and (isSemiPrime(n + 2) or isPrime(n + 2))):
		return True
	else:
		return False
			
# Driver code


#n = 7

n = int(input())

if(isChenPrime(n)):
	print("YES");
else:
	print("NO");
	
