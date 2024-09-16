"""6179.py
Title: Oh Those Rollers
Url: https://www.acmicpc.net/problem/6179
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

rollers = {}


N = int(input())
for _ in range(N):
    x, y, r = map(int, input().split())
    rollers[(x, y)] = r

stack = [(0, 0, rollers[(0, 0)])]
result = [0, 0]

while stack:
    x, y, r = stack.pop()
    if rollers.get((x, y)) is not None:
        del rollers[(x, y)]
        result = [x, y]
        for x_i, y_i in rollers.keys():
            r_i = rollers[(x_i, y_i)]
            if (x - x_i) ** 2 + (y - y_i) ** 2 == (r_i + r) ** 2:
                stack.append((x_i, y_i, r_i))
print(f"{result[0]} {result[1]}\n")
