from string import ascii_lowercase
import sys
input = sys.stdin.readline

a=list(ascii_lowercase) #소문자 리스트 만들기. 대문자 리스트는 ascii_uppercase

b=input()

c=[-1]*26

for i in a :
    
    if b.find(i)!=-1 :
        c[a.index(i)]=b.index(i)

for i in c:
    print(i, end=' ')
