# Python 3 program to print all sophie
# germain prime number till n.

# Function to detect prime number
# here we have used sieve method
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# to detect prime number
def sieve(n, prime) :
	p = 2
	while( p * p <= n ):
		# If prime[p] is not changed,
		# then it is a prime
		if (prime[p] == True) :
			
			# Update all multiples of p
			for i in range(p * 2, n, p) :
				prime[i] = False
				
		p += 1
		
				
def printSophieGermainNumber(n) :
	# We have made array till 2*n +1
	# so that we can check prime number
	# till that and conclude about sophie
	# germain prime .
	prime = [True]*(2 * n + 1)
	
	sieve(2 * n + 1, prime)

	for i in range(2, n + 1) :
		
		# checking every i whether it is
		# sophie germain prime or not.
		if (prime[i] and prime[2 * i + 1]) :
			print( i , end = ", ")
			

# Driver Code
n = int(input())
printSophieGermainNumber(n)


# This code is contributed by Nikita Tiwari.
