# 문제 유형별 정리

## 1. DFS/BFS

### 스택
``` python
stack = []  // 별도의 라이브러리를 사용할 필요가 없다
stack.append(1)
stack.pop()
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
