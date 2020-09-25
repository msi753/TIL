# 체육복
중복되는 번호가 없으므로 set를 쓸 수 있다. <br>
여분의 체육복이 있지만 도난을 받지 않은 (체육복을 빌려줄)세트<br>
체육복이 도난당했지만 여분이 있지 않은 (체육복을 빌릴)세트<br>
set의 remove는 O(1)<br>

```
def solution(n, lost, reserve):
    
    set_reserve = set(reserve) - set(lost)      //[r for r in reserve if r not in lost]
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    return n - len(set_lost)
```

# 구명보트
최대 2명이 탑승가능하고 <br>
가장 무거운 사람과 가장 가벼운 사람을 탑승시키고, <br>
limit 보다 추가되면 무거운 사람만 탑승시킨다.
```
def solution(people, limit):
    people.sort()
    j = len(people)-1
    i = 0
    cnt = 0
    while i<=j:
        cnt += 1
        if people[i]+people[j] <= limit:
            i += 1
        j -= 1
    return cnt
```
# 큰 수 만들기
