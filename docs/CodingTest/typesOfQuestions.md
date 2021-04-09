# 문제 유형별 정리

## 1. 그리디
현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘
동전 거슬러 주기
``` python
n = 1260
count = 0

# 큰 단위의 화폐부터
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin

print(count)
```

## 2. 구현
피지컬로 승부하는 알고리즘
- 입력
    ```
    5               # 크기 N
    R R R U D D     # 이동 계획
    ```
- 출력
    ```
    3 4     # 도착 좌표
    ```

``` python
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
```

## 3. DFS/BFS

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

## 4. 정렬
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

## 5. 이진 탐색 binary search

**전제:** 이미 정렬되어 있다

시작값, 중간값, 끝값이 있을 때

중간값이 찾는값보다 작을 때 오른쪽만 탐색하고,
                    클 때 왼쪽만 탐색한다

시간복잡도: O(longN), 퀵 정렬과 비슷

### 재귀
``` python
result = binary_search(array, target, 0, n-1)

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
```

### 반복문 (추천)
``` python
result = binary_search(array, target, 0, n-1)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return None
```

### 이진탐색트리
왼쪽 노드의 값 < 루트의 값 < 오른쪽 노드의 값

## 6. 다이나믹 프로그래밍 DP

중복되는 연산을 줄이는 방법

- 언제 사용하나?
1. 큰 문제를 작은 문제로 나눌 수 있고(최적 부분 구조)
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일할 때(중복되는 부분 문제)

그리디도 아니고 구현도 아니고 완전탐색도 아닐 때

### 메모이제이션기법으로 피보나치 수열 구현하기

메모이제이션이란?

한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출해 메모한 결과를 그대로 가져오는 기법(캐싱)

퀵 정렬: 피봇값을 다시 처리하는 부문 문제는 존재하지 않는다.
다이내믹 프로그래밍: 한 번 해결했던 문제를 다시 해결한다.

시간복잠도: O(N)
``` python
# 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적이 있으면 그대로 리턴
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(6))
```

### 반복문을 이용한 bottom up 방식
스택 크기가 한정되어 있을 수 있기 때문에 탑다운보다 보텀업 권장
``` python
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
```

- sys 라이브러리의 setrecursionlimit() 함수를 호출해 재귀 제한을 완화할 수 있다.

## 7. 최단 경로

## 8. 그래프 이론