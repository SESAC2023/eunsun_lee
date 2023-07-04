import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

k= int(input())
array=[]

for j in range(k) :
  a = input().strip()
  array=[]
  for i in a:
      print(array)
      if array == [] and i ==")" :
          print('NO')
          array.append('1')
          break
      if i == '(' :
          array.append(i)
      if i == ')' :
          array.pop()
          print(array)
  if len(array)==0:
      print('YES')
  else:
      print('NO')


"""
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

k = int(input())
array = []
s=0
for i in range(k) :
    a = input()
    s=0
    for i in a :
        if i== '(' :
            s += 1
        if i ==')' :
            s -= 1
            if s < 0 :
                array.append('NO')
                break
    if s==0 :
        array.append('YES')
    else :
        array.append('NO')
for i in array :
    print(i) """
