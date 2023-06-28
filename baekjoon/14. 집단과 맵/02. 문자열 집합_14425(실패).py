import sys
input = sys.stdin.readline

n,m=map(int, input().split())  #n은 집합 s의 원소 개수, m은 비교군의 개수

""" 1번
n_list=[]
m_list=[]

for i in range(n):
    n_list.append(input().strip())

for i in range(m):
    m_list.append(input().strip()) 

n_list=set(n_list)
m_list=set(m_list)

c=n_list&m_list

print(len(c))
"""
"""2번 : 1번과 같은 접근 방법이지만 혹시나 해서 다른 코드 작성함
a=set()
b=set()

for i in range(n):
    a.add(input().strip())

for i in range(m):
    b.add(input().strip()) 


print(int(len(a&b))) """
