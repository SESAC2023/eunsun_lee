import sys
sys.setrecursionlimit(int(1e6)) #재귀 깊이 한도 해제
input = sys.stdin.readline

n, m, r=map(int, input().split()) #순서대로 노드 수, 간선 수, 시작 노드

array=[[] for i in range(n+1)] #노드수+1 만큼 2차 배열 만들기
visited=[0]*(n+1) #노드 방문처리를 위한 false 리스트 만들기
o=[0]*(n+1) #순서를 기록하기 위한 리스트

for i in range(m) : #간선 정보 입력
    u, v = map(int, input().split())
    array[u].append(v)
    array[v].append(u)

for i in range(1,n+1) : #문제에서 오름차순으로 방문하라고 했으므로 정렬해줘야 함.
    array[i].sort(reverse=True) 
  
order=0  

def dfs(x) :
    global order
    visited[x]=True #현재 노드 방문처리.
    order += 1
    o[x]=order
    
    for i in array[x] : # i번의 인접 노드 방문 여부 확인하기.
        if visited[i]==False :
            dfs(i)

dfs(r)
o.remove(o[0])
for i in o :
    print(i)


                
        
