import sys
input = sys.stdin.readline

a=[]
b=[]

for i in range(30) :
    a.append(i+1)
for i in range(28) :
    n=int(input())
    b.append(n)

a=set(a)
b=set(b)
c=a-b
d=list(c)

print(min(c))
print(max(c))
