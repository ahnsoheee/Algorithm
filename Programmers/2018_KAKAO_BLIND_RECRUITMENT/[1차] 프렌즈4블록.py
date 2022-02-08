# https://programmers.co.kr/learn/courses/30/lessons/17679

dx, dy = [0, 1, 1], [1, 0, 1]

def check(board, x, y, n, m):    

    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n:
            if board[x][y] != board[nx][ny]:
                return False
    
    return True

def solution(m, n, board):
    answer = 0
    popList = []

    for i in range(m):
        board[i] = list(board[i])    
        
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '-': 
                    continue
                    
                if check(board, i, j, n, m):
                    popList.append((i, j))

                    for k in range(3):
                        popList.append((i+dx[k], j+dy[k]))
        
        if len(popList) == 0:
            return answer
        
        popList = sorted(list(set(popList)), reverse=True)
        for x, y in popList:
            answer += 1
            board[x][y] = '-'

        for x, y in popList:
            for i in range(x, -1, -1):
                if board[i][y] == '-':
                    for j in range(i-1, -1, -1):
                        if board[j][y] != '-':
                            board[i][y] = board[j][y]
                            board[j][y] = '-'
                            break

        popList = []