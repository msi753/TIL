# JAVA8
```
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        while(n>0) {
            char[] chs = sc.nextLine().toCharArray();
            for(int i=0; i<chs.length; i+=2) {            
                System.out.print(chs[i]);
            }
            System.out.print(" ");
            for(int j=1; j<chs.length; j+=2) {
                    System.out.print(chs[j]);
            }
            n--;
            System.out.println();
        }
    }   
}
```

# PHP
```
<?php
$_fp = fopen("php://stdin", "r");

fscanf($_fp, "%d\n", $n);

for($t=0; $t<$n; $t++) {
    fscanf($_fp, "%s\n", $str);
    for($i=0; $i<strlen($str); $i+=2) echo $str[$i];
    echo ' ';
    for($i=1; $i<strlen($str); $i+=2) echo $str[$i];
    echo "\n";
}

fclose($stdin);

```
> fscanf(), fgets()
- fscanf()
<br> 공백, 개행문자, 탭을 구분
<br> \n을 건너뛰고 바로 다음 줄을 읽어옴
- fgets() 
<br> 한줄
<br> fgetc(fp);로 \n을 건너뛰고 다음 줄로 이동해야함
```
abcdefgh
ijklmnopq
fscanf(fp,"%s",str[0]);    // 'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' '\0'
fgets(str[0],100,fp);      // '\n' '\0'
```

# Python3
```
n = int(input())
for i in range(n):
    S = input()
    length = len(S)
    for j in range(0, length, 2):
        print(S[j], end='')
    print(' ', end='')
    for j in range(1, length, 2):
        print(S[j], end='')
    print()
```

# 
- input 
```
2
Hacker
Rank
```
- output
```
Hce akr
Rn ak
```