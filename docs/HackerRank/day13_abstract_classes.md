# 추상 클래스

상속받는 모든 클래스에서는 이 추상 메소드를 반드시 재정의해야 합니다.

# PHP
```
<? php
abstract class Book
{
    
    protected $title;
    protected  $author;
    
     function __construct($t,$a){
        $this->title=$t;
        $this->author=$a;
    }
    abstract protected function display();
}

//Write MyBook class
class MyBook extends Book {
    protected $price;
    function __construct($title,$author,$price) {
        parent::__construct(trim($title), trim($author));   // fgets는 \n을 포함해서 한 줄을 가져오기 때문에 trim해준다.
        $this->price = $price;
    }

    function display() {
        echo 'Title: ' . $this->title . "\n"; 
        echo 'Author: ' . $this->author . "\n";
        echo 'Price: ' . $this->price . "\n";
    }
}


$title=fgets(STDIN);
$author=fgets(STDIN);
$price=intval(fgets(STDIN));
$novel=new MyBook($title,$author,$price);
$novel->display();

?>
```

# Python3
```
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book) :
    def __init__(self, title, author, price) :
        super().__init__(title, author)
        self.price = price
    def display(self) :
        print('Title:', self.title)     # print에 ,를 쓰면 공백이 포함되어 있다. -> Title: The Alchemist
        print('Author:', self.author)
        print('Price:', self.price)


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
```