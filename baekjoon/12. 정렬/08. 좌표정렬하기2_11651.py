import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
arr=[]
for i in range(n) :
    (a, b) = map(int, input().split())
    arr.append((b, a))

arr.sort()

for (x, y) in arr :
    print(y, x)
