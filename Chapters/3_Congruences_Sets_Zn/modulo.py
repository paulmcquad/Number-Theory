# What does a ≡ b (mod n) mean? Basic Modular Arithmetic, Congruence 
# https://www.youtube.com/watch?v=6dZLq77gSGU

import math

x = int(input("Enter x number:\n"))
n = int(input("Enter Mod number:\n"))

#x = 14
#n = 3
#r = 2

#print(f'∴ {x} (mod {n}) =', math.fmod(x , n)) # Outputs remainder

#x = 5
#n = 3
#r = 2

print(f'∴ {x} (mod {n}) =', math.fmod(x , n)) # Outputs remainder

# 14 ≡  5 (mod 3)
# They return the same remainder which is (r = 2)

# Identity or Equation - What is the difference?
# https://www.youtube.com/watch?v=M89lTUQBtTo
