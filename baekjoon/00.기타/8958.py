import sys

sys.setrecursionlimit(int(1e6))

#arr = list(map(int, input().split()))

n = int(input())

for _ in range(n) :
    a = input().strip()
    arr = []
    for i in a :
        if i == "O" :
            arr.append(1)
        else :
            arr.append(0)
    for i in range(1, len(arr)) :
        if arr[i] == 1 :
            arr[i] = arr[i-1] + arr[i]
        
    print(sum(arr))
