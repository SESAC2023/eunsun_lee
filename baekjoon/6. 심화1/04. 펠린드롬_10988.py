import sys
input = sys.stdin.readline

n=input().strip()

if n==n[-1::-1]:
    print(1)
else :
    print(0)
