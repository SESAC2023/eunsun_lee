
import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

array=[]
def br(y) :
    array = []
    for i in y:
        if i == '(' or  i == '{' or i == '[':
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
        if i == '(' or i ==')' or i =='{' or i =='}' or i =='[' or i ==']' :
            temp.append(i)    
    br(temp)
