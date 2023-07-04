
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

array=[]
def br(y) :
    array = []
    for i in y:
        if i == '('  :
            array.append(i)
        if i == '{' :
            array.append(i)
        if i == '[' :
            array.append(i)

        if i == ')' and array == []:
            array.append(0) 
            break
        if i ==  '}' and array == []:
            array.append(0) 
            break
        if i ==  ']' and array == []:
            array.append(0) 
            break

      
        else :  
            if i==")" and array[-1]=='(' : 
                array.pop()
            elif i=="}" and array[-1]=='{' : 
                array.pop()
            elif i=="]" and array[-1]=='[' : 
                array.pop()
            else :
                array.append(0)
                break
              
    if 0 in array :
        print('no')
    elif len(array)==0:
        print('yes')
    else:
        print('no')

while True:
    temp = []
    a = input().rstrip()
    if a == ".":
        break
    for i in a :
        if i == ('(' or ')' or '{' or '}' or '[' or ']') :
            temp.append(i)
    
    br(temp)


"""
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

array = []
while True:
  y = input()
  if y == ".":
      break
  for i in y:
      if i == '(' or '{' or '[' :
          array.append(i)
      if i == ')' or '}' or ']':
          if array == [] :
              print('no')
              break
          else :  
              if i==")" and array[-1]=='(' : 
                  array.pop()
              elif i=="}" and array[-1]=='{' : 
                  array.pop()
              elif i=="]" and array[-1]=='[' : 
                  array.pop()
              else :
                   print('no')
                   break
          
    

  if len(array)==0:
      print('yes')
  else:
      print('no')
"""

""" 아래의 코드는 (([))]  와 같은 사례를 구분하지 못함.
while True:
  s = 0
  m = 0
  l = 0

  a = input().strip()

  for i in a:
    if i == '(':
      s += 1
    if i == ')':
      s -= 1
      if s < 0:
        print('no')
        break
    if i == '{':
      m += 1
    if i == '}':
      m -= 1
      if s < 0:
        print('no')
        break
    if i == '[':
      m += 1
    if i == ']':
      m -= 1
      if s < 0:
        print('no')
        break
  if a == ".":
    break
  elif s == 0 and m == 0 and l == 0:
    print('yes')
  else:
    print('no') """
