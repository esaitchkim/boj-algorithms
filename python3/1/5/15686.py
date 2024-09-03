"""15686.py
Title: 치킨 배달
Url: https://www.acmicpc.net/problem/15686
"""

import sys

input = sys.stdin.readline


def back_tracking(num_chickens, M, start=0, stack=[]):
    if len(stack) == M:
        yield stack
        return

    for i in range(start, num_chickens):
        yield from back_tracking(num_chickens, M, i + 1, stack + [i])


def get_distance(houses, chickens, stack):
    res = 0
    for house in houses:
        res += min([abs(house[0] - chickens[i][0]) + abs(house[1] - chickens[i][1]) for i in stack])
    return res


N, M = map(int, input().split())
houses = []
chickens = []

for i in range(N):
    lines = [*map(int, input().split())]
    for j in range(N):
        if lines[j] == 1:
            houses.append((i, j))
        elif lines[j] == 2:
            chickens.append((i, j))

used = [False] * len(chickens)

min_dist = 99999999

for res in back_tracking(len(chickens), M):
    min_dist = min(min_dist, get_distance(houses, chickens, res))

print(min_dist)
