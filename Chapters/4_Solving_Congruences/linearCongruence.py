# Function to stores the values of x and y
# and find the value of gcd(a, b)
def ExtendedEuclidAlgo(a, b):
	
	# Base Case
	if a == 0 :
		return b, 0, 1
		
	gcd, x1, y1 = ExtendedEuclidAlgo(b % a, a)
	
	# Update x and y using results of recursive
	# call
	x = y1 - (b // a) * x1
	y = x1
	
	return gcd, x, y
	
# Function to give the distinct
# solutions of ax = b (mod n)
def linearCongruence(A, B, N):
	
	A = A % N
	B = B % N
	u = 0
	v = 0
	
	# Function Call to find
	# the value of d and u
	d, u, v = ExtendedEuclidAlgo(A, N)
	
	# No solution exists
	if (B % d != 0):
		print("No Solutions :", -1)
		return
	
	# Else, initialize the value of x0
	x0 = (u * (B // d)) % N
	if (x0 < 0):
		x0 += N
	
	# Print all the answers
	for i in range(d):
		print("x ≡",(x0 + i * (N // d)) % N, '(mod {0})'.format(N), end = " \n")

# Linear Congruence Solver – A Calculator
# https://www.a-calculator.com/congruence/

# Solving Linear Congruences, Modular Arithmetic 
# https://www.youtube.com/watch?v=ViqgSWoSxN8

# Input
#A = 3
#B = 1
#M = 4

#Ax ≡ B (mod M)
#3x ≡ 1 (mod 4)

A = int(input("Enter A number:\n"))
B = int(input("Enter B number:\n"))
M = int(input("Enter M number:\n"))

# Function Call
linearCongruence(A, B, M)