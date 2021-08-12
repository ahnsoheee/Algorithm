## Floyd Warshall
#### 모든 정점에서 모든 정점으로의 최단 경로를 구하는 알고리즘

cf) 다익스트라 알고리즘 : 하나의 정점에서 다른 정점까지의 최단 경로를 구하는 알고리즘

#### 특징
- 시간복잡도 : O(N^3)
- 음수 사이클이 없는 그래프라면 음수 가중치가 있어도 동작한다.

#### Python 구현 코드

- 입력 : i에서 j로 가는 거리를 저장한 배열 s -> s[i][j]
- 출력 : i에서 j로 가는 최소 거리

```python
import sys

def Folyd(s):
    Inf = 100000000 # 연결되어 있지 않음을 의미
    d = [[Inf] * n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 자기 자신으로 오는 경우
                if j == i:
                    d[i][j] = 0
                    
                # k를 거쳐서 가는 것, 원래 값 중 최소 값
                else:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                        
    for i in range(n):
        for j in range(n):
            if d[i][j] == Inf:
                print(0, end = ' ')
            else:
                print(d[i][j], end = ' ')
        print()
```