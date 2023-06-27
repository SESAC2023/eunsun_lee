"""
<24479>
1) 내용 훑기: 그래프, DFS, 방문 처리, 탐색
2) (중요) 입력 조건:
  - 노드(도시) 혹은 정점 개수 최대 100,000개
  - 간선(도로) 개수 최대 200,000개
(3) 문제 아이디어 생각하기
  - DFS로 풀면 되지 않을까?
    - DFS의 시간 복잡도가 O(N + M)이니까, 단순 DFS 돌리면 시간 초과 X
(4) 코드 작성
"""

import sys
# 재귀 깊이 한도 해제
sys.setrecursionlimit(int(1e6))
# 빠른 입력받기
input = sys.stdin.readline

# 정점 개수(N), 간선 개수(M), 시작 노드(R)
n, m, r = map(int, input().split())

graph = [[] for i in range(n + 1)] #2차배열
"""
graph = [
    [],
    [],
    ...
    []
]
"""

for i in range(m): #간선의 개수만큼 반복
    u, v = map(int, input().split())
    graph[u].append(v)#그래프의 u번째 인덱스(리스트임)에 v를 넣고 
    graph[v].append(u)#v번째 인덱스(리스트)에 u를 넣음. 양방향이기 떄문에 둘 다 해주는 거고 한방향이면 아래꺼는 필요 없음.
"""
graph = [
    [],
    [4, 2],
    [1, 3, 4],
    [2, 4],
    [1, 2, 3],
    []
]
"""

for i in range(1, n + 1): #노드만큼 반복
    graph[i].sort() #문제에 정렬하라고 했으므로 정렬해줌. 그래프의 i번째 인덱스를 정렬함. 각각 정렬 됨 
"""
graph = [
    [],
    [2, 4],
    [1, 3, 4],
    [2, 4],
    [1, 2, 3],
    []
]
"""

visited = [False] * (n + 1)

# visited = [False, False, False, False, False, False]
#                     1      2      3      4      5

answer = [0] * (n + 1)
#[0 0 0 0 0 0]
#  1 2 3 4 5

def dfs(x): #x는 노드
    global order #order은 지역함수이기 때문에 def 밖에서도 사용할 수 있도록 global처리 해줘야 함.
    visited[x] = True #예)1번을 호출 했을 때 true로 바꿔줌 visited=[ False, True, False, False, False, False]
                      #   def 한번 돈 결과 1번 다음 2번 방문함. 2번도 true로 바뀜. visited=[ False, True, True, False, False, False]
    # print(x) # 현재 방문한 노드를 출력, 1이 출력됨. 
    answer[x] = order  # [핵심] 노드를 방문한 "순서"를 기록. answer=[0 1 0 0 0 0] 이렇게 바뀜
    order += 1  #반복횟수가 곧 방문순서. 따라서 한번 반복할 때마다 1씩 증가하여 방문 순서를 나타냄. Q 윗줄의 order변수가 처음 나왔는데, 그 위에다 order=0 안 해줘도 되나?
    # 현재 노드(x)의 인접 노드를 확인하며
    for y in graph[x]:
        # 인접 노드인 y가 아직 방문하지 않은 노드라면 1번 노드의 인접 노드들이 graph[1]에 리스트로 저장되어 있음. 1번 방문 후 다음 방문할 곳이 5번이라면 
        #  5번은 graph[1]안에 있을 것이고 아직 방문 전이기 때문에 visited[5]= false임. 따라서 2번으로 def 함수가 다시 실행. 방문처리 후 oder +1.
        #  만약 graph[5]=[1] 뿐이라면 이미 1번은 방문했기 때문에 def 함수는 종료.
        if not visited[y]:
            dfs(y)      #재귀 함수. 본인의 함수 안에서 본인을 호출함. 재귀함수는 현재 함수만 고려하지 않음.
                        #함수가 마지막이라면 이전 함수로 돌아감. 모든 함수가 종료가 되면 비로소 재귀함수 종료.


order = 1
dfs(r) #위에 정의된 함수대로 실행. r은 시작노드

for i in range(1, n + 1):
    print(answer[i])
