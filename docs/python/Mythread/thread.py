import threading
import time

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python']:
    t = threading.Thread(target=say, args=(msg,))   # 함수 이름, 함수의 입력 변수
    t.daemon = True
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)


# 결과
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# you
# python
# need
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# need
# python
# you
# 18
# 19
# ...
# 99
