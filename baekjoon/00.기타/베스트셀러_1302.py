import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

dict = {}

for i in range(n) :
    book = input().strip()
    if book not in dict.keys() : 
        dict[book] = 1
    else :
        dict[book] += 1
#dict.keys().sort()

max_book = ""
max_c = -1e6
for k, v in sorted(dict.items()): # sort는 리스트만 사용가능. 따라서 sorted 사용. 튜플이 담긴 리스트로 반환해서 다서 dict로 묶는 방법
                                  # sorted(dict.items(), key = lambda x : (-x[1], x[0]) => 가로 안은 정렬 기준 순서
    if max_c < v :
        max_book = k
        max_c=v
print(max_book)

#-----------------method 2 : defaultdict 활용(없는 키를 자동으로 생성해줌)
from collections import defaultdict
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

dict = defaultdict(int)

for i in range(n) :
    book = input().strip()
    dict[book] += 1

#dict.keys().sort()

max_book = ""
max_c = -1e6
for k, v in sorted(dict.items()):
    if max_c < v :
        max_book = k
        max_c=v
print(max_book)
