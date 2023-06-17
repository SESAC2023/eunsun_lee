data = input() 
data = data.split(" ") 
data = list(map(int, data)) 

a = data[0] 
b = data[1] 
c = data[2]

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
