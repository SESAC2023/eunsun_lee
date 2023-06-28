from string import ascii_uppercase
import math
import sys
input = sys.stdin.readline


n=int(input()) #입력 회수
x=[[] for i in range(n)]
y=[]
for i in range(n) :
    a,b=input().split()
    a=int(a)
    b=b.strip()
  
    for j in b:
        x[i].append(j*a)
for i in range(n) :
    for j in x[i]:
        print(j, end='')
    print()
