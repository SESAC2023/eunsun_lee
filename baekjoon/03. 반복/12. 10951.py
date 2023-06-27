import sys

data = sys.stdin.readlines()

for d in data :
    a,b=map(int,d.split(" "))
    print(a+b)
