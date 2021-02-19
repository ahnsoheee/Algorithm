import sys, copy
sys.setrecursionlimit(100000)


N = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
  h = max(s[i])

result = 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, tmp):
  tmp[x][y] = 0
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]

    if (0 <= nx < N) and (0 <= ny < N) and tmp[nx][ny] != 0:
      dfs(nx, ny, tmp)

for k in range(1, h+1):
  tmp = copy.deepcopy(s)
  cnt = 0

  for i in range(N):
    for j in range(N):
      if tmp[i][j] <= k:
        tmp[i][j] = 0
  
  for i in range(N):
    for j in range(N):
      if tmp[i][j] != 0:
        dfs(i, j, tmp)
        cnt += 1
  
  result = max(result, cnt)

print(result)