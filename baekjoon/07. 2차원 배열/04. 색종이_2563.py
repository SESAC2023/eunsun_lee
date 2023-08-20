import sys
import math
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc=int(input())

visited = [[0 for i in range(100)] for i in range(100)]

for i in range(tc) :
    a, b = map(int, input().split())
    visited[a][b:b+10]  = [1 for i in range(10)]
    visited[a+1][b:b+10]   = [1 for i in range(10)]
    visited[a+2][b:b+10]   = [1 for i in range(10)]
    visited[a+3][b:b+10]   = [1 for i in range(10)]
    visited[a+4][b:b+10]   = [1 for i in range(10)]    
    visited[a+5][b:b+10]   = [1 for i in range(10)]
    visited[a+6][b:b+10]   = [1 for i in range(10)]
    visited[a+7][b:b+10]   = [1 for i in range(10)]
    visited[a+8][b:b+10]   = [1 for i in range(10)]
    visited[a+9][b:b+10]   = [1 for i in range(10)]


answer = 0
for i in visited :
    answer += math.fsum(i)
print(int(answer))
