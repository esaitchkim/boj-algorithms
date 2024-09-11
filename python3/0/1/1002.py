"""1002.py
Title: 터렛
Url: https://www.acmicpc.net/problem/1002
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d2 = (y2 - y1) ** 2 + (x2 - x1) ** 2
    if d2 == 0 and r1 == r2:
        print("-1\n")
    elif d2 == (r1 + r2) ** 2 or d2 == (r1 - r2) ** 2:
        print("1\n")
    elif (r1 - r2) ** 2 < d2 < (r1 + r2) ** 2:
        print("2\n")
    else:
        print("0\n")
