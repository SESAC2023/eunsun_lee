# 무방향 그래프(양방향 간선)
# 노드(정점)의 개수가 100,000개
# 간선(도로)의 개수가 200,000개
# BFS: 시간 복잡도 O(V+E)

import sys
from collections import deque
# 재귀 함수 깊이 해제
sys.setrecursionlimit(int(1e6))
# 입력이 10만 줄 이상일 때, 빠르게 입력 받기 위해 사용
input = sys.stdin.readline

# 노드의 개수(n), 간선의 개수(m), 시작 노드(r)
n, m, r = map(int, input().split())

# 인접 리스트
graph = [[] for i in range(n + 1)]
# 각 노드에 대한 방문 여부
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    # 양방향 간선이기 때문에
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort() # 오름차순 방문
                    #여기까진 dfs와 동일

# 시작할 때
q = deque()  # 큐를 생성
q.append(r)  # 큐에 시작 노드 넣기
visited[r] = True  # 시작 노드 방문 처리

answer = [0] * (n + 1)  # 각 노드를 방문한 순서
order = 1

# 큐가 빌 때까지 반복
while q:           # 빈칸 즉 0은 false 이므로 원소를 모두 빼서 빈 큐가 되면 while문 종료.
    # 매번 큐에서 원소 꺼내기. 선입선출이므로 왼쪽에서부터 빼야 함.
    x = q.popleft()
    answer[x] = order  # 순서 기입
    order += 1
    # 인접한 노드 확인하기
    for y in graph[x]: 
        # 방문하지 않았다면 방문처리하고 인접노드를 큐에 모두 삽입. for 문으로 인해 모든 원소가 들어가게 됨.
        if not visited[y]:
            visited[y] = True
            q.append(y)          #방문 안 한 인접노드 모두 삽입. 인접노드가 모드 방문처리 됐다면 삽입없이 꺼내기만 수행->바로 다음으로 반목.

for i in range(1, n + 1):
    print(answer[i])bsb
