import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

b=[]
for i in range(5) :
    a=int(input())
    b.append(a)

print(int(sum(b)/len(b)))
b.sort()
print(b[2])
