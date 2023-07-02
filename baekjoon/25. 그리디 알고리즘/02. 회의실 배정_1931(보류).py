import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input()) #회의실 개수

b=[]
a=[]
array = []

for i in range(n) :
    a0=input().strip()
    array.append(a0)

"""for i in array :
    a1,b1=map(int, input().split())
    a.append(a1)
    b.append(b1)"""
  
order=0
print(array)
for i in range(n+1) :
    for j in range(n+1) :
        array[i][0]>=array[j][3]


"""from itertools import combinations
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())
num=[i for i in range(1, n+1)]

array=[]
for i in range(n) :
    (a,b)=map(int, input().spplit())
    dict((a,b) =b-a)"""
    
