## BFS (Breadth First Search, 너비 우선 탐색)
#### 시작 정점으로부터 거리가 가까운 정점 순(너비 우선)으로 인접한 노드를 탐색하는 알고리즘

### 특징
- **최단 경로를 찾을 때** 사용
- 일반적으로 큐(Queue) 사용 (선입선출 방식을 사용해야 함)
- 재귀적 x
- 시간복잡도 : 인접 리스트로 구현된 경우 O(|V|+|E|), 인접 행렬로 구현했을 경우 O(|V|^2)

#### 장점
- 최단 경로를 보장
- 단순 검색 속도가 DFS보다 빠르다.

#### 단점
- 경로가 긴 경우 많은 메모리를 필요로 한다.


- 입력 : 노드의 갯수 n, 그래프 graph, 시작 노드 v

```python
n = 6 
graph = {1: [3, 2], 2: [3, 1, 4, 5], 3: [6, 4, 2, 1], 4: [3, 2], 5: [2], 6: [3]}
visited = [0] * (n+1)

from collections import deque

def bfs(n, graph, v):
    visited[v] = 1
    queue = deque([v])

    while(queue):
        node = queue.popleft()  
        print(node, end = ' ') 
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

```
