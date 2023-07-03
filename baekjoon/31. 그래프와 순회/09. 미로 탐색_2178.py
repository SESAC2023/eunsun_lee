from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m = map(int, input().split())
array=[]

for i in range(n) :
    a=input().strip()
    temp=[]
    for i in a:
        temp.append(int(i))

    array.append(temp)

visited = [[False]*m]*n
order = [[0]*m]*n

q=deque()
q.append((0,0))
visited[0][0] = 1
order[0][0] = 1

#상 하 좌 우
dx= [0, 0, -1, 1]
dy= [-1, 1, 0, 0]

while q :
  x, y = q.popleft()
  for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny <0 or nx>=n or ny >=m :
          continue
      if array[nx][ny] ==0:
          continue
      if visited[nx][ny] == False :
          q.append((nx, ny))
          visited[nx][ny] == True
          order[nx][ny] = order[x][y] +1

print(order[n-1][m-1])
