## Dijkstra
#### 출발점에서 도착점까지의최단 경로를 찾는 알고리즘

- 시간복잡도 : O(N^2) (우선순위 큐를 활용하면 O(NlogN))
- 입력 : 가중치 그래프 G, 점의 수 n, 선분의 수 m, 출발점 s
- 출력 : 출발점 s로부터 (n-1)개의 점까지 각각 최단 거리를 저장한 배열 D

1. 배열 D를 ∞으로 초기화 시킨다. 단, D[s] = 0으로 초기화한다.
2. while(s로부터 최단 거리가 확정되지 않은 점이 있으면) {
3. 현재까지 s로부터 최단 거리가 확정되지 않은 점 v에 대해 최소 D[v]를 가진 점 v_min을 선택하고, 출발점 s로부터 v_min까지의 최단 거리 D[v_min]을 확정시킨다.
4. s로부터 현재보다 짧은 거리로 점 v_min을 통해 우회 가능한 각 점 w에 대해서 D[w]를 갱신한다.
}
5. return D  


#### 우선순위 큐를 활용한 코드

```python
import heapq

def dijkstra(graph, s):
    distances = {node: float('inf') for node in graph}
    distances[s] = 0
    queue = []
    heapq.heappush(queue, [distances[s], s])

    while queue:
        curr_d, curr_node = heapq.heappop(queue)

        if distances[curr_node] < curr_d: continue

        for next_d, next_node in graph[curr_node].items():
            distance = curr_d + next_node

            if distance < distances[next_d]:
                distances[next_d] = distance
                heapq.heappush(queue, [distance, next_d])
        
    return distances
```