"""3135.py
Title: 라디오
Url: https://www.acmicpc.net/problem/3135
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

A, B = map(int, input().split())
res = abs(B - A)

N = int(input())

for _ in range(N):
    freq = int(input())
    if (abs(B - freq) + 1) < res:
        res = abs(B - freq) + 1

print(f"{res}\n")
