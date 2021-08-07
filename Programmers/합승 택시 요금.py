import heapq

INF = int(1e9)  

def dijkstra(graph, start, end):
    distances = [INF] * len(graph)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        curr_d, curr_node = heapq.heappop(queue)

        if distances[curr_node] < curr_d: continue

        for next_d, next_node in graph[curr_node]:
            distance = curr_d + next_d

            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))
        
    return distances[end]

def solution(n, s, a, b, fares):   
    graph = [[] for _ in range(n)]
 
    answer = dijkstra(graph, s-1, a-1) + dijkstra(graph, s-1, b-1)
    answer = INF
    for i, j, cost in fares:
        graph[i-1].append((cost, j-1))
        graph[j-1].append((cost, i-1))
    
    for i in range(n):
        answer = min(answer, dijkstra(graph, s-1, i) + dijkstra(graph, i, a-1) + dijkstra(graph, i, b-1))
  
    return answer