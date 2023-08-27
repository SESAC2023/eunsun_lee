from collections import deque

#      0  1   2   3   4  5  6  7
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

test_cases = int(input())  # 테스트 케이스의 수
for tc in range(test_cases):
    n = int(input())  # 체스판의 길이
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    # N X N 크기의 체스판 방문 체크 배열 만들기
    visited = [[False] * n for _ in range(n)]
    # N X N 각 위치까지의 최단 거리 배열 만들기
    distance = [[-1] * n for _ in range(n)]

    # start 위치에서 BFS를 수행해서 최단 거리 계산
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True  # 방문 처리
    distance[start_x][start_y] = 0  # 시작 지점 거리

    # BFS 수행
    while q: # 큐가 빌 때까지 반복
        x, y = q.popleft()
        # 찾으면 break하도록 해서 시간 초과 방지
        if x == end_x and y == end_y:
            break
        for i in range(8): # 다음 위치(인접 위치) 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny]: # 처음 방문한다면
                visited[nx][ny] = True # 방문 처리
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    print(distance[end_x][end_y])
