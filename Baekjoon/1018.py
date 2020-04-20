#No.1018 '체스판 다시 칠하기'

import sys

N, M = map(int, sys.stdin.readline().split())

board = [list(map(str, input())) for i in range(N)]

BW = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

WB = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

cnt = []

def check(i, j):
    b_cnt = 0
    w_cnt = 0
    for m in range(8):
        for n in range(8):
            if board[i+m][j+n] != BW[m][n]:
                b_cnt += 1
    
    for m in range(8):
        for n in range(8):
            if board[i+m][j+n] != WB[m][n]:
                w_cnt += 1

    return min(b_cnt, w_cnt)


for i in range(N-7):
    for j in range(M-7):
        cnt.append(check(i, j))
            
print(min(cnt))
