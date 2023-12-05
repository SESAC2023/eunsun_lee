import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc = int(input())
enter = []
out = []

cnt = 0 
#enter, out 리스트 비교. 같지 않다면 추월한 것. 
#뒷차가 추월해서 앞으로 왔으니까 다름
#out의 차랑번호를 enter에서 찾아서 기록

for _ in range(tc) :
    n = input().strip()
    enter.append(n)

for i in range(tc) :
    m = input().strip()
    out.append(enter.index(m))
#print(out)

pre = 0 # 추월하지 않았을 때의 첫 순서
array = [i for i in range(tc)] # 기준 업데이트를 위한 리스트. 추월차 번호 하나씩 제거하면서 추월하지 않은 차만 고르기 위함

for i in range(tc) :
    #print(pre)
    if pre == out[i] :
        array.remove(out[i])
        if array != [] :
            pre = array[0]
    elif out[i] > pre :
        cnt += 1
        array.remove(out[i])
        
print(cnt)

#-----------------------------------------
#실패 코드 = > out 리스트를 제대로 갱신하는 것 자체가 불가능. insert에서 밀림.=>인덱스로 비교하기 때문에 제대로 순서 맞추는 게 어려움.
import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc = int(input())
enter = []
out = []

cnt = 0
#enter, out 리스트 비교. 같지 않다면 추월한 것. 
#뒷차가 추월해서 앞으로 왔으니까 다름
#out의 차랑번호를 enter에서 찾아서 기록

for i in range(2*tc) :
    n = input().strip()
    if i < tc :
        enter.append(n)
    else :
        out.append(n)
#print(enter)
#print(out)

"""
for i in range(tc) :
    while enter[i] != out[i] :
        cnt += 1
        out[i] = enter[i] #원래 위치로 이동
        
        print(i, ":", enter)
        print(i, ":", out) """
correct_out = {}
temp_array =[]

print(enter)
for i in range(tc) :
    
    while enter[i] != out[i] :
        cnt += 1
        temp = out[i]
        temp_array.append(temp)
        id = enter.index(temp)
        correct_out[id] = temp
        out.remove(temp)
        print(temp)
        
    if i not in correct_out.keys() :
        correct_out[i] = out[i]
    correct_out = dict(sorted(correct_out.items()))
    
    while temp_array != [] :
        x = temp_array.pop()
        id_x = next(key for key, value in correct_out.items() if value == x)
        out.insert(id_x, x)
    print(i, ":", out)
    print("cnt: ", cnt)
print(cnt)
print(enter)
print(out)
#print(correct_out)
