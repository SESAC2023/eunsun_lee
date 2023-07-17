import sys
import datetime

sys.setrecursionlimit(int(1e6))

#arr = list(map(int, input().split()))

t = datetime.datetime.utcnow()
today = t.strftime("%Y-%m-%d")
print(today)
