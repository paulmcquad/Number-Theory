# Original Euclid's Algorithm
def euclid(a,b):
    print(a,b)
    if a == b: return a
    if a == 0: return b
    if b == 0: return a
    if a>b: return euclid(a-b,b)
    if a<b: return euclid(a,b-a)

# Improved Euclid's Algorithm
# a > b

def imp_euclid(a,b):
    print(a,b)
    if b == 0: return 0
    return imp_euclid(b, a%b)

if __name__ == "__main__":
    a = int(input())
    b = int(input())

    #print(euclid(a,b))
    print(imp_euclid(a,b))

