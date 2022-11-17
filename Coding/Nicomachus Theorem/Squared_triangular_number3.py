# Efficient Python program to find sum of cubes
# of first n natural numbers that avoids
# overflow if result is going to be with in
# limits.

# A000537 		Sum of first n cubes; or n-th triangular number squared. 

# Returns the sum of series
def sumOfSeries(n):
	x = 0
	if n % 2 == 0 :
		x = (n / 2) * (n + 1)
	else:
		x = ((n + 1) / 2) * n
		
	return (int)(x * x)


# Driver Function
n = int(input())
print(sumOfSeries(n))

# Code Contributed by Mohit Gupta_OMG <(0_o)>
