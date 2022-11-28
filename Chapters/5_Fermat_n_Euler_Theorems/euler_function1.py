# Euler's totient function
# https://en.wikipedia.org/wiki/Euler%27s_totient_function

# https://www.youtube.com/watch?v=DwQ7-k9LkJ4

# import totient() method from sympy
from sympy.ntheory.factor_ import totient

#n = 24
n = int(input("Enter N:\n"))
	
print("∴ Φ({}) = {} ".format(n, totient(n))) # 1 5 7 11 13 17 19 23
