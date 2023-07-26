import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

#arr = {"ChongChong"}
arr = ["ChongChong"]
for _ in range(n) :
    a, b = input().split(" ")
    a = a.strip()
    b = b.strip()
    if a  in arr :
        arr.append(b)
    if b in arr :
        arr.append(a)

arr = set(arr)
#print(arr)
print(len(arr))
