"""58점짜리"""
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
line=list(map(int, input().split()))
price=list(map(int, input().split()))

s=0

min_v = min(price)

#if min_v == price[-1]:
#      price.pop()

while price : #최소값 이후로는 모드 최저가로 주유. 최소값포함 오른쪽을 모두 삭제한 후 반복
    min_v = min(price)
    min_ind = price.index(min_v)
    distance = sum(line[min_ind:]) #최소값 이후의 거리의 합. 
    
    s += min_v * distance
    del line[min_ind :]
    del price[min_ind :]
  
print(s)


"""17점짜리

import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
line=list(map(int, input().split()))
price=list(map(int, input().split()))


s=0

for i in price[1:] :

    x=price[0]

 #다음 작은수 전까지 현재 가격으로 계산.
    if i <x:           
        s += x * sum(line[0 : (price.index(i))])
        del line[0 : price.index(i)]
        del price[0 : price.index(i)]

    elif i == x: #따로 계산하지 않으면 인덱스는 가장 작은 값을 추출하므로 계속 0이 되어 아무것도 삭제되지 않음.           
        s += x * sum(line[0 : price.index(i)+1])
        del line[0 : price.index(i)+1]
        del price[0 : price.index(i)+1]
        
    #print(x, s, price, line)
        
   
print(s)
"""
