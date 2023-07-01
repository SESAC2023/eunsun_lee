from itertools import product
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m=map(int, input().split()) #nㅠm 중복순열 구하기

n_list=[i for i in range(1,n+1)]

per = product(n_list, repeat = m)

for i in per :
    for j in i :
        print(j, end=' ')
    print()
