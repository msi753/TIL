# 문제 요약

2차원 배열

```
a b c
  d
e f g
```

모래시계 모양 중 합이 가장 큰 조합을 찾아 합을 구해라

입력 : 6 X 6

```
2 4 4 
  2 
1 2 4
```

# PHP
```
<?php

$stdin = fopen("php://stdin", "r");

$arr = array();

for ($i = 0; $i < 6; $i++) {
    fscanf($stdin, "%[^\n]", $arr_temp);
    $arr[] = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));
}

//preg_split 정규 표현식에 따라 문자열을 나눔, -1은 무제한을 의미
//PREG_SPLIT_NO_EMPTY 비어있지 않은 조각만을 반환

fclose($stdin);

$mx = -100;
for ($i=1; $i<count($arr)-1; $i++) {
    for ($j=1; $j<count($arr[0])-1; $j++) {
        $sum = $arr[$i-1][$j-1] + $arr[$i-1][$j] + $arr[$i-1][$j+1]
            + $arr[$i][$j]
            + $arr[$i+1][$j-1] + $arr[$i+1][$j] + $arr[$i+1][$j+1];
        if($sum>$mx) $mx = $sum;
    }
} 

echo $mx;

```

# Python3
```
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

# rstip()은 줄 바꿈 기호를 제거한다
# \기호로 들여쓰기를 무시하고? 사용 가능하다 
    mx = -100
    for i in range(1, len(arr)-1) :
        for j in range(1, len(arr[0])-1) :
            sm = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] \
                + arr[i][j] \
                + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if sm>mx : mx = sm
    
    print(mx)
```