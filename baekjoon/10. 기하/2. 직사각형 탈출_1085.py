
import sys
input = sys.stdin.readline

x,y,w,h=map(int,input().split()) #x,y 는 한수의 위치 w,h는 직사각형의 크기
a=[]

if w/2<x :
    a.append(w-x)
else :
    a.append(x)

if h/2<y :
    a.append(h-y)
else :
    a.append(y)

#print(a)
print(min(a))
