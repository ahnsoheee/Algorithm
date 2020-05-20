#No. 5532 '방학 숙제'

import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if A % C != 0:
    max_result = A // C + 1
else:
    max_result = A // C

if B % D != 0:
    if max_result < (B // D + 1):
        max_result = B // D + 1
    
else:
    if max_result < (B // D):
        max_result = B // D

print(L-max_result)
