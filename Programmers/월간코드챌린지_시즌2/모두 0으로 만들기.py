import sys
sys.setrecursionlimit(10**7)

def solution(a, edges):
    global answer
    answer = 0
    if sum(a):
        return -1
    
    link = [[] for i in range(len(a))]
    visited = [0] * len(a)
    for i in range(len(edges)):
        link[edges[i][0]].append(edges[i][1])
        link[edges[i][1]].append(edges[i][0])
    
    
    def dfs(v):
        global answer
        if visited[v]:
            return 0
        visited[v] = 1

        for i in range(len(link[v])):
            a[v] += dfs(link[v][i])
        child = a[v]
        a[v] = 0
        answer += abs(child)
    
        return child
    
    dfs(0)
    if not a[0]:
        return answer
    
    return -1