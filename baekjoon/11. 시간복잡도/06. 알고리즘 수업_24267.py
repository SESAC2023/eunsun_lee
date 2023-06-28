import sys
input = sys.stdin.readline

n=int(input())
s=0
for i in range(n-2) :
    s += i*(i+1)*(i+2)

print(int((n-2)*(n-1)*n/6))
print(3)
    
