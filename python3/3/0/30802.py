"""30802.py
Title: 웰컴 키트
Url: https://www.acmicpc.net/problem/30802
"""

N = int(input())
shirts_needs = map(int, input().split())
T, P = map(int, input().split())

shirts_packs = 0
pen_packs = 0
pen_singles = 0

for s in shirts_needs:
    shirts_packs += s // T
    if s % T != 0:
        shirts_packs += 1

pen_packs = N // P
pen_singles = N % P

print(shirts_packs)
print(f"{pen_packs} {pen_singles}")
