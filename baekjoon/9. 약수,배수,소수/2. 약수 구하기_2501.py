import sys
input = sys.stdin.readline

n, k=map(int, input().split())  # n의 약수 중 k번째로 작은 값 구하기
temp=[]
for i in range(1, n+1) :
    if n%i==0 :
        temp.append(i)

 #오름차순으로 정렬
temp.sort()
if len(temp)<k : #이걸 해주지 않으면 index error남
    print(0)
else :
    print(temp[k-1])
