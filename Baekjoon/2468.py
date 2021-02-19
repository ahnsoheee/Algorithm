import sys, copy

N = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
  h = max(s[i])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
  for i in range(4):
    nx, ny = x + dx[i], dy[i]
    

for k in range(1, h-1):
  tmp = copy.deepcopy(s)
  for i in range(N):
    for j in range(N):
      if tmp[i][j] <= k:
        tmp[i][j] = 0
  
  for i in range(N):
    for j in range(N):
      if tmp[i][j] != 0:
        dfs(i, j)