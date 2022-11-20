# Paul McQuade <paulmcquad@gmail.com>
# GNU GPLv3

# LCM for beginners (old version)
# https://www.youtube.com/watch?v=Z6-LksV08qU

# importing "math" for mathematical operations
import math
	
a = int(input("1st:  "))
b = int(input("2nd:  "))

if __name__ == "__main__":
    print ('∴ lcm({0},{1}) = '.format(a,b), end ="")
    print (math.lcm(a, b))