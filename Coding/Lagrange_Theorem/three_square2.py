from itertools import count, islice

def A004215_gen(startvalue=1): # generator of terms >= startvalue

    return filter(lambda n:not (m:=(~n&n-1).bit_length())&1 and (n>>m)&7==7, count(max(startvalue, 1)))

A004215_list = list(islice(A004215_gen(), 30)) # Chai Wah Wu, Jul 09 2022 
print(A004215_list);