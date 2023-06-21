n,k= map(int,input().split()) #n=시각, k=포함될 수

for h in range(n+1) :
    for m in range(60):
        for s in range(60):
            h=str(h).zfill(2)
            m=str(m).zfill(2)
            s=str(s).zfill(2)
            time=h+m+s
            if str(k) in time
                 count+=1
          
print(count)
