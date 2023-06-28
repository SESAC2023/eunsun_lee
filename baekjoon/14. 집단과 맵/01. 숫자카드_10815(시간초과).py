"""시간초과 

import sys
input = sys.stdin.readline

n=int(input())  #보유 수량 최대 50만장
a=input().split() #카드에 적힌 정수 -천만~천만

m=int(input())  # 비교군 카드 수량, 최대 50만장
b=input().split() #비교군 카드에 적힌 정수, -천만~천만

x=[0 for i in range(m)] #비교군 카드의 소유 확인

s=0

for i in b : #최대 50만번
    s+=1
    if i in a :
        x[s-1]=1  

for i in x :  #최대 50만번 
    print(i, end=' ')"""

"""
    시간초과2
    import sys
input = sys.stdin.readline

n=int(input())  #보유 수량 최대 50만장
a=set(map(int, input().split())) #카드에 적힌 정수 -천만~천만

m=int(input())  # 비교군 카드 수량, 최대 50만장
b=set(map(int, input().split())) #비교군 카드에 적힌 정수, -천만~천만

x=[0 for i in range(m)] #비교군 카드의 소유 확인

c=list(b&a)) #있는 카드 리스트
b=list(b)
for i  in c :
    
    x[b.index(i)]=1
  
for i in x :  #최대 50만번 
    print(i, end=' ')


    """
