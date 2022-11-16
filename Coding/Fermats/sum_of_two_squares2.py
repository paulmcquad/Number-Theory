# An efficient approach based implementation
# to find if a number can be written as sum
# of two squares.

# function to check if there exist two
# numbers sum of whose squares is n.
def sumSquare(n):

	s = dict()
	for i in range(n):

		if i * i > n:
			break

		# store square value in hashmap
		s[i * i] = 1

		if (n - i * i) in s.keys():
			print((n - i * i)**(1 / 2),
					"^2 +", i, "^2")
			return True
		
	return False

# Driver Code
n = int(input())

if n==1:
	print('0^2 + 1^2')
elif (sumSquare(n)):
	print("Yes")
else:
	print("No")

# This code is contributed by Mohit Kumar
