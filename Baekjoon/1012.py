import sys
sys.setrecursionlimit(50000)

T = int(sys.stdin.readline())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
  s[x][y] = 0
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    
    if 0 <= nx < M and 0 <= ny < N:
      if s[nx][ny] == 1:
        dfs(nx, ny)

for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().split())
  result = 0
  s = [[0] * N for _ in range(M)]
  print(s)
  for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    s[x][y] = 1
  
  for i in range(M):
    for j in range(N):
      if s[i][j] == 1:
        dfs(i, j)
        result += 1

  print(result)

  

  