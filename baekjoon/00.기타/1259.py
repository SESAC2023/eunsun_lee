import sys
import copy

sys.setrecursionlimit(int(1e6))

while True :
    
    a = list(input().strip())
    if a == ['0'] :
        break
    b = a.copy()
    b = b[::-1]
    if a == b :
        print("yes")
    else :
        print("no")
