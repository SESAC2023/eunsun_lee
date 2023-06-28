import sys
input = sys.stdin.readline

n,m=map(int, input().split())  #n은 집합 s의 원소 개수, m은 비교군의 개수
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
