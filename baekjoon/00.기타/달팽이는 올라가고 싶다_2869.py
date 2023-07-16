"""재귀 런타임 오류

a, b, v = map(int, input().split()) #a 낮시간에 올라가는 길이, b는 밤에 내려오는 길이, v는 나무 길이

v1=v-a #전날까지 도달해야 하는 최소 높이
v2 = v1 % (a-b)
v3 = v1 // (a-b)

days = 0
hight = 0
def hi(d, n, h) : #낮, 밤, 높이
    global days
    global hight
    days += 1
    hight += d
    if hight < h :
        hight -= n
        return hi(d, n, h)
    else :
        return days

print(hi(a, b, v))
"""

import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

a, b, v = map(int, input().split())

v1=v-a #전날까지 도달해야 하는 최소 높이
v2 = v1 % (a-b) #항상 a보다 작을 
v3 = v1 // (a-b)

if a == v :
    print(1)
elif v3*(a-b)+a<v :
    print(round(v1//(a-b)) +2)
else :
    print(round(v1//(a-b)) +1)
