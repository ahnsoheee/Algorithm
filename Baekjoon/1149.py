#N0.1149

import sys

N = int(sys.stdin.readline())

rgb = []
for i in range(N):
    rgb.append(list(map(int, sys.stdin.readline().split())))

cost = [[0]*3 for _ in range(N)]

for i in range(N):
    if i == 0:
        cost[i][0] = rgb[0][0]
        cost[i][1] = rgb[0][1]
        cost[i][2] = rgb[0][2]
    
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + rgb[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + rgb[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + rgb[i][2]

print(min(cost[N-1]))
