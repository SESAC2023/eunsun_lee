import sys
sys.setrecursionlimit(int(1e6))

s=1
for i in range(3) :
    a = int(input())
    s *= a

arr = list(str(s)) 
#print(arr)

for i in range(10) : #1부터 9를 호출
    print(arr.count(str(i)))
