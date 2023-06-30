import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n=int(input())  #반복 횟수

print((2**n+1)**2) #사각형의 개수는 4^n
                  #점의 개수는 (한 변의 사각형 개수+1개)의 제곱
