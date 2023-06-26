import sys
input = sys.stdin.readline

m=int(input())
n=int(input())

temp=[] #약수
x=[] #소수 리스트
s=0

for i in range(m, n+1):
    for j in range(1,i+1):
        if i%j==0 :
            temp.append(j)#약수
    if len(temp)==2 :
        s+=i
        x.append(i) #소수
    temp.clear()

if len(x)==0 :
    print(-1)
else :
    print(s)
    print(min(x))
