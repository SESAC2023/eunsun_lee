import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
b=[]
for i in range(n) :
    a=int(input())
    b.append(a)
 
b.sort()
for i in b :
    print(i)
