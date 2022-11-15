# Glaisher's Theorem
# https://oeis.org/A000009

def A000009(n):
    A = [1] + [0] * n
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            A[j] += A[j-i]
    return A[n]

print(', '.join([str(A000009(n)) for n in range(0, 20)]))

#for x in range(0, 20):
#    print(A000009(x),end=", ")
