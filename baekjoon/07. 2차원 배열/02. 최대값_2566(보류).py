import sys
input = sys.stdin.readline

list=[[0]*9 for i in range(9)]

x=[]
max_value=-1 

for i in range(9) :
    list[i]=map(int,input().split())
    if max(list[i])>max_value :
        max_value=max(list[i])
      
#for i in range (9) :
 #   x=list(map(int,input().split()))

print(max_value)
print(x)


#자꾸 행렬에서 오류가 나서 보류, 나중에 다시
