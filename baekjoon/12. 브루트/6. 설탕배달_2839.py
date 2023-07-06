from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

a=n//5
b=n%5

answer = 5000 #문제에서 주어진 n의 최대값

for i in range(n//3+1) :
    a=i+int((n-5*i)//3)
    if 0<=(n-5*i) and  (n-5*i)%3==0 and answer > a :
        answer = a      

if answer == 5000 :
    print(-1)
else :
    print(answer)
