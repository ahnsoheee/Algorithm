## DFS (Depth First Search, 깊이 우선 탐색)
#### 시작 정점으로부터 연결 된 노드를 따라 마지막 노드까지 탐색하는 알고리즘

![dfs](https://user-images.githubusercontent.com/61968474/128961520-6868a8d2-8787-42d2-9c41-c78c46425b5c.PNG)

### 특징
- **모든 노드를 탐색해야할 때** 사용
- 재귀적

#### 장점
- 구현이 BFS보다 간단하다.
- 저장 공간이 비교적 적다.
- 목표 노드가 깊은 단계에 있을 경우 해를 빨리 구할 수 있다.

#### 단점
- 단순 검색 속도가 BFS보다 느리다.
- 목표까지의 경로가 여러 개인 경우 구한 해가 최적이 아닐 수 있다.
- 해가 없는 경로에 깊이 빠질 가능성이 있다. -> 임의의 깊이까지 탐색할 때까지 목표를 찾지 못한다면 다음 경로를 찾을 수도..

### Python 구현 코드

```python
check = [0 for i in range(N)] # 방문 여부를 확인
s = [[0, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0]] # 노드의 연결 상태가 저장된 이차원 배열

def dfs(v):
    check[v-1] = 1
    print(v, end = ' ')
    for i in range(N):
        if(check[i] == 0 and s[v-1][i] == 1):
            dfs(i+1)
   
print(dfs(1)) # 출력 : 1 2 4 3
```