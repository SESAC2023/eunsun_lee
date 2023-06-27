import sys
input = sys.stdin.readline



while True :
    a, b=map(int, input().split())

    if a==0 and b==0: #0으로 나눌 수 없으니 종료 조건을 먼저 써줌
        break
      
    elif b%a ==0 :
        print('factor')
    elif a%b==0 :
        print('multiple')
    else :
        print('neither')
