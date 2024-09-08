"""2166.py
Title: 다각형의 면적
Url: https://www.acmicpc.net/problem/2166
"""

import sys

input = sys.stdin.readline

N = int(input())
points = []
res = 0
for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
points.append(points[0])

for i in range(N):
    res += points[i][0] * points[i + 1][1]
    res -= points[i][1] * points[i + 1][0]

tmp = abs(res) / 2
print(tmp)

res = round(abs(res) / 2, 1)
print(res)
