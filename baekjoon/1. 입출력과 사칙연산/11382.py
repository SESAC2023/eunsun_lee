data=input()

data = data.split(" ") #split이란 함수는 공백을 기준으로 데이터를 나누겠다는 뜻
data = list(map(int, data)) 

a=data[0]
b=data[1]
c=data[2]

print(a+b+c)
