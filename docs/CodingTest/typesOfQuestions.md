# 문제 유형별 정리

## 1. DFS/BFS

### 스택
``` python
stack = []  // 별도의 라이브러리를 사용할 필요가 없다
stack.append(1)
stack.pop()

not stack   // 비어있으면 1
stack[-1] if stack else '-1'    // top, 가장 위에 있는 숫자
```

### 큐
``` python
from collections import deque   // 덱 라이브러리 사용
queue = deque()
queue.append(5)
queue.popleft() //삭제
```

### 인접행렬과 인접리스트
인접 행렬은 메모리를 많이 차지하고
인접 리스트는 메모리는 적게 차지하지만 탐색이 오래걸린다
#### 인접행렬
``` python
INF = 987654321
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
```
### 인접리스트
``` python
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드(노드, 거리)
graph[1].append((1, 7))

# 노드 2에 연결된 노드(노드, 거리)
graph[2].append((0, 5))
```

### DFS
O(N)의 시간이 소요
``` python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

dfs(graph, 1, visited)
```

### BFS -> 최적해
O(N)의 시간이 소요
``` python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

bfs(graph, 1, visited)
```

## 2. 정렬
### 선택정렬
시간복잡도: O(N^2)
가장 작은 것을 선택한다
데이터 1,000개 정도까지 권장
``` python
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
```

### 삽입정렬
시간복잡도: O(N^2)
거의 정렬되어 있다면 O(N)
첫번째 데이터는 정렬되어 있다고 가정한다
``` python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
```

### 퀵 정렬
시간복잡도: O(NlogN)
이미 데이터가 정렬되어 있는 경우 O(N^2)

피벗pivot 사용
호어 분할
1. 첫 번째 데이터를 pivot으로 두고 오른쪽으로 전진하면서 큰 것, 왼쪽으로 전진하면서 작은 것을 교환한다
2. 엇갈리면 작은 데이터와 pivot을 교환한다
3. 각각의 파티션별로 1-2를 반복한다
``` python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quicksort(left_side) + [pivot] + quicksort(right_side)

print(quicksort(array))
```

### 계수Count 정렬
시간복잡도: O(N+K)
N: 데이터의 개수
K: 데이터의 최댓값
데이터의 크기 범위가 정수 형태로 제한되어 표현할 수 있을 때
중복값이 많을 때 유리하다 (ex) 성적
가장 큰 수와 작은 수의 데이터 차이가 100을 넘지 않을 때 사용하면 좋다
``` python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end='')
```

### 내장함수
시간복잡도: O(NlogN) -> 데이터 십만개일 때 유용
key로 정렬 가능
(ex) key = lambda student : student[1]
1. sorted() -> 리스트 자료형 리턴
2. sort() -> 리턴값 없고 내부 정렬
``` python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
result = sorted(student_tuples, key=lambda student: student[2])   # sort by age
print(result)
```

## 3. 이진 탐색 binary search

**전제:** 이미 정렬되어 있다

시작값, 중간값, 끝값이 있을 때

중간값이 찾는값보다 작을 때 오른쪽만 탐색하고,
                    클 때 왼쪽만 탐색한다

시간복잡도: 

### 재귀
``` python

```

### 반복문 (추천)
``` python

```

### 이진탐색트리
왼쪽 노드의 값 < 루트의 값 < 오른쪽 노드의 값

## 4. 다이나믹 프로그래밍 DP

## 5. 최단 경로

## 6. 그래프 이론