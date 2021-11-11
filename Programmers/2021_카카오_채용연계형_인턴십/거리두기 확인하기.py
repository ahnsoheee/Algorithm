from collections import deque


def bfs(p, x, y, d):
    di = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0] * 5 for _ in range(5)]

    q = deque([[x, y, d]])

    while q:
        x, y, d = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + di[i][0]
            ny = y + di[i][1]
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = 1

                if p[nx][ny] == 'P':
                    if nd <= 2:
                        return False

                elif p[nx][ny] == 'O':
                    if nd == 1:
                        q.append([nx, ny, nd])

    return True


def solution(places):
    answer = []

    for p in places:
        flag = 1

        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    result = bfs(p, i, j, 0)
                    if not result:
                        flag = 0

        answer.append(flag)

    return answer
