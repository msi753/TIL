# 1. 소수의 판별
<b>2보다 큰</b> 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 수
```
//시간복잡도 O(X)
def is_prime_number(x) :
    for i in range(x) :
        if x % i == 0 :
            return False    # 나누어 떨어지면 소수가 아님
        return True         # 소수임

print(is_prime_number(4))
```

```
//시간복잡도 O(X^1/2) -> 가운데 약수를 기준으로 대칭이므로 제곱근까지만 확인하면 됨
import math
def is_prime_number(x) :
    for i in range(2, int(math.sqrt(x))+1) :
        if x % i == 0 :
            return False    # 나누어 떨어지면 소수가 아님
        return True         # 소수임

print(is_prime_number(4))
```

```
//에라토스테네스의 체   -> 시간복잡도 O(NloglogN), 공간복잡도 O(N)
import math

n = 1000
array = [True for i in range(n+1)]      # 소수로 초기화(True)

for i in range(2, int(math.sqrt(n))+1) :
    if array[i] == True :   # 남은 수인 경우
        j = 2               # 배수 지우기
        while i*j <= n :
            array[i*j] = False
            j += 1

for i in range(2, n+1) :    # 모든 소수 출력
    if array[i] :
        print(i, end='')
```

# 2. 투 포인터
리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리
<br> 특정한 합을 가지는 부분 연속 수열 찾기
```
n = 5   # 데이터의 개수
m = 5   # 부분합
data = [1, 2, 3, 4, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n) :                     # start를 증가시키면서
    while interval_sum < m and end < n :    # 부분합보다 작으면 end포인터 증가
        interval_sum += data[end]
        end += 1
        if interval_sum = m:                # 부분합에 도달하면 count 증가
            count += 1
        interval_sum -= data[start]         # 부분합보다 크면 start포인터가 가리키는 값 제거

print(count)
```

정렬되어 있는 두 리스트의 합집합 -> O(N+M)
<br> 병합정렬Merge Sort과 같은 일부 알고리즘에서 사용되고 있다
```
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n+m)
i = 0
j = 0 
k = 0

while i < n or j < m :
    # 리스트 A의 값을 넣는 경우 (리스트 B의 모든 원소가 처리되었거나 리스트 A의 원소가 더 작을 때)
    if j >= m or (i < n and a[i] <= b[j]) :
        result[k] = a[i]
        i += 1
    else :
        result[k] = b[j]
        j += 1
    k += 1

for i in result :
    print(i, end=' ')
```