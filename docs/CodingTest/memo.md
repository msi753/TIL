# 백준 단계별로 풀어보기 (나만의 오답노트) 

그리디/구현/DFS/BFS/정렬/이진탐색/다이나믹프로그래밍/최단경로/그래프이론

+ 출력할 때 + 연산자로 묶으려면 str으로 형변환 해줘야 한다 print(str(n) + '' + str(i) + '=' + str(ni), end='\n')

+ count함수
```
a = int(input())    #150
b = int(input())    #266
c = int(input())    #427

numlist = list(str(a*b*c))
for i in range(10):
    print(numlist.count(str(i)))
```

+ 집합 자료형 set, 리스트의 중복을 제거하고 길이를 구한다
```
data = [1, 2, 3]
data = set(data)
print(len(data))
```

+ 문자열 리스트로 만들기
```
list(str(input()))
list(input())
```

+ ord의 활용
```
a는 97임을 활용해서 알파벳과 함께 사용
string ='abc'
for i in range(len(string)):
    alphabet = ord(string[i])-97    # 0부터 시작하는 배열로 표현 가능
```

+ 답안 제출 요령
```
PyPy3
import sys
input = sys.stdin.readline
n = input()
ord(n[0])   # 여기에서 오류가 발생했다 readline을 하면 \n까지 입력받기 때문이다
```
```
PyPy3
rstrip을 사용한다
import sys
input = sys.stdin.readline().rstrip
n = input()
```

+ for문이 끝난 후 줄바꿈을 하고 싶을 때 print('\n')을 하면 두 줄이 띄어진다. print('')가 이미 줄바꿈을 내포한다
```
for i in range(len(string)):
        print(string[i]*int(repeat), end='')
    print('')
```

+ 대문자로 변경하기
```
D = 'abc-def gh'

D.upper()
'ABC-DEF GH'

D.capitalize()
'Abc-def gh'

D.title()
'Abc-Def Gh'
```

+ replace 문자열 변경
```
s = 'abc'
if a in s:
    s = replace(a, '*')
print(s)    # *bc
```