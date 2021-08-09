from collections import deque

def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    visited = [0] * (n+1)
    visited[1] = 1
    queue = deque([[1, 0]])

    while(queue):
        node, depth = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                queue.append([i, depth+1])
                visited[i] = depth+1


    return visited.count(max(visited))