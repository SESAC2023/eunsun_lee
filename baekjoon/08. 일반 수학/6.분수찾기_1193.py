from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

x = int(input())

line = 1

while x > line:
    x -= line
    line += 1
  
y = line - x +1

if line % 2 ==1 :
    print(y,"/",x, sep="")
else :
    print(x,"/",y,sep="")
