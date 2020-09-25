# JAVA8
```
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        for (int j=n-1; j>=0; j-- ) {     # 집중!!!
            System.out.print(arr[j]+" ");
        }

        scanner.close();
    }
}
```

# PHP
```
<?php

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $n);

fscanf($stdin, "%[^\n]", $arr_temp);

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));
#preg_split... 정규표현식 띄어쓰기 패턴 문자열을 기준으로, 무제한 횟수, preg_split()에 의해 나눈후 비어있지 않은 조각만을 반환합니다. 
#array_map... intval로 문자를 변환한 후 맵으로 만든다.

fclose($stdin);

echo implode(' ', array_reverse($arr));     # 집중!!!

```

# Python3
```
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr.reverse();     # 집중!!!
    print(" ".join(str(i) for i in arr))
```
