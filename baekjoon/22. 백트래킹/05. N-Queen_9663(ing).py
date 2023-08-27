from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n) :
    for j in range(n):
        arr.append((i, j))
visited = [False for i in range(n*n)]
selected = []
cnt = 0
