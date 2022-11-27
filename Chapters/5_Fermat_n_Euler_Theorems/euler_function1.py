# Euler's totient function
# https://en.wikipedia.org/wiki/Euler%27s_totient_function

# import totient() method from sympy
from sympy.ntheory.factor_ import totient

#n = 24
n = int(input("Enter N:\n"))

# Use totient() method
totient_n = totient(n)
	
print("Φ({}) = {} ".format(n, totient_n)) # 1 5 7 11 13 17 19 23
