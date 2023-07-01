import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, k=map(int, input().split())
b=[]
c=[]
for i in range(n) :
    a=int(input())
    b.append(a)
b.sort(reverse=True)
for i in b :
    c.append(k//i)
    k=k%i
  
print(sum(c))
