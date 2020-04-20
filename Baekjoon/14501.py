#No.14501 '퇴사'

import sys

N = int(sys.stdin.readline())
T, P  = [], []
cost = [0] * (N + 1)
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(N):
    if T[i] <= N - i:
        cost[i + T[i]] = max(cost[i+T[i]], cost[i]+P[i]) 

    cost[i+1] = max(cost[i+1], cost[i])
print(cost[N])
