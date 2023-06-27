n=int(input())

a=[i for i in range(1,2*n,2)]
#for i in range(1,10,2) :
for i in a :
    for j in range(n-i//2-1):  #빈칸 수가 0~n-1 이므로 range()안의 숫자를 n-1부터 0까지 나올 수 있게 함
        print(end=" ")   # (" ", end="")와 결과가 같음. 빈칸은 하나만 입력해야 위 range의 개수만큼 출력됨. " ",end=" ")이렇게 쓰면 빈칸은 두배가 됨
    print("*"*i)
  
a.pop()
a=list(reversed(a)) #Q : a.reverse()로 하면 none 값이 나옴-> 왜???,

for i in a :
    for j in range(n-i//2-1):
        print(end=" ")  
    print("*"*i)
