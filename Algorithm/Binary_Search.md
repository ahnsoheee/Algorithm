## Binary Search (이진 탐색)
#### 정렬된 배열을 반으로 나누어 탐색하며 값을 찾는 알고리즘

- 선행조건 : 배열이 정렬되어 있어야 한다.
- 시간복잡도 : O(logN)

1. left = 0, right = 배열의 맨 끝 인덱스 값으로 초기화한다.
2. target이 중간 값보다 작은 경우 왼쪽 부분만 선택 -> right가 mid-1이 됨
3. target이 중간 값보다 큰 경우 오른쪽 부분만 선택 -> left가 mid+1이 됨
4. target과 중간 값과 같으면 탐색 종료
5. target을 찾을 때까지 2 ~ 4 반복

```python

def binary_serach(data, target):
    left = 0
    right = len(data)-1

    while left <= right:
        mid = (left + right) // 2
        
        if target < mid:
            right = mid - 1
        elif target > mid:
            left = mid + 1
        else:
            return mid
    
    return -1 #값을 찾지 못한 경우
        
```
