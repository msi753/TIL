nhn 지원에 자소서는 필요하지 않았다.

그래서 지원하게 되었고

pre-test1차는 코딩 테스트 전형이다.

코딩 테스트는 파이썬으로 준비하는 게 유리하다고 해서 파이썬을 공부하고 있었는데...

모든 기업이 파이썬을 허용하지 않는다는 사실을 간과하고 있었다.

지원하는 언어는 c, c++, java가 있다.

자바는 입출력이 까다롭기 때문에 입출력 과정을 가져다 쓸 수 있도록 정리해두자.

우선, 코드업 100제를 풀었던 내용을 회고해보자.

# 자바

## 1. 간단한 입출력
```
int a = sc.nextInt();                       // int 변수 1개 입력받는 예제
double b = sc.nextDouble();                 // double 변수 1개 입력받는 예제 ex) 1.0
String var = sc.next();                     // 문자열 1개 입력받는 예제
long AB = sc.nextLong();                    // long 변수 1개 입력받는 예제   ex) 12345678901234567L

//charAt
char c = sc.next().charAt(0);               // 문자 1개를 입력받는 예제

String stringName = 'coding everybody';
System.out.printf(stringName.charAt(0)); 					// c
System.out.printf(stringName.charAt(stringName.length-1));	// y
System.out.printf(stringName.charAt(1000) == ''); 			// true

//charCodeAt 유니코드값을 리턴
var stringName = '생활코딩'
alert(stringName.charCodeAt(0)); // 493373



int a = 0;     
int b = 1;       
System.out.printf("%d %d", a, b);          	// int 변수 1개 출력하는 예제
// int는 4byte -> 32bit -> 2^32 
// -이십억 ~ +이십억 까지 표현 가능하다.	<- 이 경우는 int 처리
// unsigned는 40억까지					  <- 이 경우는 long 처리
long AB = 12345678901234567L;
System.out.println(AB);		       			// long 변수 1개 출력하는 예제

double c = 1.123;
System.out.printf("%.2f", c); 		       	// double 변수를 소수점 이하 세번째 자리에서 반올림하여 소수점 이하 둘째 자리까지 출력	ex) 1.12

char g = 'b';
System.out.printf("%c", g);		       		// char 변수 1개 출력하는 예제
System.out.print((int)g);					// char문자(유니코드)에 해당하는 숫자 출력, A의 경우 65
System.out.print((char)65);					// A

String var1 = "ABCDEFG";
String var2 = "HIJ";
System.out.printf("%s%s", var1, var2);		// 문자열 2개 출력하는 예제

```

### 1-1. Scanner 사용법
```
import java.util.Scanner;

class Solution {
	public static void main(String args[]) throws Exception {
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
		
		}
        sc.close();
	}
}

```

### 1-2. 이스케이핑
```
'작은따옴표'와 "큰따옴표"와 백슬래시\를 이스케이핑하려면
\' \" \\ 와 같이 써야한다.

public class Main{
    public static void main(String args[]) {
        System.out.printf("\"C:\\Download\\hello.cpp\"");
    }
}
```

## 2. 문자열 자르기

### 2-1. split과 System.out.format, join

입력: 년, 월, 일이 ".(닷)"으로 구분되어 입력된다.

출력: 입력받은 년, 월, 일을 출력한다. 단, 자릿수는 yyyy.mm.dd형태로 출력한다.

(입출력 예시 참고, %02d를 사용하면 2칸을 사용해 출력하는데, 1자리 수인 경우 앞에 0이 붙어 출력된다.)

