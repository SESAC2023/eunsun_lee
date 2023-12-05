from collections import deque
import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

max_value = 0 #현재 언덕 최고점
s = 0         #가장 높은 언덕 높이
pre = 0

#가장 높은 언덕이 되면 s 업데이트.
#이전값이랑 같거나 이전값보다 크면 max_value 업데이트 => 새로운 언덕의 시작

for i in array[::-1] :
  if pre > i : #언덕 계산
      if s < max_value-i:
          s = max_value-i
      else:
          pass
  else: #새로운 언덕
      max_value = i
  pre = i
print(s)
