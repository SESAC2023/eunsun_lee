a = [int(input()) for _ in range(10)]
b=[i%42 for i in a]

c=set(b)
print(len(c))
