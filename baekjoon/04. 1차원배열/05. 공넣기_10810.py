import sys
input = sys.stdin.readline

n,m =map(int,input().split()) #n은 바구니 개수, m은 공을 넣을 회수
a=[0]*n

for x in range(m):
    i,j,k=map(int,input().split())
    for y in range(i-1, j):
        a[y]=k
     
for i in range(n):
    print(a[i], end=' ')
