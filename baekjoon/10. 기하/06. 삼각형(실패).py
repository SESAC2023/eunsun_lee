import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

an=[]
s=0
for i in range(3):
    a=int(input())
    an.append(a)
    s+=a

if s==180 :
    if an[0]==60 and an[1]==60:
        print('Equilateral')
    elif an[0]==an[1] or an[0]==an[2] or an[1]==an[2] :
        print('Isosceles')
    else :
        print('Scalene')

else :
    print('Error')
