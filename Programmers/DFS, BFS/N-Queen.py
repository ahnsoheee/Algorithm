# https://programmers.co.kr/learn/courses/30/lessons/12952

def n_queen(n, x, queen):
    result = 0
    
    if x == n:
        return 1
    
    for i in range(n):
        queen[x] = i
        
        if check(x, queen):
            result += n_queen(n, x+1, queen)

    return result

def check(x, queen):
    for i in range(x):
        if queen[x] == queen[i] or abs(x-i) == abs(queen[x] - queen[i]):
            return False
    return True
    
def solution(n):
    queen = [0] * n
    answer = n_queen(n, 0, queen)
    
    return answer