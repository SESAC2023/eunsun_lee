from itertools import permutations
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
num=list(map(int, input().split()))


p,m,t,d=map(int,input().split())  #차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
l = []

for i in range(p) :
    l.append("+")
for i in range(m) :
    l.append("-")
for i in range(t) :
    l.append("*")
for i in range(d) :
    l.append("//")

array = permutations(l)
array = list(set(array))
for i in array :
    print(i)

str = ""
for i in range(n) :
    num[i]+
