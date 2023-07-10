from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())

def f(x) :
    if x == 0 :
        return 0
    if x == 1 :
        return 1
    return f(x-1)+f(x-2)

print(f(n))
