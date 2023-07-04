import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
array=[]

for i in range(n) :
    temp=[]
    a=input().strip()
    for j in a :
        temp.append(j)
    array.append(temp)

visited=[[False]*n for i in range(n)]

#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x,y) :
    global cnt
    visited[x][y] = True
    cnt+=1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny <0 or nx>=n or ny >= n :
            continue
        if array[nx][ny] == 0 :
            continue
        if not visited[nx][ny] :
            dfs(nx, ny)
an=0
answer = []
for i in range(n) :
    for j in range(n) :
        if array[i][j] == 0 :
            continue
        if not visited[i][j] :
            an +=1
            cnt=0
            dfs(i, j)
            answer.append(cnt)

print(an)
answer.sort()
for x in answer :
    print(x)
