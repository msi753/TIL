
세 가지 언어로 공부하니까 문법이 너무 헷갈린다.

우선, 당장 필요한 언어만 선택해서 공부하자.

PHP: 회사에서 사용하는 언어, 내가 필요한 것은 게시판을 만드는 것 같은 기술인데, 문제를 풀면서 다양한 함수를 접해보고 싶어서 문제를 풀어보고 있다. 도움이 될지 안될진 모르겠지만 우선 해보고 판단하자.

PYTHON3: 코딩테스트에서 사용하는 언어

# 문제 요약

10진수를 2진수로 바꾸기

13은 1101 인데 연속되는 1의 개수는 2개이므로

2를 출력하는 문제

# PYTHON3
```
n = int(input())

cnt = 0
max = 0

while n > 0 :
    if n % 2 == 1 :
        cnt += 1
        if cnt>max : max = cnt
    else : cnt = 0  //연속적으로 1이 나오지 않으면 cnt를 0으로 초기화한다.
    n //= 2

print(max)
```

# PHP
```
<?php

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $n);

fclose($stdin);

$a = decbin($n);    //10진수에서 2진수로 바꿔주는 함수
$cnt = 0;
$mx = 0;

for ($i=0; $i<strlen($a); $i++) {
    if($a[$i]==1) {
        $cnt += 1;
        if($cnt>$mx) $mx = $cnt;
        continue;
    }
    $cnt = 0;
}

echo $mx;
```
