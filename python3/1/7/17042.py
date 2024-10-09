"""17042.py
Title: Elder
Url: https://www.acmicpc.net/problem/17042
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

wizard = input().rstrip()
masters = set()
masters.add(wizard)

N = int(input())

for _ in range(N):
    Z1, Z2 = input().rstrip().split()
    if Z2 == wizard:
        wizard = Z1
        masters.add(Z1)


print(f"{wizard}\n")
print(f"{len(masters)}\n")
