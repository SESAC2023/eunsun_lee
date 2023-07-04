from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

k = int(input())
array=[]

for i in range(k) :
    a = int(input())
    if a ==0 :
        array.pop()
    else :
        array.append(a)

print(sum(array))
