from collections import deque
import sys
sys.setrecursionlimit(int(1e6)) #재귀 깊이 한도 해제
input = sys.stdin.readline

n, m, r = map(int, input().split())

array=[[] for i in range(n+1)] #노드수+1 만큼 2차 배열 만들기
visited=[0]*(n+1) #노드 방문처리를 위한 false 리스트 만들기

for i in range(m) : #간선 정보 입력
    u, v = map(int, input().split())
    array[u].append(v)
    array[v].append(u)
  
for i in range(n):
    array[i].sort()
  
def dfs(x) :
    visited[x]=True #현재 노드 방문처리.
    print(x, end=' ')
    for i in array[x] : # i번의 인접 노드 방문 여부 확인하기.
        if visited[i]==False :
            dfs(i)

dfs(r)
print()


#bfs
visited=[0]*(n+1) #노드 방문처리를 위한 false 리스트 초기화

q=deque()
q.append(r)
visited[r]=True

while q :
    x=q.popleft()
    print(x, end=' ')
    for i in array[x] :
        if visited[i]==False :
            visited[i]=True
            q.append(i)
