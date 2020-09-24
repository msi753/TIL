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
