#--------------intertools사용 1-------------------------------------------------
from itertools import combinations
tc =  int(input())

for _ in range(tc) :
    n, m = map(int, input().split())
    y = [x for x in range(1,m+1)]
    a = list(combinations(y,n))
    print(len(a))
      
#--------------intertools사용 2-------------------------------------------------
import sys
from itertools import combinations
sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline
tc = int(input())

for i in range(tc) :
    m, n=map(int, input().split()) #nCm 조합 구하기

    n_list=[i for i in range(1,n+1)]

    com=combinations(n_list, m)

#print(com)
    cnt = 0
    for i in com :
        cnt += 1
    print(cnt)

#--------------백트래킹-------------------------------------------------
import sys

sys.setrecursionlimit(int(1e6))

tc = int(input())


def dfs(depth, now) :
    global cnt
    if depth == a :
        cnt += 1
        return
    for i in range(now, b):
        if visited[i]:
            continue
        # 백트래킹은 3단계로 재귀 호출
        # (1) 원소 넣기
        selected.append(arr[i])
        visited[i] = True
        dfs(depth + 1, i)  # (2) 재귀 호출
        # (3) 원소 빼기
        selected.pop()
        visited[i] = False



for _ in range(tc) :
    a, b = map(int, input().split()) #b개에서 a개를 뽑는다.(조합)
  
    visited = [ 0 for i in range(b)]
    selected = []
    arr = [i for i in range(b)]
    cnt = 0
    dfs(0,0)
    print(cnt)
