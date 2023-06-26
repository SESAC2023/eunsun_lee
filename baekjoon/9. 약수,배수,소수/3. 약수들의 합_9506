import sys
input = sys.stdin.readline


temp=[]
s=0

#약수 구해서temp에 넣기
while True :
    
    n=int(input())
    if n==-1 :
        break
    for i in range(1,n+1) :
        if n%i==0 :
            temp.append(i)
        

    #temp에는 항상 자기자신이 포함. 따라서 자기 자신 빼주기
    temp.sort()
    temp.pop() 
  #  print(temp)
  
    #약수의 합 구하기
    for i in temp :
        s +=i
  #  print(s)
  
    #완전수인지 파악하기
    if n==s :
        print(n, '=', end=' ')
        for i in temp :
            print(i, end=' ')
            if i==temp[-1] :
                print("")
            else :
                print('+', end=' ')
    else :
        print(n,'is NOT perfect.')
    temp.clear() #한번 수행할 때마다 클리어 해주지 않으면 이전 약수에 누적됨.
    s=0
    
