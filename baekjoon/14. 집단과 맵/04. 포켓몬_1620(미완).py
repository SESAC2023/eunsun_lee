import sys
input = sys.stdin.readline

n,m=map(int, input().split())  #n은 도감의 포켓몬 수, m은 맞춰야 하는 문제수

v=[] #이름
k=[i for i in range(1,n+1)] #번호

for i in range(n) :
    a=input().strip()
    v.append(a)

d=dict(zip(v,k))             #도감 만들기
print(d)
for i in range(m):
    b=input().strip()
    if b in k : #만약 숫자면 이름 출력
        print('a=', v[int(b)-1] ) 
    else : #이름이면 숫자출력
        print('a=', v.index(b)+1 ) 
