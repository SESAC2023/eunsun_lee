import sys
import copy

sys.setrecursionlimit(int(1e6))

arr = list(map(int, input().split()))

asc = arr.copy()
dsc = arr.copy()
asc.sort()
dsc.sort(reverse = True)

if arr == asc :
    print("ascending")
elif arr == dsc :
    print("descending")
else :
    print("mixed")
