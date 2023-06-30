import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

a=int(input())
b=[] #글자 하나씩 새로 나올 때마다 추가
c=[] #문자 저장

for i in range(a) :
    b=[] #새로운 단어 입력할 때마다 b 초기화 시켜주기
    cha=input().strip()
    for j in cha :
        if j not in b : #새로 나온 글자는 b에 추가
            b.append(j)
        elif j == b[-1] : #연속된 경우는 무시
            continue
        else :  #이전에 나온 단어이지만 연속되지 않은 경우에는 a에서 1빼기
            a-=1

print(a)            
