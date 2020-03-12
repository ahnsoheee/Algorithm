#No. 2231

import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    if N == i + sum(list(map(int, str(i)))):
        print(i)
        break
    
    if i == N: 
        print(0)
