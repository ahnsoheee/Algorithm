#No. 11720

import sys

L = int(sys.stdin.readline())

N = list(sys.stdin.readline())

sum = 0

for i in range(L):
    sum += int(N[i])

print(sum)
