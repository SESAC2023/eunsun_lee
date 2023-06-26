import copy
import sys
input = sys.stdin.readline

a,b,c,d,e,f=map(int,input().split())

a1=copy.deepcopy(a)
b1=copy.deepcopy(b)
c1=copy.deepcopy(c)
d1=copy.deepcopy(d)
e1=copy.deepcopy(e)
f1=copy.deepcopy(f)

a=a*d
b=b*d
c=c*d
d=a1*d
e=e*a1
f=f*a1

if a!=0 or d!=0 :
    if a*d>=0 : #부호가 같으면 빼기
        y=(c-f)/(b-e)
        b=b*y
        x=(c-b)/a
    else : #a,d 서로 부호가 다르면 더하기
        y=(c+f)/(b+e)
        b=b*y  
        x=(c-b)/a

elif a==0 :
    y=c1/b1
    e1=e1*y
    x=(f1-e1)/d1
else :
    y=f1/e1
    b1=b1*y
    x=(c1-b1)/a1
    
    
print(int(x), int(y))
