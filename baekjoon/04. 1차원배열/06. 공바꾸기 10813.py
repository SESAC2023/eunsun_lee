import sys
input = sys.stdin.readline

n,m =map(int,input().split()) #n은 바구니 개수, m은 공을 바꿀 횟수
a=[]

for i in range(n) :
    a.append(i+1)

for x in range(m):
    i,j=map(int,input().split())
    a[i-1],a[j-1]=a[j-1],a[i-1]
     
for i in range(n):
    print(a[i], end=' ')
