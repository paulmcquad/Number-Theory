# Python3 implementation of above approach

# Number of ways of writing n
# as a sum of 4 squares
def sum_of_4_squares(n):

	# sum of odd and even factor
	i, odd, even = 0,0,0

	# iterate from 1 to the number
	for i in range(1,int(n**(.5))+1):
		# if i is the factor of n
		if (n % i == 0):
			
			# if factor is even
			if (i % 2 == 0):
				even += i

			# if factor is odd
			else:
				odd += i

			# n/i is also a factor
			if ((n // i) != i):
				
				# if factor is even
				if ((n // i) % 2 == 0):
					even += (n // i)

				# if factor is odd
				else:
					odd += (n // i)
			
		
	
	# if n is odd
	if (n % 2 == 1):
		return 8 * (odd + even)

	# if n is even
	else :
		return 24 * (odd)

# Driver code

n = 4

print(sum_of_4_squares(n))
