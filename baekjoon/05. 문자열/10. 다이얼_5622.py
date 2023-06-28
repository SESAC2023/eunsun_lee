from string import ascii_uppercase
import sys
input = sys.stdin.readline

n=input().strip()
k_list = list(ascii_uppercase)
v_list = []

for i in range(2,10) :
    v_list.append(i+1)

#알파벳에 매칭할 시간 구하기
v_list=v_list*3
v_list.append(8)
v_list.append(10)
v_list.sort()

#딕셔너리 만들기
d=dict(zip(k_list, v_list))
s=0


for i in list(n) :
    #s+=d.values(i) #TypeError: no arguments(1 given) 오류
    s+=d[i]
  
print(s)
