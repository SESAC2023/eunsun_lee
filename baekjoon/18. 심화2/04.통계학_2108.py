import sys
input=sys.stdin.readline

n=int(input())
arr=[]

"""첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다."""


for _ in range(n) :
    a = int(input())
    arr.append(a)

arr.sort()


ave = sum(arr)/len(arr)
#print(sum(arr))
median = arr[int(len(arr)//2)]

range = arr[-1] - arr[0]



d = dict()

for i in arr :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1

max_v = max(d.values())

mode_list = []
mode_list.sort()

for i in arr :
    if d[i] == max_v :
        mode_list.append(i)
#print(mode_list)
mode_list = list(set(mode_list))
mode_list.sort()
if len(mode_list) == 1 :
    mode = mode_list[0]
else :
    mode = mode_list[1]
"""
if ave < 0 :
    round(ave * (-1), 1)
    print"""

print(round(ave))
print(median)
print(mode)
print(range)
