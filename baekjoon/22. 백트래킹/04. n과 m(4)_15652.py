from itertools import combinations_with_replacement
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m=map(int, input().split()) #중복허용 조합 구하기

n_list=[i for i in range(1,n+1)]

com=combinations_with_replacement(n_list, m)

#print(com)

for i in com :
    for j in i :
        print(j, end=' ')
    print()
