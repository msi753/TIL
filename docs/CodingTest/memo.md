# 백준 단계별로 풀어보기 (나만의 팁)

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

