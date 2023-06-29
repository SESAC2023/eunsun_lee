#묶음을 구하는 것이므로 dfs로 푸나 bfs로 푸나 답은 같을 것.

from collections import deque
import sys
sys.setrecursionlimit(int(1e6)) #재귀 깊이 한도 해제
input = sys.stdin.readline

n=int(input()) # 노드 수
m=int(input()) # 간선 수


array=[[] for i in range(n+1)] #노드수+1 만큼 2차 배열 만들기
visited=[0]*(n+1) #노드 방문처리를 위한 false 리스트 만들기
o=[0]*(n+1) #순서를 기록하기 위한 리스트

for i in range(m) : #간선 정보 입력
    u, v = map(int, input().split())
    array[u].append(v)
    array[v].append(u)
  
q=deque()  # 큐 생성
q.append(1) #시작 노드 큐에 넣기
visited[1]=True #방문처리
order=1


while q : #0이 false이므로 q가 빈때 false 값을 출력하므로 while 종료됨
    x = q.popleft()
    o[x]=order
    order+=1  #순서입력 이후에 순서를 올려야 함. 예를 들어 첫번째 노느가 1번일 경우 
              #1번에 순서 1을 넣어야 하는데, 1을 더한 것을 먼저 넣게 되면 1에 2가 들어가게 됨.

    for i in array[x] :
        if visited[i] ==False :
            visited[i] = True
            q.append(i)
a=[]
for i in o :
  if i!=0 :
      a.append(i)

print(len(a)-1)
