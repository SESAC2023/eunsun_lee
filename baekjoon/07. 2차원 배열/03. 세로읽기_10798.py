import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
array=[]
b=[[] for i in range(15)]
l=[]
for i in range(5) :
    cha=input().strip()
    array.append(cha)
    l.append(len(cha))

for i in range(5):
    for j in range(l[i]) :
        b[j].append(array[i][j])
            
for i in range(15) :
    for j in b[i] :
        print(j,end='')
