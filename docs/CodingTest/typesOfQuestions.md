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
- 유형
    + 다익스트라 최단 경로 알고리즘
    + 플로이드 워셜 알고리즘
    + 벨만 포드 알고리즘

### 다익스트라 최단 알고리즘 Dijkstra
'특정한 노드'에서 출발하여 '다른 노드'로 가는 경우 사용

주로 GPS 소프트웨어의 기본 알고리즘으로 채택됨

'그리디' 알고리즘으로 분류된다(방문하지 않은 노드 중에서 현재 최단 거리가 가장 짧은 노드를 확인하기 때문이다)

int(1e9)는 10억, 무한을 표현할 때 사용

987654321으로도 대체 가능

한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것

> 바로 아래의 예시는 간단한 다익스트라 알고리즘으로 시간 복잡도는 O(V^2)이다
``` python
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한

# 노드와 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    def get_smallest_node():
        min_value = INF
        index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        # 시작 노드에 대해서 초기화
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        for i in range(n-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
            now = get_smallest_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```

> 개선된 다익스트라 알고리즘, 시간복잡도 O(ElogV), 힙heap 자료구조 사용(현재 가장 가까운 노드를 저장하기 위한 목적)

- heapq
<br>우선순위 큐
<br> 최소힙, O(NlongN), 최상단 원소는 '가장 작은' 원소
```
import heapq

def heapsort(iterable) :
    h = []
    result = []
    for value in iterable :
        heapq.heappush(h, value)    //최대힙 heapq.heappush(h, -value)
    for value in range(len(h)) :
        result.append(heapq.heappop(h))  //최대힙 result.append(-heapq.heappop(h))
    return result       //여기까지 O(logN)... 트리구조

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) //여기까지 O(NlogN)
print(result)   //[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_val = one+two
    result += sum_val
    heapq.heappush(heap, sum_val)
```

``` python

```

## 8. 그래프 이론