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

        scanner.close();

        loops(n);
    }

    static void loops(int n) {
        for(int i=1; i<11; i++) {
            System.out.format("%d x %d = %d\n", n, i, n*i );
        }
    }
}
```

# PHP
큰 따옴표 안에 있으면 php를 해석해서 가져온다(변수의 값을 읽어온다)
```
<?php

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $n);

fclose($stdin);

for($i=1; $i<=10; $i++) {
    echo "$n x $i = " . ($n*$i) . "\n";
}
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

    for i in range(1,11):
        print('{0} x {1} = {2}'.format(n, i, n*i))

```