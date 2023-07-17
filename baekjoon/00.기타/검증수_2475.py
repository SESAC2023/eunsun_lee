import sys
sys.setrecursionlimit(int(1e6))


arr = list(map(int, input().split()))

s = 0
for i in arr :
    s += i**2
print(int(s%10))
