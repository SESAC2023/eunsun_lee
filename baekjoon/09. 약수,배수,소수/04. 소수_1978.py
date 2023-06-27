import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
temp=[]
s=0

for i in a :
    for j in range(1,i+1): #a의 원소들의 약수 구하기
        if i%j==0 :
            temp.append(j)
    if len(temp)==2 : #a의 원소 한개의 약수를 모두 구한 후 원소의 개수가 2개인 것만 s에 1더하기
            s+=1
    temp.clear() #a의 원소 하나가 끝날 때마다 clear 해주지 않으면 이전 원소에 누적됨

print(s)
