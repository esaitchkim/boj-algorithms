"""1004.py
Title: 어린 왕자
Url: https://www.acmicpc.net/problem/1004
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    res = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        d2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        r2 = r * r
        if (r2 > d1 and r2 < d2) or (r2 > d2 and r2 < d1):
            res += 1
    print(f"{res}\n")
