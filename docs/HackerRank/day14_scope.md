# Scope

sample input

3

1 2 5

sample output

4

입력받은 숫자들 사이에서 절댓값을 구해서 가장 큰 수를 출력하는 문제인 줄 알았는데

입력값이 1보다 크고 100보다 작은 제한조건에 따라

제일 큰 값에서 제일 작은 값을 구하는 방식으로 문제를 풀었다.

# PHP
private $elements=array();  // private으로 선언되어있고

public $maximumDifference;  // public으로 선언되어 있어서... 

$maximumDifference변수에 계속 접근해 값을 바꿔준다
```
<?php
    class Difference{
    private $elements=array();
    public $maximumDifference;

    // Write your code here
    function __construct($arr) {
        $this->elements = $arr;
    }

    public function ComputeDifference() {
        $max = 1;    //문제에서 명시
        $min = 100;  //문제에서 명시
        foreach($this->elements as $num) {
            if ($num > $max) $max = $num;
            if ($num < $min) $min = $num;
        }
        $this->maximumDifference = $max - $min;
    }

} //End of Difference class  
     

$N=intval(fgets(STDIN));
$a =array_map('intval', explode(' ', fgets(STDIN)));
$d=new Difference($a);
$d->ComputeDifference();
print ($d->maximumDifference);
?>
```

# Python3
```
class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self) :
        mx = 1
        mn = 100
        for num in self.__elements :
            if num>mx : mx = num
            if num<mn : mn = num
        self.maximumDifference = mx - mn

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
```