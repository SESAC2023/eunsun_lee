import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

grade=[] #글자 하나씩 새로 나올 때마다 추가
num=0
sum=0
d={
'A+':4.5,
'A0':4.0,
'B+':3.5,
'B0':	3.0,
'C+':	2.5,
'C0':	2.0,
'D+':	1.5,
'D0':1.0,
'F' :	0.0}

a=[] #점수
b=[] #학점
for i in range(20) :
    cha=input().strip()
    if cha[-1]=='P' :
          pass
    elif cha[-1]=='F':
          a.append(cha[-1])
          b.append(cha[-5:-2])
      
    else :
          a.append(cha[-2:])
          b.append(cha[-6:-3])

for k,v in d.items() :
    for i in range(len(a)):
        if a[i]==k:
            sum+=v*float(b[i])
            num+=float(b[i])
print(sum/num)   
