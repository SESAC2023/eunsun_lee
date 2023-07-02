import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=[]

for i in range(9) :
    a=list(map(int, input().split()))
    n.append(a)

print(n)

row_s=0
row=[]

for i in n :
        if i.count(0) ==1 :
            i[i.index(0)]= 45-sum(i)

for j in n :
        row_s=0
        row=[]
        for x in range(9) :
            row_s+=j[x]
            row.append(j)
            if row_s==45 :
                pass
            elif row.count(0)==1 :
                j[j.index(0)] = (45-sum(row))


print(n)
for i in range(0,9,3) :

    for j in range(0,9,3) :

        s=sum(n[i][j:j+3])+sum(n[i+1][j:j+3])+sum(n[i+2][j:j+3])
        c=n[i][j:j+3].count(0)+n[i+1][j:j+3].count(0)+n[i+2][j:j+3].count(0)
        if c==1 :
            if 0 in [i+1][i:i+3] :
                n[n[i][i:i+3].index(0)]=(45-s)
            if 0 in [i+1][i:i+3] :
                n[n[i][i:i+3].index(0)]=(45-s)
            if 0 in [i+1][i:i+3] :
                n[n[i][i:i+3].index(0)]=(45-s)
print(n)
