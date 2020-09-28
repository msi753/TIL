# JAVA8
```
//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        HashMap<String, Integer> phoneBook = new HashMap<String, Integer>();

        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();
            phoneBook.put(name, phone);
        }
        while(in.hasNext()){
            String s = in.next();
            if(!phoneBook.containsKey(s)) {
                System.out.println("Not found");
                continue;
            }
            System.out.println(s+"="+phoneBook.get(s));
        }
        in.close();
    }
}
```

# PHP
```
<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */

$n = rtrim(fgets($_fp));

$phoneBook = [];
for($i=0; $i<$n; $i++) {
    list($k, $v) = explode(' ', rtrim(fgets($_fp)));
    $phoneBook[$k] = $v;
}

while($k=rtrim(fgets($_fp))) {
    if(!array_key_exists($k, $phoneBook)) {
        echo "Not found\n";
        continue;
    }
    echo $k.'='.$phoneBook[$k]."\n";
}
?>
```

# Python3
try except 구문
```
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}
for _ in range(n) :
    name, phoneNumber = input().split()
    phoneBook[name] = phoneNumber
while True:
    # exception이 발생하면 실행되지 않습니다!
    try:
        query = input()
    # exception이 발생하면 실행됩니다!
    except :
        break
    if query in phoneBook :
        print(query + "=" + phoneBook[query])
    else :
        print("Not found")
```