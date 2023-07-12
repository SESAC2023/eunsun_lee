import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def isprime(n) :
    a = [False,False] + [True]*(n-1) #0,1은 이미 false이므로 최초 true 값은 m-1개 필요
    primes=[] #소수
    cnt = 0
    for i in range(2, n+1):
        if a[i] : #a[i]가 true면 소수.
            primes.append(i)
            for j in range(2*i, n+1, i): 
                a[j] = False #소수인 i의 배수들을 지우기.              
 #   for x in primes :
        if a[n-i] and a[i] :
            a[i] = False
            cnt += 1
            
    return cnt

tc = int(input())

for i in range(tc) :
    y = int(input())
    print(isprime(y))
