
import sys
input = sys.stdin.readline
n, m=map(int, input().split()) #n은 바닥에 깔린 카드 수, m은 기준 숫자
card=list(map(int, input().split()))

s=0
a=[]

for i in card:
    for x in card :
        if i!=x :
            for y in card :
                if i!=y and x!=y :
                    s=i+x+y
                    if s<=m : 
                        a.append(s)
                        s=0

print(max(a))
