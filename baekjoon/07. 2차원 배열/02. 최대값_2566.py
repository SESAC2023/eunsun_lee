import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

array=[]
a=[]
cnt=[]
for i in range(9) :
    cha=list(map(int, input().split()))
    array.append(cha)

for i in range(9):
    a.append(max(array[i]))

max_v=max(a)

ind=(-1,-1)
for i in range(9) :
    for j in array[i] :
        if j==max_v :
            ind=(i+1,array[i].index(max_v)+1)


print(max_v)
for i in ind :
    print(i, end=' ')
