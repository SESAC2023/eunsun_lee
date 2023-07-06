from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n , m= map(int, input().split())
l=list(map(int, input().split())) #뽑을 숫자
num=deque(range(1,n+1)) #처음의 순서
cnt=0   #연산 횟수
#print(num.index(2))

for i in l :

    while i in num :
        if num[0]==i :
            num.popleft()
        elif len(num)//2 < num.index(i) :
            num.appendleft(num.pop())
            cnt+=1
        else :
            num.append(num.popleft())
            cnt+=1
print(cnt)
