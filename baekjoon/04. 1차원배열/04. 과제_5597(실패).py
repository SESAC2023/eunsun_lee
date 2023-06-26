a = [input() for _ in range(28)]
b = [i for i in range(1,31)]

for i in b:
    if i==a :
        b.remove(i)
      
print(min(b))
print(max(b))
