import sys
input = sys.stdin.readline

counter = dict()
data = input().strip()
data=data.upper()

for x in data:
    x = x.upper() # 무조건 대문자로 통일
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1


c=0
for i in counter.values() :
    if i==max(counter.values()) :
        c +=1

if len(data)==1 :
    print(data)
elif c>=2 :
    print('?')
else :
    for k, v in counter.items() :
        if max(counter.values())  ==v :
            print(k)
