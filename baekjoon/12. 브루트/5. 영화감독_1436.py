import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

num=1
cnt=0

while True :
    num+=1
    if '666' in str(num) :
        cnt+=1

        if cnt==n :
            break

print(num)
  
