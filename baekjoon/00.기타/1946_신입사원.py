import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n) ]
    arr = sorted(arr, key = lambda x : x[1])
   # print(arr)
    cnt = 0

    standard = n+1 # 꼴등 순위보다 더 큰수로 잡고 갱신할 수 있게 함
    for i in range(n) :
        if arr[i][0] < standard :
            cnt += 1
            standard = arr[i][0]
    
    print(cnt)
