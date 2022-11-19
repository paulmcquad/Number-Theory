# Paul McQuade <paulmcquad@gmail.com>
# GNU GPLv3

#  D2-Greatest Common Divisor gcd() of Three Numbers 
# https://www.youtube.com/watch?v=TtW4hNPYzAM


# importing "math" for mathematical operations
import math
	
a = int(input("1st:  "))
b = int(input("2nd:  "))
c = int(input("3rd:  "))

if __name__ == "__main__":
    print ('gcd({0}, {1}, {2}) = '.format(a,b,c), end ="")
    print (math.gcd(a, b, c))