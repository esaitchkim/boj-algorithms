"""1932.py
Title: The Triangle
Url: https://www.acmicpc.net/problem/1932
"""

import sys

input = sys.stdin.readline

n = int(input())

tri_res = [0]
for _ in range(n):
    line = [*map(int, input().split())]
    for i in range(len(line)):
        if i == 0:
            line[i] += tri_res[i]
        elif i == len(line) - 1:
            line[i] += tri_res[i - 1]
        else:
            line[i] += max(tri_res[i - 1], tri_res[i])
    tri_res = line

print(max(tri_res))
