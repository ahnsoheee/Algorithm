#N0.15650

import sys

N, M = map(int, sys.stdin.readline().split())
res = [0] * M
check = [0] * N

def go(index, start, n, m):
    if index == m:
        print(*res)
        return
    
    else:
        for i in range(start, n+1):
            if check[i-1] == 0:
                check[i-1] = 1
                res[index] = i
                go(index+1, i+1, n, m)
                check[i-1] = 0
    
go(0, 1, N, M)
