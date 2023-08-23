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

d = dict()
for i in arr : #m보다 짧은 단어 삭제
    if len(i) >= m :
        if i in d :
            d[i] += 1
        else :
            d[i] = 1

d = sorted(d.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in d :
    print(i[0])
