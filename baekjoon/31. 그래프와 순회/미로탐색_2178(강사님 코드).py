import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n, m = map(int, input().split())
graph = []

# DFS와 BFS의 기본 요소: graph, visited (방문 처리 배열)
# 최단 거리 문제에서는 1개가 더 필요: distance (최단 거리 배열)

visited = [[False] * m for i in range(n)]  # 값이 모두 0인 n*m의 2차배열을 만들기
distance = [[0] * m for i in range(n)]      # 값이 모두 0인 n*m의 2차배열을 만들기

for i in range(n): # 한줄씩 입력 받기
    line = input().strip()
    current = [] #문자정보를 정수 정보로 바꾸기 위한 작업. 아래 for문을 통해 정수의 2차배열 만들기
    for x in line:
        current.append(int(x))
    graph.append(current)

# print(graph)

# BFS 수행
q = deque()  # 큐 생성
q.append((0, 0))  # 출발 노드 넣기
visited[0][0] = True
distance[0][0] = 1

# 상, 좌, 하, 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:  # 큐가 빌 때까지 반복
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 맵을 벗어난다면 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 벽이라면 무시
        if graph[nx][ny] == 0:
            continue
        # 방문한 적 없다면, 방문 처리 및 거리 기록
        if not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))
            # 이전 위치에서 다음 위치로 넘어가므로 1칸 거리 추가
            distance[nx][ny] = distance[x][y] + 1

print(distance[n - 1][m - 1])
