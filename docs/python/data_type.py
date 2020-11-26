# 문자열
# 문자열 슬라이싱
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:13]
print(yyyymmdd) #연월일
print(num)      #숫자
# 문자열 인덱싱
pin = "881120-1068234"
print(pin[7])

#리스트
#정렬
a=[1,3,5,4,2]
a.sort()    #[1, 2, 3, 4, 5]
a.reverse() #[5, 4, 3, 2, 1]
print(a)
#리스트에서 문자열으로
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)   #Life is too short

#튜플 (값을 변경할 수 없으며, 새로운 튜플이 생성되고 그 값이 변수a에 대입된다.)
a = (1, 2, 3)
a = a + (4,)    # 단일 요소 튜플의 경우 후행 쉼표가 필요합니다.
print(a)    #(1, 2, 3, 4)

#딕셔너리
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) # B를 추출한 후 딕셔너리 {'A': 90, 'C': 70}
print(result) # B에 해당되는 값 80

#집합(리스트자료형이 집합자료형으로 바뀌면서 중복된 값을 제거한다)
a = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)    #[1, 2, 3, 4, 5]

# sample.txt를 읽고 총합과 평균값을 구한 후, 평균값을 result.txt파일에 쓰는 프로그램
f = open('sample.txt')
lines = f.readlines()   #sample.txt를 줄단위로 모두 읽는다.
f.close()

total = 0
for line in lines:
    score = int(line)   # 줄에 적힌 점수를 숫자형으로 변환한다.
    total += score

average = total / len(lines)

f = open('./result.txt', 'w')
f.write(str(average))
f.close()
