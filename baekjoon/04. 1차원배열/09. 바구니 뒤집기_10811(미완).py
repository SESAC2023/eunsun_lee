"""실패한 코드

a, b = map(int,input().split()) #a=정수개수, b=역순 횟수
c=[input() for i in range(b)] #역순 취할 인덱스 모음
n=[i for i in range(1,a+1)] #1~a까지의 정수


for i in c:
    
     j=list(map(int,i.split(" ")))
        n.insert(j[0]-1, n.index(j[1]-1)) # 맨 뒤에 숫자를 앞으로 insert하기. insert는 n[]+1에 함. 마지막 인덱스가 같아질때까지. 여기서 막힘....

"""


import sys
input = sys.stdin.readline


a, b = map(int,input().split()) #a=정수개수, b=역순 횟수
n=[i for i in range(1,a+1)] #1~a까지의 정수

#c=list(map(int,c.split()))
for i in range(b): # b번 반복해서 입력받고 입력받은 대로 순서 바꾸기
    x, y =map(int, input().split())
    n[x-1:y]=reversed(n[x-1:y])
    
#    n.insert(j[0]-1, n.index(j[1]-1)) # 맨 뒤에 숫자를 앞으로 insert하기. insert는 n[]+1에 함. 마지막 인덱스가 같아질때까지. 여기서 막힘....

#하나씩 땡기지 않아도 됨 위의 슬라이싱하여 리버스 하면 됨

#리스트 벗기기
for i in n :
    print(i,end=" ")



"""두번째 솔루션

for i in range(m):
    left, right = map(int, input().split())
    left -= 1
    temp = []
    for j in range(left, right):
        temp.append(arr[j])
    for j in range(left, right):
        arr[j] = temp.pop()

for x in arr:
    print(x, end=" ")

"""
