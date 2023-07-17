import sys
import copy

sys.setrecursionlimit(int(1e6))

while True :
    
    arr = list(map(int, input().split()))
    arr.sort()
    if arr == [0, 0, 0] :
        break
    if arr[2]**2 == arr[0]**2 + arr[1]**2 :
        print("right")
    else :
        print("wrong")
