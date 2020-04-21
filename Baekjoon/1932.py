#No.1932 '정수 삼각형'

import sys

n = int(sys.stdin.readline())

d = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
l = 2
for i in range(1, n):
    for j in range(l):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == len(d[i]) - 1:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])
    l += 1
    
print(max(d[n-1]))
