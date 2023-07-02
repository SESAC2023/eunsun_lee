import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())

time=list(map(int, input().split()))
time.sort()

s=0

a=[]
for i in time :
    s+=i
    a.append(s)

print(sum(a))
