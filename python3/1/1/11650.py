"""11650.py
Title: 좌표 정렬하기
Url: https://www.acmicpc.net/problem/11650
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
points = []

for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x: (x[0], x[1]))


for point in points:
    print(f"{point[0]} {point[1]}\n")
