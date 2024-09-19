"""3063.py
Title: 게시판
Url: https://www.acmicpc.net/problem/3063
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    area1 = (x2 - x1) * (y2 - y1)
    area2 = 0

    x3 = max(x1, x3)
    x4 = min(x2, x4)
    y3 = max(y1, y3)
    y4 = min(y2, y4)

    if x3 < x4 and y3 < y4:
        area2 = (x4 - x3) * (y4 - y3)

    res = area1 - area2
    print(f"{res}\n")
