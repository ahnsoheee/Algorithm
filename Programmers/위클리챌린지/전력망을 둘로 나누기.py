def solution(n, wires):
    answer = 100
    
    s = [[0] * n for _ in range(n)]
    
    for x, y in wires:
        s[x-1][y-1] = 1
        s[y-1][x-1] = 1
        
    for x, y in wires:
        visited = [0] * n
        s[x-1][y-1] = 0
        s[y-1][x-1] = 0
        
        cnt = dfs(s, 1, visited, n, 1)
        answer = min(answer, abs(n-cnt-cnt))
        
        s[x-1][y-1] = 1
        s[y-1][x-1] = 1

    return answer

def dfs(s, start, visited, n, cnt):
    visited[start-1] = 1
    
    for i in range(n):
        if(visited[i] == 0 and s[start-1][i] == 1):
            cnt = dfs(s, i+1, visited, n, cnt+1)
            
    return cnt