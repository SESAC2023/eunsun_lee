from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = input().strip()
m = input().strip()

string = []
a = len(m)
m_list = list(m)

for i in n :
    string.append(i)
    if string[-a : ] == m_list :
        for _ in range(a) :
            string.pop()

if string == [] :
    print("FRULA")
else : 
    print("".join(string))
