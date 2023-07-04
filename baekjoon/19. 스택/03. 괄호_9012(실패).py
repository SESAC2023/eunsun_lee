import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

k = int(input())
array = []
s=0
for i in range(k) :
    a = input()
    s=0
    for i in a :
        if i== '(' :
            s += 1
        if i ==')' :
            s -= 1
            if s < 0 :
                array.append('NO')
                break
    if s==0 :
        array.append('YES')
    else :
        array.append('NO')
for i in array :
    print(i)
