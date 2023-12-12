import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc = int(input())

d = [tuple(map(int, input().split())) for _ in range(tc) ]

# 끝나는 시간이 빠른 거 먼저 선택!! 그래야 최대한 많은 회의 선택 가능
d = sorted(d, key =lambda x : (x[1], x[0]) )
#print(d)

pre_meeting = -1
cnt = 0
for start, end_time in d:

    if start >= pre_meeting :
        pre_meeting = end_time
        cnt += 1
print(cnt)
        
