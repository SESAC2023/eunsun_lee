from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
order = []
st=[]
b='push 1'

for i in range(n) :
    a=input().strip()
    order.append(a)

for i in order :
    if i[0]=='p' and i[1] =='u':
        st.append(int(i[5:]))
    if i == 'pop' :
        if st==[] :
            print(-1)
        else :
            print(st[-1])
            st.pop()
    if i=='size' :
        print(len(st))
    if i =='empty' :
        if st==[] :
            print(1)
        else :
            print(0)
    if i=='top' :
        if st==[] :
            print(-1)
        else :
            print(st[-1])
