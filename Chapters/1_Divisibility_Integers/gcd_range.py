from math import sqrt, gcd
def cf(num1,num2):
    n=[]
    g=gcd(num1, num2)
    for i in range(1, int(sqrt(g))+1):
        if g%i==0:
            n.append(i)
            if g!=i*i:
                n.append(int(g/i))
    return n


if __name__ == "__main__":
    print(cf(int(input("1st:")),int(input("2nd:"))))