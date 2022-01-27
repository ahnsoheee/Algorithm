# https://programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0
    row = len(board)
    col = len(board[0])
    d = [[0] * (col + 1) for _ in range(row+ 1)]

    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        if type == 1:
            degree = -degree
        
        d[r1][c1] += degree
        d[r1][c2+1] -= degree
        d[r2+1][c1] -= degree
        d[r2+1][c2+1] += degree

    # 위 -> 아래 누적합    
    for j in range(col):
        for i in range(1, row):
            d[i][j] += d[i-1][j]
            
    # 왼 -> 오 누적합
    for i in range(row):
        for j in range(1, col):
            d[i][j] += d[i][j-1]

    for i in range(row):
        for j in range(col):
            if board[i][j] + d[i][j] > 0:
                answer += 1

    return answer