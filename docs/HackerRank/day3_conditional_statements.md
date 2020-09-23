# JAVA8

>에러
>>non-static method ... cannot be referenced from a static context

main 메서드가 static인 경우에는 class를 인스턴스화(객체화)하지 않고, <br>
class이름.method이름 이런 식으로 사용하는데

1. 객체를 생성해서 사용하거나
```
class Test {
    public static void main(String[] args) {
        new test().test1();
    }
    void test1() {
        System.out.println('a');
    }
}
```
2. 메서드에 static을 선언해서 사용한다
```
class Test {
    public static void main(String[] args) {
        test1();
    }
    static void test1() {
        System.out.println('a');
    }
}
```

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
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();

        System.out.println(isWeird(N) ? "Weird" : "Not Weird");
    }

    static boolean isWeird(int N) {
        if( N % 2 == 1) return true;    //홀수면 Weird
        if( N <= 5 ) return false;
        if( N <=20 ) return true;
        return false;
    }
}
```

# PHP
die()
```
<?php

$stdin = fopen("php://stdin", "r");
fscanf($stdin, "%d\n", $N);
fclose($stdin);

if( $N%2 == 1 ) die("Weird");
if( 2<=$N && $N<=5 ) die("Not Weird");
if( 6<=$N && $N<=20 ) die("Weird");
if( $N>20 ) die("Not Weird");
```

# Python3
```
#!/bin/python3

import math
import os
import random
import re
import sys

def isWeird(N):
    if(N%2==1): return True
    if(2<=N<=5): return False
    if(6<=N<=20): return True
    return False

if __name__ == '__main__':
    N = int(input())

    if(isWeird(N)) :
        print("Weird")
    else :
        print("Not Weird")
```
