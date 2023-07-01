from itertools import combinations
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m=map(int, input().split()) #nCm 조합 구하기

n_list=[i for i in range(1,n+1)]

com=combinations(n_list, m)

#print(com)

for i in com :
    for j in i :
        print(j, end=' ')
    print()
