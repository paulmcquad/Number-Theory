# Python program for Lagrange's four square identity

# Lagrange's theorem tells us that each positive integer can be written as a sum of four squares. 

# Prints all the possible combinations 4 numbers
# whose sum of squares is equal to the given no.

def printFourSquares(a) :

	# loops checking the sum of squares
	i = 0
	while (i * i <= a) :
		j = i
		while (j * j <= a) :
			k = j
			while (k * k <= a) :
				l = k
				while (l * l <= a) :

					# if sum of four squares equals
					# the given no.
					if (i * i + j * j + k * k + l * l == a) :		

						# printing the numbers
						print ("{} = {}*{} + {}*{} +".
								format(a,i,i,j,j), end = " ")
						print ("{}*{} + {}*{}".
								format(k,k,l,l), end="\n")
					l = l + 1
				k = k + 1
			j = j + 1
		i = i + 1
					
# Driver Code
a = 74

# 74 = 0*0 + 0*0 + 5*5 + 7*7
# 74 = 0*0 + 1*1 + 3*3 + 8*8
# 74 = 0*0 + 3*3 + 4*4 + 7*7
# 74 = 1*1 + 1*1 + 6*6 + 6*6
# 74 = 2*2 + 3*3 + 5*5 + 6*6

printFourSquares(a)

# This code is contributed by Manish Shaw
# (manishshaw1)
