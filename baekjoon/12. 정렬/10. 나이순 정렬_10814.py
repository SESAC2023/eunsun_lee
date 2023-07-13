import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
arr=[]
for i in range(n) :
    a, b=input().split()
    arr.append((i+1, int(a), b)) #가입순서, 나이, 이름

arr=sorted(arr, key = lambda x: (x[1],x[0]))

for x, y, z in arr :
    print(y, z)
