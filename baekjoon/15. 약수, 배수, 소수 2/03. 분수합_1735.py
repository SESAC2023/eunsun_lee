import sys
import math
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

a, b = map(int, input().split())
a1, b1 = map(int, input().split())

a2, b2 = (a*b1)+(a1*b), b*b1

common = math.gcd(a2,b2) #최대공약수를 직접 구하면 시간 초과남.

#for i in range(2, int(min(a2,b2)+1)) : #30,000
#    if a2%i==0 and b2%i==0:
 #         common = i

print(int(a2//common), int(b2//common))
