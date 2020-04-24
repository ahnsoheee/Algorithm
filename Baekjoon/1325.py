#No.1325 '효율적인 해킹'

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

s = [[] * N for _ in range(N)]

res = []

def bfs(v):
    q = deque()
    check = [0] * N
    check[v] = 1
    q.append(v)
    cnt = 1
    
    while(q):
        v = q.popleft()
        for i in s[v]:
            if check[i] == 0:
                q.append(i)
                check[i] = 1
                cnt += 1
    return cnt
        
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    s[b-1].append(a-1)

for i in range(N):
    res.append(bfs(i))

for i in range(len(res)):
    if res[i] == max(res):
        print(i+1, end = ' ')
