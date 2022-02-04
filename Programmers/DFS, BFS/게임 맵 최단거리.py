# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    check = [[0] * m for _ in range(n)]
    check[0][0] = 1
    
    q = deque()
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()
        
        if x == n-1 and y == m-1:
            return check[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0 and maps[nx][ny] == 1:
                    check[nx][ny] = check[x][y] + 1
                    q.append([nx, ny])
            
    return -1