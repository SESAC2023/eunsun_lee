a=input()
b=input()

a=list(map(int, a.split()))
b=int(b)

if a[0]+(a[1]+b)//60<24 :
    print(a[0]+(a[1]+b)//60, (a[1]+b)%60)

if a[0]+(a[1]+b)//60>=24:
    print(a[0]-24+(a[1]+b)//60, (a[1]+b)%60)
