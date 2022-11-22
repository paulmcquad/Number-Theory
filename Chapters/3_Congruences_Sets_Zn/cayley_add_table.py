import numpy as np

def is_associative(table, n):
    return all(table[x][table[a][y]] == table[table[x][a]][y] \
           for a in np.arange(n) for x in range(n) for y in range(n))

# calay table for ({0,1,...,n-1}, +n), addition modulo n, which is an Abelian group

n = int(input("Enter addition Table Zn:\n"))
calay_table = np.zeros((n, n), dtype=int)
calay_table[0] = np.arange(n)
for i in range(1, n):
    calay_table[i] = np.roll(calay_table[i-1],-1)



print(calay_table)
#n = 4

# [[0 1 2 3]
# [1 2 3 0]
# [2 3 0 1]
# [3 0 1 2]]

# print(is_associative(calay_table, n))
# True