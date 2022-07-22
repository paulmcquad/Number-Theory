#
# ∑m=1nm=n×(n+1)2
#
def s1tnvm(n):
  return (n*(n+1))//2 

s = input("Summation 1 to n:" )
w = int(s)

print("n:", s1tnvm(w))
