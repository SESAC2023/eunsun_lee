n, m = map(int, input().split())

def f(x):
  if x == 0:
    return 1
  else:
    return x * f(x - 1)

a= f(n)/f(n-m)
print(int(a/f(m)))
