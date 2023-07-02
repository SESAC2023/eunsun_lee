import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=input().strip()
n='('+n+')'
for i in n :
    if i=='-' :
        n[n.index('-')]='-('

print(n)
print(n.index('-'))

c=n.count("(")-n.count(')')
n.append(")"*c)   #모자른 괄호 닫기
