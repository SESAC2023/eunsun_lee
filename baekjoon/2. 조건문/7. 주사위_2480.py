a=input()

a=list(map(int, a.split()))

if a[0]==a[2]==a[1] :
  print(10000+a[0]*1000)

elif a[0]!=a[1] and a[0]!=a[2] and a[1]!=a[2] :
    maxValue = a[0]   # 이 방법보다 max(a,b,c)*100을 하는 게 더 간단함
    for i in range(1, len(a)):
        if maxValue < a[i]:
            maxValue = a[i]
    print(maxValue*100)
  
else :

    arr = []

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                if a[i] not in arr:
                    arr.append(a[i])
    print(arr[0]*100+1000)
