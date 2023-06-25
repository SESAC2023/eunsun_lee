data = input() 
data = data.split(" ") 
data = list(map(int, data)) 

a = data[0] 
b = data[1] 

print(a+b)
print(a-b)
print(a*b)
print(int(a//b))
print(a%b)

""" 2번째 방법
a, b=map(int,input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)


"""
