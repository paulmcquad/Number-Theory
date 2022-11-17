# A formula based Python program to find sum
# of series with cubes of first n natural
# numbers

# A000537 		Sum of first n cubes; or n-th triangular number squared. 

# Returns the sum of series
def sumOfSeries(n):
	x = (n * (n + 1) / 2)
	return (int)(x * x)



# Driver Function


n = int(input())
print(sumOfSeries(n))

# Code Contributed by Mohit Gupta_OMG <(0_o)>
