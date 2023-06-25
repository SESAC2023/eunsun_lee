import math

d={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,  'A':10, 'B': 11, 'C':12, 'D':13, 'E':14, 'F': 15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y': 34, 'Z': 35}

n, b=map(int,input().split()) #n은 십진법 숫자, b는 진법

l=int(math.log(n,b))

temp=[]
a=list(d.keys())

for i in range(l+1):
    x=n%b #나머지 : 진법 구성
    n=n//b #몫
    temp.append(a[x])
  
temp=temp[-1::-1]
for i in temp :
    print(i, end="")
