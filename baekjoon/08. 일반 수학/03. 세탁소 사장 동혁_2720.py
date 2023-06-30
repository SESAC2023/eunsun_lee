import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input()) 
change=[25,10,5,1]
ch=0
b=[[] for i in range(n)]

for i in range(n) :
    a=int(input()) 
    for j in change:
        b[i].append(a//j)#동전 단위로 나눈 몫이 그 동전을 줘야 하는 개수. 따라서 큰 동전부터 나누어 가면 됨.
        a=a%j #나머지로 a 업데이트


for i in b :
    for j in i:
      print(j, end=' ')

    print()
      
        
     
        

    
