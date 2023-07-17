import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

a, b = map(int, input().split())


def co_multiple(x,y) : #최대공약수로 최소공배수 구하는 함수 정의
    common = 1

    for i in range(2, int(min(x,y)+1)) :
        if x%i==0 and y%i==0:
             common = i # 최대공약수

    min_co_multiple = x*y/common  #최소공배수
  
    return int(common), int(min_co_multiple)
  

c = co_multiple(a, b)
for i in c :
    print(i)
