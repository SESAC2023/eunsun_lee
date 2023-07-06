"""시가초과 코드 

from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

for i in range(n) :
    try :
        f=list(input().strip()) #수행 함수 순서
        m=int(input()) #수의 개수
        l=input()  #수 리스트
        l=l.replace('[','')
        l=l.replace(']','')
        l=deque(map(int, l.split(',')))
    
              
        for i in f :
            if i=='R' :
                l=deque(reversed(l))
              
            elif i =='D' :
                l.popleft()
        print('[', end='')
        for i in l :
            if i==l[-1] :
                print(i, end=']')
            else :
                print(i, end=',')
    except :
        print('error')          
        """

"""실패 코드
from collections import deque
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
r_cnt=0

for i in range(n) : #100
    try :
        r_cnt=0
        f=list(input().strip()) #수행 함수 순서
        m=int(input()) #수의 개수
        l=input()  #수 리스트
        l=l.replace('[','')
        l=l.replace(']','')
        l=deque(map(int, l.split(',')))
    
              
        for i in f : #100,000
            if i=='R' :
                r_cnt+=1
              
            elif i =='D' :
                if r_cnt%2==0 :
                    l.popleft()
                else :
                    l.pop()
        if r_cnt%2==1 :
            l=deque(reversed(l))
          
        print('[', end='')          

        for i in l :
            if i==l[-1] :
                print(i, end=']')
            else :
                print(i, end=',')
        
        print()
      
    except :
        print('error')          
    """
    
