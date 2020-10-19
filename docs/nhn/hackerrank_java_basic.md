# Day 0: Hello, World.
```
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in); 		
		// full line of input from stdin 읽어오고 변수에 저장하기
		String inputString = scan.nextLine();
		scan.close(); 
		System.out.println("Hello, World.");
        System.out.println(inputString);
	}
}

```
```
Hello, World. 
Welcome to 30 Days of Code!
```

# Day 1: Data Types
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
/*        
String nextLine(): Returns the next line of text, or, if you are in the middle of a line, returns the remainder of the line. Caution: If you are in the middle of a line, nextLine does not return the next line, but instead the remainder of the current line.
*/
        scan.nextLine();
        String ss = scan.nextLine();
        
        System.out.println(i+ii);

		System.out.println(d+dd);

        System.out.println(s+ss);

        scan.close();
    }
}
```
```
16
8.0
HackerRank is the best place to learn and practice coding!
```

# Day 2: Operators
```
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the solve function below. (여기!!!)
    static void solve(double meal_cost, int tip_percent, int tax_percent) {
        double tip = meal_cost * tip_percent/100;
        double tax = meal_cost * tax_percent/100;
        
        //Math.round()는 long타입을 리턴한다.
        long totalCost = Math.round(meal_cost + tip + tax);
        
        System.out.println(totalCost);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        double meal_cost = scanner.nextDouble();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tip_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tax_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        solve(meal_cost, tip_percent, tax_percent);

        scanner.close();
    }
}

```
```
12.00
20
8
```
```
15
```

# Day 3: Intro to Conditional Statements
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
```
3
```
```
Weird
```

# Day 4: Class vs. Instance
```
import java.io.*;
import java.util.*;

public class Person {
    private int age;	
  
	public Person(int initialAge) {
        if(initialAge<0) {
            System.out.println("Age is not valid, setting age to 0.");
            initialAge = 0;
        }
        this.age = initialAge;
	}

	public void amIOld() {
        if(this.age<13) {
            System.out.println("You are young.");
            return;
        }
        if(this.age>=13 && this.age<18) {
            System.out.println("You are a teenager.");
            return;
        }
        System.out.println("You are old.");
	}

	public void yearPasses() {
  		this.age++;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int age = sc.nextInt();
			Person p = new Person(age);
			p.amIOld();
			for (int j = 0; j < 3; j++) {
				p.yearPasses();
			}
			p.amIOld();
			System.out.println();
        }
		sc.close();
    }
}
```

# Day 5: Loops 구구단

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

# Day 6: Let's Review
```
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        while(n>0) {
            char[] chs = sc.nextLine().toCharArray();   //배열로 만들기
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
```
2
Hacker
Rank
```
```
Hce akr
Rn ak
```

# Day 7: Arrays

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

        for (int j=n-1; j>=0; j-- ) {
            System.out.print(arr[j]+" ");
        }

        scanner.close();
    }
}

```
```
split으로 쪼개고
Integer.parseInt()해서 배열에 담은 후
역순으로 출력하기
```

# Day 8: Dictionaries and Maps
```
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
```
HashMap은 Map interface를 implements 한 클래스로서 중복을 허용하지 않는다.
Map의 특징인 key와 value의 쌍으로 이루어지며, key 또는 value 값으로써 null을 허용한다.
put(key, value)으로 배열에 넣고, get(key)으로 가져온다.
containsKey(key)는 boolean 타입으로 키값 여부를 체크한다.
```

# Day 9: Recursion 3
```
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the factorial function below.
    static int factorial(int n) {
        if(n<=1) return 1;
        return n*factorial(n-1);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int result = factorial(n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

```
```
String.valueOf vs .toString vs (String) Casting

- valueOf : 파라미터가 null이면 문자열 null을 만들어서 담는다
- toString: null이면 NullPointerException 발생, Object에 담긴 값이 String이 아니어도 출력
- casting: null이면 NullPointerException, Object값이 String이 아니면 ClassCastException 발생

String str = null;
System.out.println((String) str);           //'null' text return
System.out.println(String.valueOf(str));    //'null' text return
System.out.println(str.toString());         //NullPointerException
```

# Day 10: Binary Numbers
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

        int cnt = 0;
        int max = 0;
        while(n>0) {
            if(n % 2 == 1) {
                cnt += 1;
                if(cnt > max) max = cnt;
            } else {
                cnt = 0;
            }
            n /= 2;
        }

        System.out.println(max);
    }
}

```
```
13을 2진수로 표현하면 1101인데, 연속적인 1의 숫자는 최대 2이다.
```

# Day 11: 2D Arrays
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
        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        scanner.close();

        int sum = 0;
        int max = -100;
        for(int n=1; n<5; n++) {
            for(int m=1; m<5; m++) {
                sum = arr[n-1][m-1] + arr[n-1][m] + arr[n-1][m+1]
                + arr[n][m] 
                + arr[n+1][m-1] + arr[n+1][m] + arr[n+1][m+1];
                if (sum>max) max = sum;
            }
        }
        System.out.println(max);
    }
}

```
```
max에서 왜 -100을 해주었냐면
input에 음수값이 있기 때문이다.
그래서 0이라고 초기화하지 않았던 것이다.

Integer 클래스의 메서드를 활용할 수 있다(Long, Short도 제공)
Integer.MAX_VALUE -> 2147483647
Integer.MIN_VALUE -> -2147483647
```

# Day 12: Inheritance
```
import java.util.*;

class Person {
	protected String firstName;
	protected String lastName;
	protected int idNumber;
	
	// Constructor
	Person(String firstName, String lastName, int identification){
		this.firstName = firstName;
		this.lastName = lastName;
		this.idNumber = identification;
	}
	
	// Print person data
	public void printPerson(){
		 System.out.println(
				"Name: " + lastName + ", " + firstName 
			+ 	"\nID: " + idNumber); 
	}
	 
}

class Student extends Person{
	private int[] testScores;

    /*	
    *   Class Constructor
    *   
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
    // Write your constructor here
    Student(String firstName, String lastName, int id, int[] scores) {
        super(firstName, lastName, id);
        this.testScores = scores;
    }
    /*	
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    // Write your method here
    public char calculate() {
        double avg = Arrays.stream(this.testScores).average().getAsDouble();
        if( avg >= 90 ) return 'O';
        if( avg >= 80 ) return 'E';
        if( avg >= 70 ) return 'A';
        if( avg >= 55 ) return 'P';
        if( avg >= 40 ) return 'D';
        return 'T';
    }
}

class Solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String firstName = scan.next();
		String lastName = scan.next();
		int id = scan.nextInt();
		int numScores = scan.nextInt();
		int[] testScores = new int[numScores];
		for(int i = 0; i < numScores; i++){
			testScores[i] = scan.nextInt();
		}
		scan.close();
		
		Student s = new Student(firstName, lastName, id, testScores);
		s.printPerson();
		System.out.println("Grade: " + s.calculate() );
	}
}
```

```
자바8 stream 스트림은 반복자
double avg = Arrays.stream(this.testScores).average().getAsDouble();

List<String> list = Arrays.asList("홍길동", "신용권", "김남준");
Stream<String> stream = list.stream();
stream.forEach(name -> System.out.println(name));

https://ict-nroo.tistory.com/43
```
