import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input()) #진짜 약수의 개수

lst=list(map(int, input().split()))

print(min(lst)*max(lst))
