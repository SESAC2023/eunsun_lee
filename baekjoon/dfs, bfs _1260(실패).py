import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m, v=map(int, input().split())

list=[[] for i in range(n+1)]  #[[]]*(n+1)로 만들면 제대로 안 들어감.
visited=[False]*(n+1)
order=[0]*(n+1)

for i in range(5) :
    a,b=map(int, input().split())
  
    list[a].append(b) 
    list[b].append(a)  

for i in range(1,n+1) :
    list[i].sort()
ord_dfs=0

#dfs
def dfs(x) :
    global ord_dfs
    visited[x]=True
    ord_dfs +=1
    order[x] = ord_dfs
    for y in list[x] :
        if visited[y] is not True :
            dfs(y)   

dfs(v)
for i in order :
    if i==0 :
        pass
    else :
        print(i, end=" ")   
print()

order1=0

#bfs
visited=[False]*(n+1)
order=[0]*(n+1)

q=deque()
q.append(v)
visited[v]=True

while q :
    x=q.popleft()
    print(x, end=" ")
    visited[x]=True
    order1+=1
    order[x]=order1


    for y in list[x] :
        if  visited[y] is not True :
            visited[y] = True
            q.append(y)
