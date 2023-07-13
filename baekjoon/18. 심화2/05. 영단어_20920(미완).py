import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


"""
자주 나오는 단어일수록 앞에 배치한다.
해당 단어의 길이가 길수록 앞에 배치한다.
알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
"""


n, m = map(int, input().split()) 
arr=[]
for i in range(n) :
    a = input().strip()
    arr.append(a)

for i in arr : #m보다 짧은 단어 삭제
    if len(i) < m :
        arr.remove(i)
#print(arr)
arr.sort()
print(arr)
b=[]
an=[]
cnt= 0
for i in range(1, len(arr)) :
    if arr[i-1]==arr[i] :
         cnt+=1 
    else :
         b.append(cnt)
         cnt = 0

arr=set(arr)
d=dict(zip(arr,b)) #단어와 횟수
for i in range(1, len(arr)) :
    len(arr[i-1]

