def sum(a, b):
    return a + b

# D:\TIL\docs\python\module     으로 이동
# py    대화형 인터프리터 실행 명령
# import mod1   현재 디렉터리에 있는 파일, 모듈만 불러올 수 있다
# print(mod1.sum(3, 4))     #7

# from mod1 import sum  하면
# sum(3,4)  처럼 호출 할 수 있다.

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다")
        return 
    else:
        result = sum(a, b)
        return result

if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(10, 10.4)

# python mod1.py (직접파일 실행)일 때는 __name__ == "__main__"이 참으로 오류가 발생하지 않지만
# import mod1 (대화형 인터프리터나 모듈 불러오기)하면 __name__ == "__main__" 거짓으로 if문 다음 문장들이 수행되지 않음
