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

array = [[0]*9 for i in range(9)] #가능한 수 저장하기.

for i in range(9) : #가로 

    if n[i].count(0) ==1 :
        n[i][n[i].index(0)]= 45-sum(i)
    number=[ i for i in range(1,10)]
    for j in range(9) : #세로
        if n[i][j] != 0 :
            n[i].remove(array[i][j])
    array[i][j].append(number)   
             
        
print(n)
print(array)

for i in range(9) : #세로
        row_s=0
        row_s_list = []
        zero_c = 0
        for j in range(9) : #가로
            row_s+=array[j][i]
            if array[j][i] == 0 :
                zero_c+=1
            if row_s==45 :
                pass
            elif row!=45 and zero_c==1 :
                array[j][i] = (45-row_s)


print(n)
for i in range(0,9,3) :
    for j in range(0,9,3) :

        s=sum(n[i][j:j+3])+sum(n[i+1][j:j+3])+sum(n[i+2][j:j+3]) # 3*3 -> 9개 숫자의 합
        c=n[i][j:j+3].count(0)+n[i+1][j:j+3].count(0)+n[i+2][j:j+3].count(0) # 9개 중 0이 몇 개인지
        if c==1 :
            if 0 in [i+1][i:i+3] :
                n[i][n[i][i:i+3].index(0)+i]=(45-s)
            if 0 in [i+1][i:i+3] :
                n[n[i][i:i+3].index(0)+i]=(45-s)
            if 0 in [i+1][i:i+3] :
                n[n[i][i:i+3].index(0)+i]=(45-s)
print(n)
