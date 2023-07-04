from itertools import combinations
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
num=[i for i in range(1, n+1)]

array=[]

for i in range(n) :
    a=list(map(int, input().split()))
    array.append(a)

#팀원 조합 구하기.
#한팀을 뽑으면 나머지 팀은 자동으로 결정. 앞팀을 구하고 이를 통해 다른 팀의 능력치 별도로 계산'
com=list(combinations(num, int(n/2)))
del com[int(len(com)/2):]

num2=set(num)
opposite=[]
#상대팀 구하기
for i in com :
    b=num2-set(i)
    opposite.append(b)

#각 팀의 능력치 구하기
ab=[]
ab2=[]

def abil(list, out):
    for i in range(int(len(list))) :
          com2=[]
          com2 = combinations(list[i] , 2) #한팀씩 소환하여 각각의 능력치 구함.
          ability=0
    
          for x, y in com2 :
              ability += array[x-1][y-1]+array[y-1][x-1]
          out.append(ability)
    return 
      
abil(com,ab)
abil(opposite,ab2)
#print( ab, ab2)

min_v=10e9
for i in range(len(ab)) :
    if abs(ab[i]-ab2[i]) < min_v :
        min_v = abs(ab[i]-ab2[i])
      
print(min_v)
