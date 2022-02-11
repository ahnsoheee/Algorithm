## 정렬 알고리즘
### 1. 버블 정렬
- 배열의 첛 원소부터 순차적으로 진행해, 현재 원소가 다음 원소의 값보다 크면 두 원소를 바꾸는 작업을 반복한다.
- 평균 / 최악 실행 시간 : O(N^2)
- 메모리 : O(1)
![image](https://user-images.githubusercontent.com/61968474/153554342-ffcfeca6-1b19-4241-9627-88d27b5fc787.png)


### 2. 선택 정렬
- 가장 작은 원소를 배열의 맨 앞의 원소와 바꾼다.
- 그 다음에는 두 번째로 작은 원소를 찾은 뒤 앞으로 보낸다.
- 이 작업을 모든 원소가 정렬될 때까지 반복한다.
- 평균 / 최악 실행 시간 : O(N^2)
- 메모리 : O(1)
![image](https://user-images.githubusercontent.com/61968474/153554231-1fa92545-05b5-4a56-9636-f4f651e5d355.png)

### 3. 합병 정렬
- 배열을 절반씩 나눠 각각을 정렬한 다음 이 둘을 합해 다시 정렬하는 방법이다.
- 나눈 배열을 정렬할 때도 같은 알고리즘을 사용해 결국 원소 한 개짜리 배열 두 개를 병합하게 된다.
- 이 알고리즘에서는 병합을 처리하는 것이 가장 복잡하다.
- 합병 대상이 되는 2개의 배열을 임시 배열에 복사하고, 각 배열의 처음부터 시작해 더 작은 값을 원래 배열에 복사해 넣는다.
- 두 배열 중 한 배열의 순회가 끝난 경우 다른 배열의 남은 부분을 원래 배열에 복사해 작업을 마친다.
- 평균 / 최악 실행 시간 : O(NlogN),
- 메모리 : 상황에 따라 다름

![image](https://user-images.githubusercontent.com/61968474/153554108-2768af22-2f1d-4209-bcbd-2340aa758e33.png)


### 4. 퀵 정렬
- 무작위로 선정된 한 원소(피봇)를 사용해 배열을 분할한다.
- 피봇보다 작은 원소들은 피봇 앞에, 큰 원소들은 뒤로 보낸다.
- 배열 분할 작업은 연속된 swap 연산을 통해 효율적으로 수행된다.
- 배열 분할에 사용되는 원소가 중간값에 가까운 값이 된다는 보장이 없기 때문에 정렬  알고리즘이 느리게 동작할 수 있어 최악의 경우 수행시간이 O(N^2)이 될 수 있다.
- 평균 실행 시간 : O(NlogN)
- 최악 실행 시간: O(N^2)
- 메모리 : O(logN)


![image](https://user-images.githubusercontent.com/61968474/153553372-66c44bd6-ebb6-44ff-8c21-e2306470f951.png)


### 5. 힙 정렬
- 최대 힙, 최소 힙 트리를 구성해 정렬하는 방법
- 정렬해야 할 요소들을 최대/최소 힙을 만든다.
- [힙(Heap)](https://github.com/ahnsoheee/TIL/blob/master/Data%20structure/Heap.md)

<details>
<summary>참고</summary>

- https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html
- https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html
- https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html
- https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html

</details>
