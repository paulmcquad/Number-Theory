# Paul McQuade <paulmcquad@gmail.com>
# GNU GPLv3

#  D2-Greatest Common Divisor gcd(a,b) of Two Numbers 
# https://www.youtube.com/watch?v=TtW4hNPYzAM


# importing "math" for mathematical operations
import math
	
a = int(input("1st:  "))
b = int(input("2nd:  "))

print ('gcd({0},{1}) = '.format(a,b), end ="")
print (math.gcd(a, b))