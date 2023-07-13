import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input()) 
enter=input()
arr=set()
cnt =0
for i in range(n-1) :
    a = input().strip()
    if i == n-2 and a != "ENTER":
        arr.update([a])
        cnt += len(arr)
    elif i == n-2 and i == "ENTER" :
        cnt += len(arr)
    elif a != "ENTER"  :
        arr.update([a])

    else :
        cnt += len(arr)

        arr=set()  

print(cnt)
