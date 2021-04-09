# 0. 탭키보다 띄어쓰기 4번을 습관 들이자
# 0. python(pypy)이 초과되면 pypy(python)로 제출한다.
# 0. 1초에 2000만번의 연산을 처리할 수 있다고 가정하고 문제를 푼다.
시간 제한이 1초이고, 데이터의 개수가 100만 개인 문제가 있다면 일반적으로 시간 복잡도 O(NlogN) 이내의 알고리즘을 이용하여 문제를 풀어야 한다.
- argument, 인자, 함수를 호출할 때 넣는 값
- parameter, 매개변수, 함수 내부적으로 전달받고자 하는 값
<br>

# 0. 입력의 개수가 정해지지 않았을 때 입력 받는 방법
+ EOF
+ try/except
```
# input.txt
1 1
2 3
3 4
9 8
5 2
```
```
# main.py
import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
for line in sys.stdin
    print(line)                     # 1 1\n
    print(line.split())             # ['1', '1']
    n, m = map(int, line.split())   # 1 1
    print(n+m)                      #2
```
```
제출 답변 1 (정석)
import sys
for line in sys.stdin
    print(line)     
    print(line.split())
    n, m = map(int, line.split())
    print(n+m)
```
```
제출 답변 2
import sys
input = sys.stdin.readline
while True:
    try:
        n, m = map(int, input().split())
        print(n+m)
    except:
        break
```
```
제출 답변 3
while True:
    try:
        n, m = map(int, input().split())
        print(n+m)
    except:
        break
```
# 1. 자료형
> 수
- 1e9 는 10의 9제곱(10억)
- 987,654,321 로 표현하기도 한다
- round(123.456, 2) 의 결과는 123.46
    + round()는 끝자리가 0이면 출력하지 않는다. ex) round(3.1015, 2) -> 3.1
    + math는 정수를 리턴
    ``` python
    import math
    math.ceil(3.1015)   # 4
    ```
- a//b 몫 구하기
- a**b x의 y제곱근
<br>
> 지수
- 1e^9 는 10^9 (10,000,000,000) 십억
- 최단경로 알고리즘에서 도달할 수 없는 노드에 대한 최단거리를 무한으로 둘 때 사용
- int(ie^9)를 해야 정수형으로 사용 가능
- round(123.456, 2) -> 123.46

