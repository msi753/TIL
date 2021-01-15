# 준비방법

## 1. 공부 방법
- ~~코드업 200문제 풀기~~
- 백준 문제풀기
- 프로그래머스 문제 풀기

## 2. 온라인 개발환경
> https://repl.it/ 리플릿 <br>
> http://www.pythontutor.com/visualize.html#mode=edit 파이썬 튜터

### 2-1. vsc에서 디버깅 연습할 때
- input.txt
- main.py
```python
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline().rstrip
n, m = map(int, input().split())
print(n+m)
```
- launch.json
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            //"program": "${file}",
            "program": "main.py",
            "console": "internalConsole"
        }
    ]
}
```

## 3. 유형
구현> DFS/BFS> 그리디> 정렬> DP

## 4. 포트폴리오
프로젝트당 1~2장 정도의 분량으로 개발 과정 등을 문서화하고,
팀 프로젝트면 본인이 맡은 역할과 이슈를 해결하면서 배운 내용 등을 문서에 담아야 한다.<br>
AWS나 Google Cloud Platform(GCP)와 같은 클라우드 서비스를 이용해보면 좋다.


