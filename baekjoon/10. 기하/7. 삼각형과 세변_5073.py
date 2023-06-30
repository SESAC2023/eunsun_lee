import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

while  True:
    a,b,c=map(int, input().split())
    if a==0 and b==0 and c==0 :
        break
    elif max([a,b,c])>=sum([a,b,c])-max([a,b,c]):
        print('Invalid')
    elif a==b and b==c :
        print('Equilateral')
    elif a==b or b==c or a==c :
        print('Isosceles')
    elif a!=b or b!=c or a!=c :
        print('Scalene')      
  
