# Pentagonal number theorem
# A001318 		Generalized pentagonal numbers: m*(3*m - 1)/2, m = 0, +-1, +-2, +-3, ....

def A001318(n):
    p = n % 2
    return (n + p)*(3*n + 2 - p) >> 3

print([A001318(n) for n in range(60)])  # Peter Luschny, Jul 15 2022 