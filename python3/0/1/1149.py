"""1149.py
Title: RGB거리
Url: https://www.acmicpc.net/problem/1149
"""

import sys

input = sys.stdin.readline

N = int(input())
houses = []

for _ in range(N):
    rgb = list(map(int, input().split()))
    houses.append(rgb)

for i in range(1, N):
    houses[i][0] += min(houses[i - 1][1], houses[i - 1][2])
    houses[i][1] += min(houses[i - 1][0], houses[i - 1][2])
    houses[i][2] += min(houses[i - 1][0], houses[i - 1][1])

min_cost = min(houses[N - 1])
print(min_cost)
