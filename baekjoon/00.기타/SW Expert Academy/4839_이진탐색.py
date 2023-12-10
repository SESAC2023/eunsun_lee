from sre_constants import CATEGORY_NOT_LINEBREAK
import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc = int(input())


def binary_search(l, r, p) :
    '''
    
    '''
    global cnt
    
    cnt = 0
    while True:
        temp = int((l+r)/2)
        cnt += 1
        if temp < p :
            l = temp
        elif temp > p:
            r = temp
        else :
            break
    return cnt


for i in range(tc) :
    total, a, b = map(int, input().split())
    A = binary_search(1,total, a)
    B =  binary_search(1,total, b)
    if  A < B :
        print(f'#{i+1} A')
    elif A > B:
        print(f'#{i+1} B')
    else :
        print(f'#{i+1} 0')

"""
    l_a = 1
    l_b = 1
    r_a = total 
    r_b = total

    cnt_a = 0
    cnt_b = 0


    while int((l_a + r_a)//2) == A :
        cnt_a += 1
        temp_a = int((l_a + r_a)//2)
        if temp_a  < A :
            l_a = temp_a 
        elif temp_a  > A :
            r_a = temp_a
            
    while int((l_b + r_b)//2) == B :
        cnt_b += 1
        temp_b = int((l_b + r_b)//2)
        if temp_b < B :
            l_b = temp_b
        elif temp_b > B :
            r_b = temp_b

    print(cnt_a)
    print(cnt_b)
    print(l_a, r_a)

    if cnt_a == cnt_b :
        print(f'#{i+1}', 0)
        
    elif cnt_a < cnt_b :
        print(f'#{i+1}', "A")
    else:
        print(f'#{i+1}', "B") 
"""
