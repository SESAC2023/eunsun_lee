import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input()) 
arr=[]
for i in range(n) :
    a = input().strip()
    if i ==0 :
        arr = "ENTER"
    else :
        arr += " " + a

#print(arr)
arr=list(arr.split("ENTER"))
arr1 = []
for i in arr :
    arr1.append(set(i.split()))

s=0
for i in arr1 :
    s += len(i)

print(s)
