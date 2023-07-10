import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())

def f(x) :
    if x <=1 :
        return 1
    return x*f(x-1)

print(f(n))
