from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m = map(int, input().split())

array=[]
for i in range(n) :
    a=input().strip() 
    temp=[]
    for i in a :
        temp.append(int(i))
    array.append(temp)

visited=[[0]*(m)]*(n)
order=[[0]*m]*(n)
#print(array)
#print(visited)

# 상, 하, 좌, 우 정의 

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

q=deque()
visited[0][0] = True
order[0][0] = 1  
q.append((0,0)) #출발 노드 넣기

while q :
    x = q.popleft()

    for i in range(4) :#현재 위치에서 네방향 모두 탐색
        nx = x +dx[i] 
        ny = y +dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m :
            continue
        if array[nx][ny] ==0 :
            continue
        if visitied[nx][ny] == 0 :
            visitied[nx][ny] == 1
            q.append((nx,ny))
            order[nx][ny]=order[x][y]+1

print(order[n-1][m-1])
