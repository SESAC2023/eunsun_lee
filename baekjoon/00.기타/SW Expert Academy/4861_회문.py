tc = int(input())

for test in range(tc) :
    #2차원 배열로 입력 받기
    arr = []
    n, m = map(int, input().split())
    for _ in range(n) :
        temp_list = []
        for a in input().strip() :
            temp_list.append(a)
        arr.append(temp_list)
   # print(arr)
    #가로 회문 찾기
    for x in range(n) :
        for y in range(n-m+1) :
            temp = arr[x][y:y+m]
            if temp[:] == temp[::-1] :
                print(f'#{test+1}', end=" ")
                for p in temp :
                    print(p, end="")
                print()
                break
       
    #세로 회문 찾기
    else :
        arr = list(map(list, zip(*arr)))
       # print("vertical")
        for x in range(n) :
            for y in range(n-m+1) :
                temp = arr[x][y:y+m]
                if temp[:] == temp[::-1] :
                    print(f'#{test+1}', end=" ")
                    for p in temp :
                        print(p, end="")
                    print()
                    break
