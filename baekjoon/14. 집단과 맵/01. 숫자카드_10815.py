import sys
input = sys.stdin.readline

#크로아티아 알파벳 리스트 만들기

n=int(input())
a=list(map(int, input().split()))

m=int(input())
b=list(map(int, input().split()))
x=[0 for i in range(m)]

s=0
for i in b :
    s+=1
    if i in a :
        x[s-1]=1

for i in x:
    print(x, end=' ')
