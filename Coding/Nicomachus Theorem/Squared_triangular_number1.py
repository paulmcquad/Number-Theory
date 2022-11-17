# Simple Python program to find sum of series
# with cubes of first n natural numbers

#A000537 		Sum of first n cubes; or n-th triangular number squared. 

# Returns the sum of series
def sumOfSeries(n):
	sum = 0
	for i in range(1, n + 1):
		sum += i * i*i
		
	return sum


# Driver Function
#n = 5

n = int(input())

print(sumOfSeries(n))

# Code Contributed by Mohit Gupta_OMG <(0_o)>
