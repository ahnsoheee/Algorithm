#No. 14503 '로봇 청소기'

import sys

N, M = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#현재 위치
x = r
y = c

res = 1

s[x][y] = 2

while(1):
    # 청소 가능한 공간 -> 있으면 1, 없으면 0
    e = 0
    for _ in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]  
        
        if s[nx][ny] == 0 and 0 <= nx < N and 0 <= ny < M:
            s[nx][ny] = 2
            res += 1
            x = nx
            y = ny
            e = 1
            break

    if e == 0:
        if d == 0:
            x += 1
        elif d == 1:
            y -= 1
        elif d == 2:
            x -= 1
        elif d == 3:
            y += 1

        if s[x][y] == 1:
            break

print(res)       
