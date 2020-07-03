#No. 3190 '뱀'

import sys
from collections import deque

N = int(sys.stdin.readline())
s = [[0] * N for _ in range(N)]

for _ in range(int(sys.stdin.readline())):
    r, c = map(int, sys.stdin.readline().split())
    s[r-1][c-1] = 1

change = []
L = int(sys.stdin.readline())
for _ in range(L):
    x, c = input().split()
    change.append([int(x), c])

q = deque([[0, 0]])

#상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#처음 뱡향: 오른쪽 dx[1], dy[1]
d = 1

#다음 위치
nx = 0
ny = 0

#change 배열의 index
c = 0 

res = 0

while(1):
    res += 1
    nx += dx[d]
    ny += dy[d]
    
    if change[c][0] == res:
        if change[c][1] == 'D':
            d = ((d+1) % 4)
        else:
            d = ((d-1) % 4)
         
        if c != L-1:
            c += 1
   
    if 0 <= nx < N and 0 <= ny < N:
        for i in q:
            if [nx, ny] == i:
                print(res)
                exit(0)


        #다음 위치에 사과가 있는 경우
        if s[nx][ny] == 1:
            s[nx][ny] = 0
            q.append([nx, ny])
        
        elif s[nx][ny] == 0:
            q.append([nx, ny])
            x, y = q.popleft()

    else:
        break
        
print(res)
