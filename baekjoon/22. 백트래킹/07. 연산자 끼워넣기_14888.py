from itertools import permutations
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
num=list(map(int, input().split()))


p,m,t,d=map(int,input().split())  #차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수

array = ['+'*p, '-'*m, '*'*t, '//'*d]
for i in array :
    if i=="" :
        array.remove("")
array = permutations(array)