```
split은 정규표현식을 사용하는데 . 은 임의의 한문자를 나타내는 정규식이다. (정규표현식을 사용한다는 것은 문자열에 규칙이 있다는 말이다.)
따라서 모든 문자가 토큰이 되고 배열에 남는 게 없게 된다.
String 안에 이스케이프 문자인 \를 쓰려면 \\라고 써야하기 때문에 \\.이 된다.
또는 [] 대괄호 안에 넣어주면 된다. ex) [.], [|], \\^ (특수문자를 구분자로 사용하는 경우)


import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a;
		a = sc.next();
		sc.close();
		String[] time = a.split("\\.");
		//split은 아마 object를 리턴하나보다
		System.out.format("%04d.%02d.%02d", Integer.parseInt(time[0]), Integer.parseInt(time[1]), Integer.parseInt(time[2]));
	}
}

String phone = "010-323-2928";
String strPhone = String.join("", phone.split("-"));
//strPhone = phone.replace("-", "");	위와 동일
System.out.println(strPhone);
```

### 2-2.  substring
```
begin index는 0, end index는 자르려는 글자 끝 index + 1

String str = "ABCDEFGHIJKLMN";
String getStr1 = str.substring(0, 3);	// ABC
String getStr2 = str.substring(5);		// FGHIJKLMN
```

> Scanner로 한 줄 입력 받은 후(nextLine), Token으로 끊어서 출력하기 (split과 비슷하다)
(st.nextToken()은 Object타입을 리턴하기 때문에 Integer.parseInt(st.nextToken())으로 형변환한다.)
(next로 입력 받으면 띄어쓰기나 개행문자 모두를 경계로 값을 인식)
```
//StringTokenizer
//hasMoreTokens
//nextToken

import java.util.Scanner;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.nextLine();
		StringTokenizer st = new StringTokenizer(a, ".");
		int[] times = new int[3];

		int i=0;
		while(st.hasMoreTokens()) {
			times[i] = Integer.parseInt(st.nextInt());
			i++;
		}
		System.out.print(times[1]);
	} 
}
```

## 3. 버퍼

데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 임시 메모리 영역

입출력 속도를 향상시키기 위해 사용
물을 나르는데 컵을 쓰느냐, 양동이를 쓰느냐의 차이

### 3-1. 버퍼를 이용한 입력: BufferedReader
```
import java.io.*;
 
class BufferedReaderEx1 {
    public static void main(String[] args){
        try{ //예외처리 필수! 또는 throwsIOException해주기
            //콘솔에서 입력 받을 경우
			//InputStreamReader는 '바이트 스트림'을 지정된 문자 '인코딩'에 따라 '문자 스트림'으로 변환하는 데 사용한다.
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
 
            //파일에서 입력받을 경우
            FileReader fr = new FileReader("BufferedReaderEx1.java");
            BufferedReader br_f = new BufferedReader(fr);
            
            //String이 리턴값이라 형변환 필수! 라인단위임
            int num = Integer.parseInt(br.readLine());             
            br.close(); //입출력이 끝난 후 닫아주기
            
            //파일의 한 줄 한 줄 읽어서 출력한다.
            String line ="";
            for(int i=1; (line = br_f.readLine()) != null; i++){	//line을 입력받아서 null이 아닐때까지(즉, 값이 있을 때까지)
                System.out.println(line);
            }
        } catch (IOException e){ //
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}

```

### 3-2. 버퍼를 이용한 출력: BufferdWriter
```
import java.io.*;
 
class BufferedWriterEx1 {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter("bufferedWriter.txt"));
        bw.write("hello\n"); //출력
        bw.newLine(); //개행 즉 엔터 역할
        bw.write("I am writing\n"); //개행과 함께 출력
        bw.flush(); //남아 있는 데이터를 모두 출력(버퍼스트림은 버퍼가 꽉 찼을 때만 출력되는 특징이 있기 때문)
        bw.close(); //스트림 
    }
}
```
```
import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));        
        String n = br.readLine();
        br.close();
        
        StringTokenizer st = new StringTokenizer(n);
        int r = Integer.parseInt(st.nextToken());
        int g = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        
        BufferedWriter bf = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int c=0;
        for(int i=0; i<r; i++) {
            for(int j=0; j<g; j++) {
                for(int k=0; k<b; k++) {
                    String s = i+" "+j+" "+k;
                    bf.write(s+"\n");
                    bf.flush();
                    c++;
                }
            }
        }
        System.out.print(c);
        //bf.write(Integer.toString(r*g*b));
        //bf.close();
	}
}

```

