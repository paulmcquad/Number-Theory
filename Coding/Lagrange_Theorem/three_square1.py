def valuation(n, b):
    v = 0
    
    while n > 1 and n%b == 0: n //= b; v += 1
    return v

def ok(n): return n//4**valuation(n, 4)%8 == 7 # after M. F. Hasler

print(list(filter(ok, range(344))))