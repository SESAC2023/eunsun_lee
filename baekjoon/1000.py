data = input() #정보를 입력한다는 것. 그래서 입력창에 1,2를 입력하면 결과를 출력하기 위함
data = data.split(" ") #split이란 함수는 공백을 기준으로 데이터를 나누겠다는 뜻
data = list(map(int, data)) 

a = data[0] #인덱스, 첫번째라는 뜻
b = data[1] #인덱스, 두번째라는 뜻

print(a+b)
