a=[1,3,5,7,9]
#for i in range(1,10,2) :
for i in a :
    for j in range(4-i//2): #빈칸 수가 4,3,2,1,0 이므로 range()안의 숫자를 4,3,2,1,0이 되게 함
        print(end=" ") # (" ", end="")와 결과가 같음. 빈칸은 하나만 입력해야 위 range의 개수만큼 출력됨. " ",end=" ")이렇게 쓰면 빈칸은 두배가 됨
    print("*"*i)

for i in [9,7,5,3,1] : #a.reverse()로 하면 none 값이 나옴-> 왜???, b라는 새로운 리스트로 해도 그럼. (copy해야 하나? 나중에 검색해보기)
    for j in range(4-i//2):
        print(end=" ")  
    print("*"*i)
