PI = 3.141592
class Math:
    def solv(self, r):
        return PI * (r**2)  #r^2

    def sum(self, a, b):
        return a + b
    
if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))

# py
# import mod2 하면 __name__ == "__main__" 거짓으로 아무것도 실행되지 않는다.
# a = mod2.Math()
# a.solv(2) 또는
# mod2.solv(2) 처럼 사용한다
