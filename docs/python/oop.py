# 클래스, 모듈, 패키지, 예외 처리, 내장 함수, 외장 함수

# 1. 클래스
# 계산기 예제 (계산기마다 이전에 계산된 결과값을 기억하고 있어야 한다)
class Calculator:
    def __init__(self):
        self.result = 0
    
    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))    # 3
print(cal1.adder(4))    # 7
print(cal2.adder(3))    # 3
print(cal2.adder(7))    # 10

# self와 __init__
class Service:
    def sum(self, a, b):    # self는 인스턴스를 지칭한다. 클래스 내 함수의 첫 번째 인수는 무조건 self로 사용해야 인스턴스의 함수로 사용할 수 있다.
        result = a + b
        print("%s + %s = %s 입니다" % (a, b, result))

pey = Service()
print(pey.sum(1, 2))    # 1 + 2 = 3 입니다
#pey.sum(pey, 1, 2)와 동일한 결과

class NewService:
    secret = "역누는 배꼽이 두 개다"
    def __init__(self, name):   # init은 인스턴스를 만들 때 항상 실행된다. (생성자)
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다" % (self.name, a, b, result))

pey = NewService("홍길동")  # name을 넣지 않으면 TypeError: __init__() missing 1 required positional argument: 'name' 오류 발생
pey.sum(1, 2)

# 참고: 내장함수 type()은 객체의 타입을 출력한다

# 사칙연산 클래스 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def truediv(self):
        result = self.first / self.second
        return result                        

# 연산자 오버로딩: 연산자(+, -, *, /,,,)를 객체끼리 사용할 수 있게 하는 기법
class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다" % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))

class HouseKim(HousePark):  # 상속
    lastname = "김"
    def travel(self, where, day):   # 메서드 오버라이딩
        print("%s, %s여행 %d일 가다" % (self.fullname, where, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
juliet.travel("부산", 3)
pey.love(juliet)
print(pey + juliet) # __add__ 호출, 박응용, 김줄리엣 결혼했네
print(pey - juliet) # __sub__ 호출, 박응용, 김줄리엣 이혼했네