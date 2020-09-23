# JAVA8
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

# PHP
```
<?php
class Person{
    public $age;
   public function __construct($initialAge){
        if( $initialAge < 0 ) {
            $initialAge = 0;
            echo "Age is not valid, setting age to 0.\n";
        }
        $this->age = $initialAge;
    }

   public  function amIOld(){
        if($this->age<13) {
            echo "You are young.\n";
            return;
        }
        if($this->age>=13 && $this->age<18) {
            echo "You are a teenager.\n";
            return;
        }
        echo "You are old.\n";
        return;

    }
   public  function yearPasses(){
        $this->age++;
    }
}

$T = intval(fgets(STDIN));
 for($i=0;$i<$T;$i++){
     $age=intval(fgets(STDIN));
     $p=new Person($age);
     $p->amIOld();
     for($j=0;$j<3;$j++){
         $p->yearPasses();
     }
     $p->amIOld();
     echo "\n";
         
 }
?>
```

# Python3

self를 사용하는구나!

```
class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            initialAge = 0
        self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
            return
        if 13 <= self.age and self.age < 18:
            print("You are a teenager.")
            return
        print("You are old.")
        return;
    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
```