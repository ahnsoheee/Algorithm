# https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3

import heapq

def dijkstra(dist, adj, end):
    heap = []
    heapq.heappush(heap, (0, 1))
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        for n_cost, n_node in adj[node]:
            d = cost + n_cost
            
            if d < dist[n_node]:
                dist[n_node] = d
                heapq.heappush(heap, (d, n_node))
                
    return dist[end]
        
    
def solution(N, road, K):
    answer = 1
    
    dist = [float("inf")] * (N+1)
    dist[1] = 0
    adj = [[] for _ in range((N+1))]
    
    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])

        
    for i in range(N-1):
        result = dijkstra(dist, adj, i+2)
        
        if result <= K:
            answer += 1
            
    return answer