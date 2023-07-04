import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

while True:
  s = 0
  m = 0
  l = 0

  a = input().strip()

  for i in a:
    if i == '(':
      s += 1
    if i == ')':
      s -= 1
      if s < 0:
        print('no')
        break
    if i == '{':
      m += 1
    if i == '}':
      m -= 1
      if s < 0:
        print('no')
        break
    if i == '[':
      m += 1
    if i == ']':
      m -= 1
      if s < 0:
        print('no')
        break
  if a == ".":
    break
  elif s == 0 and m == 0 and l == 0:
    print('yes')
  else:
    print('no')
