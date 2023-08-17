import sys
sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline
tc = int(input())


def fac(n) :
    if n<=1 :
        return n
    else :
        return n*fac(n-1)

for i in range(tc) :
    m, n=map(int, input().split()) #nCm 조합 구하기
    if n == m :
        print(1)
    else :
        a = fac(n)//fac(n-m)
        b = a//fac(m)
        print(int(b))
