import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc = int(input())

for i in range(tc) :
    n = int(input())
    school = ""
    mount = 0
    for j in range(n) :
        a, b = input().split()
      
        if int(b) > mount :
            mount = int(b)
            school = a
    print(school)
