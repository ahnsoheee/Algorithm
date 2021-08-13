# 네트워크

def dfs(computers, check, v):
    check[v] = 1
    for i in range(len(check)):
        if check[i] == 0 and computers[v][i] == 1:
            dfs(computers, check, i)
        
def solution(n, computers):
    answer = 0
    
    check = [0] * n
    
    for i in range(n):
        if check[i] == 0:
            dfs(computers, check, i)
            answer += 1
            
    return answer