Scanner는 띄어쓰기(스페이스)와 엔터(개행문자)를 경계로 값을 인식하기 때문에 가공할 필요가 없어서 사용하기 매우 편리하다

BufferedReader는 엔터만 경계로 인식하고 받은 데이터가 String으로 고정되기 때문에 데이터를 따로 가공해야 하는 경우가 많다

## 4. toCharArray()로 배열을 만들고, new String으로 문자열 만들기
```
public class Test {
	public static void main(String[] args) {
		String str = "helloworld";
		
		char[] arr = str.toCharArray();
		for(int i=0; i<arr.length; i++) {
			System.out.print(arr[i] + " ");		//h e l l o w o r l d
		}

		String newStr = new String(arr);
		System.out.println(newStr);				//helloworld
	}
}
```

## 5. int long, double float

int 4바이트 '기본형' 20억까지 정수	Integer.parseInt()

long 8바이트 정수	Long.parseLong()

double 8바이트 '기본형' 실수

float 4바이트 실수		%.0f -> 정수처럼 출력됨

> String.format() 원하는 형식으로 출력
```
String.format("%X", i);	// %X는 대문자, %x는 소문자

//%X는 정수를 대문자 16진법으로 표시(소문자는 %x), \n은 줄바꿈
System.out.format("%X*%X=%X\n", b, i, b*i);
```

## 6. length, length(), size() 의 차이

length: 배열의 길이

length(): 문자열의 길이

size(): 컬렉션프레임워크 타입의 길이

## 7. 비트단위(bitwise) 연산자

~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), 
<<(bitwise left shift), >>(bitwise right shift)

- 시프트

	32비트를 넘어가는 비트는 삭제된다.
	```
	<<: 2배 증가	ex) a<<b, a*2^b
	>>: 2배 감소
	```
- xor: 서로 다를 때 1(참)

## 8. 삼항 연산자
```
System.out.println(a>b?a:b);
System.out.println((a<b?a:b)<c?(a<b?a:b):c);	//a, b, c 의 값 중 가장 큰 값
```

## 9. 반복문
### 9-1. switch

switch( ) 에 주어지는 값은 “정수"값만 가능하며,
문자도 아스키코드 정수값이기 때문에 가능하다.
```
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        sc.close();
        
        switch(a) {
            case 3:case 4:case 5:
                System.out.print("spring");
                break;
            case 6:case 7:case 8:
                System.out.print("summer");
                break;
            case 9:case 10:case 11:
                System.out.print("fall");
                break;
            case 12:case 1:case 2:
                System.out.print("winter");
                break;
        }
	}
}
```

### 9-2. do while 로 알파벳 출력하기
``` java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        
        char word = sc.next().charAt(0);
        
        //영문 a~z까지의 아스키코드값은
        //대문자 65~90
        //소문자 97~122
        char start = 'a';
        
        do {
            System.out.print(start+" ");
            start += 1;
        } while(start<=word);
	}
}
```

### 9-3. 반복문 continue 사용하기

3의 배수는 통과 시켜라
``` java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        
        for(int i=1; i<a+1; i++) {
            if(i%3==0) {
                //3의 배수일 때 아래 부분은 건너뛰고 계속
                continue;   
            }
            System.out.println(i);
        }
        
	}
}
```
## 10. 에제
### 10-1. 바둑알 십자 뒤집기 (+)
``` java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] arr = new int[19][19];
		
		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		int n = sc.nextInt();
		int x, y;
		
		for (int i = 0; i < n; i++) {
			x = sc.nextInt();
			
			for (int a = 0; a < 19; a++) {
				if (arr[x-1][a] == 0) {
					arr[x-1][a] = 1;
				} else {
					arr[x-1][a] = 0;
				}
			}
			
			y = sc.nextInt();
			
			for (int b = 0; b < 19; b++) {
				if (arr[b][y-1] == 0) {
					arr[b][y-1] = 1;
				} else {
					arr[b][y-1] = 0;
				}
			}
		} // end for()
		
		
		for (int[] a : arr) {
			for(int b : a) {
				System.out.print(b + " ");
			}
			System.out.println();
		}
	} // end main()
}	// end Main

```

