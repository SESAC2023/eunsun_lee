import sys
import copy

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

tc = int(input())

for i in range(tc) :
    n, spell = input().split()
    n = int(n)
    spell = spell.strip()
    new_spell = spell[:n-1]+spell[n:]
    print(new_spell)
