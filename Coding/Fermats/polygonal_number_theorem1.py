#!/usr/bin/python
# -*- coding: utf-8 -*-

# Fermat polygonal number theorem

def f(s, x, n=0, a=[]):
    y = ~n * (~-n - n * s / 2)
    return ((x < 1) * a * (len(a) <= s) if x < y else f(s, x, n + 1, a)
            or f(s, x - y, n, a + [y]))


print(f( 3,   1)) # 1
print(f( 3,   2)) # 1, 1
print(f( 6,   5)) # 1, 1, 1, 1, 1
print(f( 3,  17)) # 1, 6, 10
print(f( 4,  17)) # 1, 16
print(f( 5,  17)) # 5, 12
print(f( 3,  36)) # 36
print(f( 6,  43)) # 15, 28
print(f(17, 879)) # 17, 48, 155, 231, 428
print(f(23,4856)) # 130, 448, 955, 1398, 1925