### 10-2. 설탕과자 뽑기
``` java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        

        //가로 세로 길이를 입력받는다
        String[] hw = br.readLine().split(" ");
        //height=5 / width=5
        int height = Integer.parseInt(hw[0]);
        int width = Integer.parseInt(hw[1]);
        
        //입력값의 정의역
        if (height > 0 && height <= 100 &&
                width > 0 && width <= 100) {
            
            //[5][5] 크기의 배열을 만든다
            String[][] arr = new String[height][width];
            
            //막대의 개수를 입력받는다.
            int n = Integer.parseInt(br.readLine());
            
            if (n >= 1 && n <=10) {
                
                for (int i = 0; i < n; i++) {
                    //막대의 정보를 String배열에 입력받는다
                    //막대의길이 (length) 방향(d) 0이면 가로로 1이면 세로로
                    //좌표 (x) (y)
                    String[] stick = br.readLine().split(" ");
                    
                    int length = Integer.parseInt(stick[0]);
                    int d = Integer.parseInt(stick[1]);
                    int x = Integer.parseInt(stick[2])-1;
                    int y = Integer.parseInt(stick[3])-1;
                    
                    //2 0 1 1로 예를 들면
                    if (d == 0) { //막대 방향이 가로일때
                        for (int j = y; j < y + length; j++) {
                            //int j=0; j<2; j++
                            if (j < width) {
                                //[0][0] 과 [0][1]에 1을 넣어준다
                                arr[x][j] = "1";
                            }                               
                        }
                    //3 1 2 3으로 예를 들면
                    }else{ //막대 방향이 세로일때
                        for (int j = x; j < x + length; j++) {
                            //int j=1; j<4; j++
                            if (j < height) {
                                //[1][2],[2][2],[3][2]에 1을 넣어준다
                                arr[j][y] = "1";
                            }                               
                        }
                    }
                }
                
                //전체 출력 for문
                for (int i = 0; i < arr.length; i++) {
                    for (int j = 0; j < arr[i].length; j++) {
                        if (arr[i][j] == null) {//위에 해당되는 값이 없어서 null이면
                            arr[i][j] = "0"; //0을 넣어준다
                        }
                        System.out.print(arr[i][j] + " ");
                    }
                    System.out.println();
                }
            }else{
                System.out.println("1 >= stick num <= 10");
            }
        }else{
            System.out.println("1 >= width & height <= 100");
        }
        
    }
}
```

### 10-3. 성실한 개미
``` java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.Scanner;
public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[][] arr = new String[10][10];
        
        //10*10크기의 미로 상자 구조와 먹이 위치를 입력받는다
        for (int i = 0; i < 10; i++) {
            String[] arr_n = br.readLine().split(" ");
            for(int j=0; j<10; j++) {
                arr[i][j] = arr_n[j];
            }
        }
        
        /*
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[10][10];
        for(int i=0; i<10; i++) {
            for(int j=0; j<10; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        */
        
//행을 고정하고 열j(flag)을 움직이다가 2를 만나면 종료 플래그를 만나서 아예 종료시키고,
//행을 고정하고 열j(flag)을 움직이다가 1을 만나면 열j(flag)을 1 감소시키고 종료시킨 후, 행을 증가시킨다.
        int end = 0; //종료
        int flag = 1; //y값
        for(int i=1; i<arr.length; i++) {
            if(end!=1) {
                for(int j=flag; j<arr.length; j++) {
                    if(arr[i][j].equals("0")) {
                        arr[i][j] = "9";
                    } else if(arr[i][j].equals("2")) {
                        arr[i][j] = "9";
                        end = 1;
                        break;
                    } else {
                        flag = j-1;
                        break;
                    }
                }
            } else {
                break;
            }
        }
            
        //전체 출력 for문
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

    }
}
```