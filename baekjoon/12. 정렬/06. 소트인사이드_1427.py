import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=list(input().strip())
n.sort(reverse=True)

for i in n :
    print(i,end="")
