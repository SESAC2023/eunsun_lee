import sys
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

print(c)
    