> 리스트
- 내부적으로 연결리스트 자료구조
- 빈 리스트 선언 방법, a = list(), a = []
- 크기가 n이고, 모든 값이 0인 1차원 리스트 초기화, a = [0] * n
- 인덱싱과 슬라이싱
```
a = [1, 2, 3, 4]
print(a[-1])    #4
print(a[-3])    #2
print(a[1:4])   #[2, 3, 4]
                #0부터 시작하고 1을 뺀 값의 인덱스까지 처리
```
- 리스트 컴프리헨션 [i for i in range(20) if i %2 == 1]
<br>[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
- 2차원 리스트 [[0] * 4 for _in range(3)]
- 0이 아닐 때, [[] for _ in range(n)]
<br><b>반드시 이 방법으로 초기화해야 한다!</b>
<br>[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
- append()의 시간복잡도는 O(1)
- sort()의 시간복잡도는 O(NlogN)
- reverse(), insert(), count(), remove()의 시간복잡도는 O(N)
- 삭제는 [i  for i in a  if i <b>not in</b> remove_Set] 
<br>
> 문자열
- +로 연결
- 특정 인덱스의 값 변경 <b>불가능</b>
```
a = "String"
print(a*3)  #StringStringString
```

> 튜플
- 변경 불가능
- (비용, 노드번호)
- 최단경로 알고리즘
<br>
> 사전자료형
- 해시테이블 O(1) 리스트보다 빠르다
```
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
key_list = data.keys()
value_list = data.values()
for key in key_list:
    print(data[key])
```

> 집합자료형 Set
- 중복X, 순서X
- O(1), 특정한 데이터가 이미 등장한 적이 있는지 여부
- 초기화, set([1, 2, 3]), {1, 2, 3}
- | 합집합, & 교집합, - 차집합
- add(), update(), remove()

> array[::] 용법 (Extended Slices)
- arr[A:B:C], index A 부터 index B 까지 C의 간격으로 배열을 만들어라

arr = range(10)
<br>

arr
<br> [0,1,2,3,4,5,6,7,8,9]

arr[::2] # 처음부터 끝까지 두 칸 간격으로
<br> [0,2,4,6,8] 

arr[1::2] # index 1 부터 끝까지 두 칸 간격으로 
<br> [1,3,5,7,9] 

arr[::-1] # 처음부터 끝까지 -1칸 간격으로 (역순으로) 
<br> [9,8,7,6,5,4,3,2,1,0] 

arr[::-2] # 처음부터 끝까지 -2칸 간격으로 (역순, 두 칸 간격으로) 
<br> [9,7,5,3,1] 

arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 (역순으로) 
<br> [3,2,1,0] 

arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로 
<br> [1,3,5]

# 2. 조건문
- pass 나중에 작성할 소스코드
```
if score >= 80: result = "Success"
    else: result = "Fail"
```
```
result = "Success" if score >= 80 else "Fail"   #한줄에 쓸 땐 if문이 가운데
```
- if ~ elif ~ else

# 3. 반복문
- range(시작값, 끝값+1) 
- 1~9, range(1, 10)
- for i in range(5)하면 0부터 시작되며, 리스트나 튜플에서 사용

# 4. 함수
> 람다 표현식 Lambda Express
- print((lambda a, b: a + b)(3, 7))
```
add = lambda x, y : x + y
print(add(3, 4))
```
```
lambdas = [lambda x:x+10, lambda x:x+100]
print(lambda[0](5))
print(lambda[1](5))
```
```
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b : a+b, list1, list2)
print(list(result))     #[7, 9, 11, 13, 15]
```

# 5. 입출력
- input() 한 줄의 문자열
- 공백 list(map(int, input().split()))일 때,
<br> input()으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼 후에
<br> map을 이용하여 해당 리스트의 모든 원소에 int()함수를 적용하고, 그 결과를 list()로 다시 바꾼다
- 줄바꿈 int(input())
- n, m, k = map(int, input().split())
<br>
```
import sys
data = sys.stdin.readline().rstrip()
print(data)
```
- readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데,
<br> 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 한다.
- print()는 줄바꿈 포함
```
answer = 7
print("정답은 "+str(answer)+"입니다")
print("정답은", str(answer), "입니다")  #공백이 들어간다
```
- Python3.6 이상 f-string
``` python
answer = 7
print(f"정답은 {answer}입니다.")

rate = count/data[0]*100
print(f'{rate:.3f}')   # 40.000
```
- 문자열 자료형끼리만 더하기 연산이 가능하다
- , 는 띄어쓰기 포함
- end는 print(줄바꿈 포함)의 줄바꿈 대신 사용

- format()
``` python
format(3.141592, ".2f") # 3.14
print("{0:.0f}".format(2.34))   # 2 (정수만 출력)
print("{:.0f}".format(3.01))    # {0} 이라고 표시하면 format함수 안의 첫번째 값을 넣으라는 뜻, 0은 생략 가능
```
# 6. 주요 라이브러리의 문법과 유의점
- 표준 라이브러리를 사용하자
<br> <a>https://docs.python.org/3.8/library/index.html</a>

> 1. 내장함수
``` python
sum([1, 2, 3, 4, 5])   #15

data = list(map(int, input().split(' ')))
sum(data[1:])   # 0번째 말고 1번째부터 끝까지의 합

min(7, 3, 5, 2)     #2
max(7, 3, 5, 2)     #7
eval("(3+5)*7")     #56

# sorted(list)와 list.sort()의 차이

# 1. sorted(iterable[, key=<function>][, reverse=<True|False>])
# 리턴값은 정렬된 새로운 리스트(원본에 영향X)
sorted([9, 1, 8, 5, 4])     #[1, 4, 5, 8, 9]
sorted([9, 1, 8, 5, 4], reverse = True) #[9, 8, 5, 4, 1]
# 튜플의 두 번째 원소(수)를 기준으로 내림차순으로 정렬
sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x:x[1], reverse=True)   #[('이순신', 75), ('아무개', 50), ('홍길동', 35)]

# 2. list.sort([reverse=<True|False>][, key=<function>])
# 리턴값은 None, 원본에 영향O
data = [9, 1, 8, 5, 4]
data.sort()     #[1, 4, 5, 8, 9]

office = [(1, 2), (3, 4), (5, 6)]
office.sort(key = lambda x: (x[1], x[0]))
```

> 2. itertools

- 순열 permutations: n개에서 r개를 선택하여 일렬로 나열
<br>
nPr = n!/(n-r)!
<br>
클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용 

```
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
#[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```
```
import itertools
data = [1, 2]
for x in itertools.permutations(data, 2)
    print(list(x))
#[1, 2]
#[2, 1]
```

- 조합 combination: 순서를 고려하지 않는 경우
```
from itertools import combinations
data = ['A', 'B', 'C']
list(combinations(data, 2))
#[('A', 'B'), ('A', 'C'), ('B', 'C') ]
```

- product: permutations와 비슷하지만 원소 중복
```
from itertools import product
data = [A, B, C]
result = list(prodect(data, repeat=2))  # 2개 뽑기
print(result)
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

- combinations_with_replacement: combinations와 비슷하지만 원소 중복
```
from itertools import combinations_with_replacement
data=['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))   # 2개 뽑기
print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```

> 3. heapq

<br> 다익스트라 최단 경로 알고리즘
<br> 우선순위 큐
<br> 최소힙, O(NlongN), 최상단 원소는 '가장 작은' 원소
```
import heapq

def heapsort(iterable) :
    h = []
    result = []
    for value in iterable :
        heapq.heappush(h, value)
    for value in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_val = one+two
    result += sum_val
    heapq.heappush(heap, sum_val)
```

> 4. bisect
``` python
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left, value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
```