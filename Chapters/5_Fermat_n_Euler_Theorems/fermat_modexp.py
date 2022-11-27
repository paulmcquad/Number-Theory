#  Modular Exponentiation (Part 1) 
# https://www.youtube.com/watch?v=_gYUlvcnjs0

# Modular exponentiation made easy 
# https://www.youtube.com/watch?v=tTuWmcikE0Q

# Iterative Function to calculate (x^y)%p in O(log y)
def power(x, y, p):

	# Initialize result
	res = 1

	while (y > 0):

		# If y is odd, multiply x with result
		if ((y & 1) != 0):
			res = res * x

		# y must be even now
		y = y >> 1 # y = y/2
		x = x * x # Change x to x^2

	return res % p

x = int(input("Enter x:\n"))
y = int(input("Enter y:\n"))
p = int(input("Enter p:\n"))

#Ex1
#x = 23
#y = 3
#p = 30

#23^3 mod 30 = 17

#Ex2
#x = 31
#y = 500
#p = 30

#31^500 mod 30 = 1

#Ex3
#x = 242
#y = 329
#p = 243

#242^329 mod 243 = 242


#Ex4
#x = 11
#y = 7
#p = 13

#11^7 mod 13 = 2

print("∴ {0}^{1} (mod {2}) ≡".format(x,y,p), power(x, y, p))
