#N0.15649

#1

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

num = [i for i in range(1,N+1)]

result = permutations(num, M)
for i in result:
    print(' '.join(map(str, i)))
    
#2
    
import sys

N, M = map(int, sys.stdin.readline().split())
res = [0] * M
check = [0] * N
def go(index, n, m):
    if index == m:
        print(*res)
        return
    
    else:
        for i in range(1, n+1):
            if check[i-1] == 0:
                check[i-1] = 1
                res[index] = i
                go(index+1, n, m)
                check[i-1] = 0
    
go(0, N, M)
