from collections import deque
import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

paper = []
for _ in range(n) :
    paper.append(list(map(int, input().split())))
#print(paper)


white = 0
blue = 0

def cutting(c, r, n) :
    global white, blue
    
    color = paper[c][r] #왼쪽 위 색깔. 이거랑 다르면 cutting
    
    for i in range(n) :
        for j in range(n) :

            if color != paper[c+i][r+j] :
                
                cutting(c+n//2, r+n//2, n//2)
                cutting(c, r+n//2, n//2)
                cutting(c+n//2, r, n//2)
                cutting(c, r, n//2)
                
                return

    #모든 색이 같을 때 세는 것. 그래서 for문 앞에다 두면 안 됨
    if color == 0 : 
        white += 1
    else :
        blue += 1
        
cutting(0,0,n)

print(white)
print(blue)
