## Lower Bound
#### target 보다 이상인 값이 처음 나오는 위치를 리턴

- 선행조건 : 배열이 정렬되어 있어야 한다.
- 시간복잡도 : O(logN)

```python
def lower_bound(data, target):

    left, right = 0, len(data)

    while left < right:
        mid = (left + right) // 2

        if data[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    return right
```
