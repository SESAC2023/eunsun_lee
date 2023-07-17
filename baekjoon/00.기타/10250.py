import sys

sys.setrecursionlimit(int(1e6))

#arr = list(map(int, input().split()))

tc = int(input())

for _ in range(tc) :
    h, w, n = map(int, input().split())
    a = str(int(n % h)) #호실의 앞자리, 층수
    b = int(n // h) +1 #호실의 뒷자리

    if a == '0' :
        a = str(h)
        b = int(n // h)
    if b < 10 :
        b='0'+str(b)
    else :
        b = str(b)
    print(a+b)
