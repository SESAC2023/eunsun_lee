import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
"""
#이동 상황을 보기 위한 리스트. 없어도 됨.
l1 = [i for i in range(1, n + 1)]
l2 = []
l3 = []
"""

def hanoi(x, left, right, middle):
  if x == 1:  #예제에 따라 처음엔 x = 3이니까 else를 수행. else에서도 x-1도 1이 아니니까 다시 -1 로 올라감. 그렇게 1이 될 때 (1,3)을 반환. 그래서 처음에 프린트된 x가 1임.
    print(left, right)


#        right.append(left.pop(0))
#       print(x)
#      print(left, middle, right)
  else:
    hanoi(x - 1, left, middle, right)
    #     print(x-1)
    print(left, right)
    #      middle.append(left.pop(0))
    #    print(left, middle, right)
    hanoi(x - 1, middle, right, left)
    
print(2**n - 1)
hanoi(n, 1, 3, 2)
#hanoi(n, l1, l3, l2) #상황을 보기 위해
