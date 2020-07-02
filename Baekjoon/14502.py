#No. 14502 '연구소'

import sys, copy
from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0

def bfs(): #바이러스 퍼뜨리기
    global res
    t = copy.deepcopy(s)
    for i in range(N):
        for j in range(M):
            if t[i][j] == 2:
                q.append([i, j])
        
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if t[nx][ny] == 0:
                    t[nx][ny] = 2
                    q.append([nx, ny])

    cnt = 0
    for i in t:
        cnt += i.count(0)
    res = max(res, cnt)

def wall(x): #x = 벽의 갯수
    if x == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if s[i][j] == 0:
                s[i][j] = 1
                wall(x+1)
                s[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()
wall(0)
print(res)
