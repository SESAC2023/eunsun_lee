import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

a, b = map(int, input().split())


def co_multiple(x,y) : #최대공약수로 최소공배수 구하는 함수 정의
    common = 1

    for i in range(2, int(min(x,y)+1)) :
        if x%i==0 and y%i==0:
             common = i

    min_co_multiple = x*y/common
  
    return int(min_co_multiple)
  

print(co_multiple(a, b))
