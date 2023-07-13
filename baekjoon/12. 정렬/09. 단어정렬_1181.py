import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
arr=[]
for i in range(n) :
    a=input().strip()
    b=len(a)
    arr.append((b,a))
arr=set(arr)
arr=sorted(arr, key = lambda x: (x[0], x[1]))

for x, y in arr :
    print(y)
