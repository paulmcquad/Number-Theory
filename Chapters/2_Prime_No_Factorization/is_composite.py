from sympy import *

if __name__ == "__main__":

    n = int(input("Composite or not: "))

    # Use sympy.is_composite method
    composite = simplify(n).is_composite
    print(composite)