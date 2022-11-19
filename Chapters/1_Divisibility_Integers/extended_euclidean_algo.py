def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def xgcd(a, b):
    a, b = max(a, b), min(a, b)

    q = [-1, -1]
    r = [a, b]
    s = [1, 0]
    t = [0, 1]

    while r[-1] > 0:
        q.append(r[-2] // r[-1])
        r.append(r[-2] % r[-1])
        s.append(s[-2] - q[-1] * s[-1])
        t.append(t[-2] - q[-1] * t[-1])

    return s[-2], t[-2]

if __name__ == "__main__":
    a = int(input("1st:  "))
    b = int(input("2nd:  "))

    print ('∴ gcd({0},{1}) = '.format(a,b), end ="")
    print (gcd(a, b))

    print ('∴ xgcd({0},{1}) = '.format(a,b), end ="")
    print (xgcd(a, b))
    #print("xgcd(a, b) = ax + by")