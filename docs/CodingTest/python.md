# 0. 탭키보다 띄어쓰기 4번을 습관 들이자

# 1. 자료형
> 수
- 1e9 는 10의 9제곱(10억)
- 987,654,321 로 표현하기도 한다
<br>
- round(123.456, 2) 의 결과는 123.46
<br>
- a//b 몫 구하기
- a**b x의 y제곱근
<br>
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
<br><b>반드시 이 방법으로 초기화해야 한다!</b>
<br>[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
- append()의 시간복잡도는 O(1)
- sort()의 시간복잡도는 O(NlogN)
- reverse(), insert(), count(), remove()의 시간복잡도는 O(N)
- 삭제는 [i  for i in a  if i <b>not in</b> remove_Set] 
<br>
> 튜플
- 변경 불가능
- (비용, 노드번호)
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

# 2. 조건문
- pass 나중에 작성할 소스코드
```
if score >= 80: result = "Success"
    else: result = "Fail"
```
```
result = "Success" if score >= 80 else "Fail"
```

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

lambdas = [lambda x:x+10, lambda x:x+100]
print(lambda[0](5))
print(lambda[1](5))
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

#Python3.6 이상 f-string
answer = 7
print(f"정답은 {answer}입니다.")
```
- 문자열 자료형끼리만 더하기 연산이 가능하다

# 6. 주요 라이브러리의 문법과 유의점
- 표준 라이브러리를 사용하자
<br> <a>https://docs.python.org/3.8/library/index.html</a>
<br>
> 1. 내장함수
```
sum([1, 2, 3, 4, 5])   #15
min(7, 3, 5, 2)     #2
max(7, 3, 5, 2)     #7
eval("(3+5)*7")     #56
sorted([9, 1, 8, 5, 4])     #[1, 4, 5, 8, 9]
sorted([9, 1, 8, 5, 4], reverse = True) #[9, 8, 5, 4, 1]

//튜플의 두 번째 원소(수)를 기준으로 내림차순으로 정렬
sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x:x[1], reverse=True)   #[('이순신', 75), ('아무개', 50), ('홍길동', 35)]

data = [9, 1, 8, 5, 4]
data.sort()     #[1, 4, 5, 8, 9]
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