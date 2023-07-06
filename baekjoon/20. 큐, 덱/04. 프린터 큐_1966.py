from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
q=deque()
an=[] #중요도 출력
an1=[] #출력된 문서 번호. 순서 기록을 위한 것.
for i in range(n):
    an=[] #중요도 출력
    an1=[]
    a, b =map(int, input().split())
    q=deque(map(int, input().split())) #문서의 중요도 리스트
    num=deque(range(0,a)) #문서 번호 리스트

    while q : #q가 빌때까지 반복
        if q[0] == max(q) : #가장 앞에 문서가 중요도가 가장 높으면 출력. 아니면 맨 뒤로 보내기. 동시에 문서번호도 똑같이 수행.
            an.append(q.popleft())
            an1.append(num.popleft())
                
        else :
            q.append(q.popleft())
            num.append(num.popleft())
    print(an1.index(b)+1)
