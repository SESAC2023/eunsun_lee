import sys

test_case=int(sys.stdin.readline())

for t in range(test_case):
    a, b=map(int,sys.stdin.readline().split())
    print(a+b)
