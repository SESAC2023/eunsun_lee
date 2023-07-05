from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
q=deque()


for i in range(n) :
    a=input().strip()
    if a[0]=='p' and a[1]=='u':
        q.append(int(a[5:]))
    if a == 'pop' :
        if q==deque() :
            print(-1)
        else :            
            print(q[0])
            q.popleft()
    if a=='size' :
        print(len(q))
      
    if a =='empty' :
        if q==deque():
            print(1)
        else :
            print(0)
    if a =='front' :
        if q==deque():
            print(-1)
        else :
            print(q[0])
    if a =='back' :
        if q==deque():
            print(-1)
        else :
            print(q[-1])
