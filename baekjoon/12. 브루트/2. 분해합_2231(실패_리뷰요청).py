
import sys
input = sys.stdin.readline

n=int(input()) 

a=[] #각 분해 숫자를 리스트형식으로 저장 문자형식
b=[] #생성자 리스트
s=0 #분해합

for i in range(1, n+1) :
    a.append(list(str(i)))
    for j in a[i-1] : #분해숫자 리스트 호출
        for x in j : #분해숫자 하나씩 호출
            s=s+int(x)
        if s+i==n :
            b.append(i)
    s=0
if len(b)==0 : #생성자가 없으면 0출력
    print(0)
else :
    print(min(b))
