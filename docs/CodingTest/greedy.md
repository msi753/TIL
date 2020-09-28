# 그리디

거스름돈
```
n = 1260
count =0

coin_types=[500, 100, 50, 10]

for coin in coin_types:
    count += n//coin            #몫(코인당 동전의 개수)
    n %= coin

print(count)
```
<br>

큰 수의 법칙
```
n, m, k = map(int, input().split())
data = list(int, input().split())

data.sort()
first = data[n-1]
second = data[n-2]
/*
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
*/

count = int(m/(k+1))*k + m%(k+1)        #int(A/B)와 A//B는 같다

result = 0
result += (count)*first
result += (m-count)*second

print(result)

```
<br>

숫자 카드 게임
```
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    /*
    min_value = min(data)           # min()함수 이용
    */
    min_value = 10001               # 2중 반복문 이용
    for a in data:
        min_value = min(min_value, a)
    result = max(result), min_value
print(result)
```
<br>

1이 될 때까지
```
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
```