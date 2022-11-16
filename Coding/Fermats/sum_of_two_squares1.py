# A brute force approach based
# implementation to find if a number
# can be written as sum of two squares.

# function to check if there exist two
# numbers sum of whose squares is n.
def sumSquare( n) :
	i = 1
	while i * i <= n :
		j = 1
		while(j * j <= n) :
			if (i * i + j * j == n) :
				print(i, "^2 + ", j , "^2" )
				return True
			j = j + 1
		i = i + 1
		
	return False

# driver Program
#n = 25

n = int(input())

if (sumSquare(n)) :
	print("Yes")
else :
	print( "No")
	

# This code is contributed by Nikita Tiwari.
