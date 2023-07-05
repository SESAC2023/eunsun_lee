from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, k = map(int, input().split())
q=deque(range(1,n+1))


yo=[]

while q :
    for i in range(k-1) :
        q.append(q.popleft())
    x=q.popleft()
    yo.append(x)

print("<", end='')
for i in yo :
    if i == yo[-1] :
        print(i, end=">")
    else :
        print(i, end=', ')
