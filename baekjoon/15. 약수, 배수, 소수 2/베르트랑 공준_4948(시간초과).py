"""시간초과//에스토스테테스의 체로 다시 시도하기

import sys
import math
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def prime(x) :
    temp=[] #약수
    p = [] #소수 리스트
    y = 2*x
    for i in range(x+1, y+1):
      for j in range(1, math.squr(i)+1):
          if i%j==0 :
              temp.append(j)#약수
      if len(temp)==1 :
          p.append(i) #소수
      temp.clear()
    
    return len(p)    


while True :
    n=int(input())
    if n == 0 :
        break
    else :
        print(prime(n))
"""
