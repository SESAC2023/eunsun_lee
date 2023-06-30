import sys
import math
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())  

temp=[] #약수
x=[] #소수 리스트
s=0

for i in range(1, n//2):
    for j in range(1,i+1):
        if i%j==0 :
            temp.append(j)#약수
    if len(temp)==2 :
        s+=i
        x.append(i) #소수
    temp.clear()
  
#x.sort()
print(x)

d=[]

for i in x :
    while n%i == 0 :
        n=n//i
        d.append(i)
        
for i in d :
    print(i, end=' ')


"""import sys
input = sys.stdin.readline

n=int(input())
a=[i for i in range(2,n//2+1)]
b=[]
c=[]

while len(a) > 0:
    x = a[0]
    b.append(x)
    for i in reversed(range(0, len(a))):
        if a[i] % x == 0:
            a.pop(i)
print(b)
for i in b :
    while n%i!=1 :
        c.append(n%i)

print(c)"""
    
