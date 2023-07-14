from itertools import combinations
tc =  int(input())

for _ in range(tc) :
    n, m = map(int, input().split())
    y = [x for x in range(1,m+1)]
    a = list(combinations(y,n))
    print(len(a))
      
