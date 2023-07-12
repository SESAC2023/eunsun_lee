import sys
import math
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m = map(int, input().split())

a = [False,False] + [True]*(m-1) #0,1은 이미 false이므로 최초 true 값은 m-1개 필요
primes=[] #소수
for i in range(2, m+1):
    if a[i]: #a[i]가 true면 소수.
        primes.append(i)
        for j in range(2*i, m+1, i): 
            a[j] = False #소수인 i의 배수들을 지우기.
for i in primes :
    if i >=n :
        print(i)
