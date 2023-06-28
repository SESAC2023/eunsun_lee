from string import ascii_uppercase
import math
import sys
input = sys.stdin.readline


a,b=map(list,(map(reversed, input().split())))

x=[]
y=[]
for i in range(3) :
    if a[i]==b[i] :
        pass
    elif a[i]>b[i] :
        x.append(a)
    else :
        x.append(b)

for i in x[0]:
    print(i,end="")
   
