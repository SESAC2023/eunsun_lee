import sys
input = sys.stdin.readline


n=int(input())
d=dict()

for i in range(n) :
    a, b = input().split()
    a=a.strip()
    b=b.strip()
    d[a]=b

r=[]
for k, v in d.items() :
    if  v=="enter" :
        r.append(k)
r.sort(reverse=True) 

for i in r :
    print(i)



