import sys
import math
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())  #도착지

#6으로 나눈 몫은 등차수열의 합. 해당 등차수열의 개수 또는 마지막 수가 최단 거리

tem=[]
s=0
for i in range(1,n//5) :
    s+=i
    tem.append(s)
tem1=[]
for i in tem :
    if i<=n//6 :
       tem1.append(i)
    if i>n//6:
        break

max_v=max(tem1)
c=(-1+math.sqrt(1+8*max_v))/2
print(int(c))
      
  
