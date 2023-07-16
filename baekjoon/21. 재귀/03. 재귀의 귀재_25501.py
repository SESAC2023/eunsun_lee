import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
cnt =0
def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1 
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1) #s가 한글자이거나 없으면 1을 반환



tc=int(input())

for i in range(tc) :
    a = input().strip()
    cnt = 0
    print(isPalindrome(a), end=" ")
    print(cnt)

