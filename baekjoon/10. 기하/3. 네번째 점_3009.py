
import sys
input = sys.stdin.readline

a=[] #x리스트
b=[] #y리스트


for i in range(3):
    x,y=map(int, input().split())
    a.append(x)
    b.append(y)
a.sort()
b.sort()

# 축에 평행하므로 같은 수가 두개씩 있음. 따라서 x,y 각각 다른 거 하나씩 추출하면 됨
if a[0]==a[1] : 
    print(a[2], end= " ")
else :
    print(a[0], end=" ")

if b[0]==b[1] :
    print(b[2], end= " ")
else :
    print(b[0], end=" ")
