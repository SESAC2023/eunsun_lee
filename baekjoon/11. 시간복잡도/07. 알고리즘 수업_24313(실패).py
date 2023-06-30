import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

#f(n) = a1n + a0
#O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
#f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력한다.
a1,a0 =map(int,input().split()) 
c=int(input())
n0=int(input())
n=100

temp=0
while n>=n0  :
    n-=1
    f=a1*n + a0
    g=n
    if a1*n+a0<=c*n:
        if temp==0 :
            temp+=1
        else : 
            continue
    else :
      
        break

print(temp)

if n==1 :
   print(a1*n+a0<=c*n)
        
    
