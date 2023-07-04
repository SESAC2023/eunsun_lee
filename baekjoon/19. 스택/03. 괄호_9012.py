import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

k= int(input())

def br(a) :
  array=[]
  for i in a:
  #    print(array)
      if array == [] and i ==")" :
          array.append(0)
          break
      if i == '(' :
          array.append(i)
      if i == ')' :
          array.pop()
   #       print(array)
  if 0 in array :
      print('NO')
      
  elif len(array)==0:
      print('YES')
  else:
      print('NO')


for j in range(k) :
  x = input().strip()
  br(x)
