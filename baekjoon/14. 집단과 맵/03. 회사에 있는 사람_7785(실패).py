import sys
input = sys.stdin.readline


n=int(input())
d=dict()

for i in range(n) :
    a, b = input().split()
    d[a]=b

for k, v in d.items() :
    if  v=="enter" :
        print(k)
