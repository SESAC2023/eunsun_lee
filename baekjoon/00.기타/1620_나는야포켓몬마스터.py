from collections import deque
import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m = map(int, input().split())

poketmon_book = {} #key : num

for i in range(n) : #poketmon_book
    poketmon = input().strip()
    poketmon_book[str(i+1)] = poketmon
#print(poketmon_book)
r_poketmon_book = dict(map(reversed, poketmon_book.items())) #key = name
#poketmon_list = list(poketmon_book.values())
#print(poketmon_list)

for _ in range(m) :
    ques = input().strip()
    try  : #문제가 이름으로 들어올 때
        answer = poketmon_book[ques]
        
    except :  #문제가 숫자일 때

        answer = r_poketmon_book[ques]
    
    print(answer)
