#No. 11404 '플로이드'

import sys
Inf = 100000000

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

d = [[Inf] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if d[a-1][b-1] > c:
        d[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if j == i:
                d[i][j] = 0
                
            else:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                    
for i in range(n):
    for j in range(n):
        if d[i][j] == 100001:
            print(0, end = ' ')
        else:
            print(d[i][j], end = ' ')
    print()
