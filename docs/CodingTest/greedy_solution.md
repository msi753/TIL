# 1. 모험가 길드
```
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1  # 현재 그룹에 모험가 하나씩 포함시키기
    if count >= i:  # 모험가의 수가 공포도 이상이면
        result += 1 # 그룹의 수 증가
        count = 0   #초기화

print(result)
```
# 2. 곱하기 혹은 더하기
```
data = input()

result = data[0]

for i in range(1, len(data)) :
    num = int(data[i])
    //0 또는 1인 경우 더하기가 효율적
    if num <= 1 or result <= 1 :
        result += num
    else:
        result *= num

print(result)
```

# 3. 문자열 뒤집기
```
data = input()

count0 = 0
count1 = 0

if data[0] == '1' :
    count0 = 1
else :
    count1 = 1

for i in range(len(data)-1) :
    if data[i] != data[i+1] :
        if data[i+1] == '1':
            count0 += 1
        else :
            count1 += 1 
    
print(min(count0, count1))
```

# 4. 만들 수 없는 금액
```
n = input()
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data :
    if target < x :
        break
    target += x

print(target)
```

 # 5. 볼링공 고르기
 ```
 n, m = map(int, input().split())
 data = list(map(int, input().split()))

 array = [0] *11

 for i in data :
    array[i] += 1

 result = 0
 for i in range(1, m+1) :
    n -= array[i]
    result += array[i] * n

 print(result)
 ```