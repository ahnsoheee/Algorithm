#15686 '치킨 배달'

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

s = []
for _ in range(N):
    s.append(list(map(int, sys.stdin.readline().split())))

chicken = []  

for i in range(N):
    for j in range(N):
        if s[i][j] == 2:
            chicken.append([i+1, j+1])

cnt = [i for i in range(len(chicken))]
com = list(combinations(cnt, M))


res = 99999
for i in range(len(com)):
    shop = []
    for j in range(M):
        shop.append(chicken[com[i][j]])

    chi_len = 0
    for j in range(N):
        for k in range(N):
            tmp = 100
            if s[j][k] == 1:
                for l in range(M):
                    tmp = min(tmp, abs(j + 1 - shop[l][0]) + abs(k + 1 - shop[l][1]))
                chi_len += tmp
    res = min(res, chi_len)

print(res)
