# JAVA8
```
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);

        int ii = scan.nextInt();
        double dd = scan.nextDouble();

        //스캐너에 개행문제 \r\n이 남아서 비워줘야 한다.
        //If you are in the middle of a line, nextLine does not return the next line, but instead the remainder of the current line.
        scan.nextLine();

        String ss = scan.nextLine();
        
        System.out.println(i+ii);
		System.out.println(d+dd);
        System.out.println(s+ss);

        scan.close();
    }
}
```

# PHP
```
<?php
    $handle = fopen ("php://stdin","r");
    $i = 4;
    $d = 4.0;
    $s = "HackerRank ";

    $ii = intval(fgets($handle));
    $dd = floatval(fgets($handle));
    $ss = fgets($handle);

    echo $i+$ii."\n";
    echo number_format($d+$dd, 1)."\n";
    echo $s.$ss;
    fclose($handle);
?>
```

# Python3
```
    i = 4
    d = 4.0
    s = 'HackerRank '

    ii=int(input())
    dd=float(input())
    ss=input()

    print(i+ii)
    print(d+dd)
    print(s+ss)
```