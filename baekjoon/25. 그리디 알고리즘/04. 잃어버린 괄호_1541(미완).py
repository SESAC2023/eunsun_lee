import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=input().strip()
#n='('+n+')'
n=list(n.split('-'))

a=[]    #더하기로 연결되어 있는 것들을 합하기 위해 분리
for i in n :
    if '+' in i :
        p=list(map(int, i.split('+')))  
        a.append(p)
    else :
        p=int(i)
        a.append([p])
#print(a)
      
b=[] #합한 값들

for i in a :
    x=0
    for j in i :
        x += j
    b.append(x)
  
s=0
for i in b[1:] :
    s -= i

s=s+b[0]
    
print(s)


""" 괄호 식 표현 코드.  문자열이기 떄문에 계산 불가.
a=""

for i in n[0:-1] :
    a=a+i+')-('

a=a+n[-1]
print(a)

#c=n.count("(")-n.count(')')
#n.append(")"*c)   #모자른 괄호 닫기"""


print
