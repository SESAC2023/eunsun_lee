import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def isprime(n) :
    m = 2*n
    a = [False,False] + [True]*(m-1) #0,1은 이미 false이므로 최초 true 값은 m-1개 필요
    primes=[] #소수
    for i in range(2, m+1):
        if a[i] : #a[i]가 true면 소수.
            for j in range(2*i, m+1, i): 
                a[j] = False #소수인 i의 배수들을 지우기.
            if i > n :
                primes.append(i)

    return len(primes)
  
while True :
    x=int(input())
    if x == 0 :
        break
    if x == 1 :
        print(1)
    else :
        print(isprime(x))
        
        
        """시간초과

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
