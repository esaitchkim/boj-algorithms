"""6186.py
Title: Best Grass
Url: https://www.acmicpc.net/problem/6186
"""

import sys

input = sys.stdin.readline
R, C = map(int, input().split())

grass = []
visited = [[True for _ in range(C)] for _ in range(R)]
cnt = 0

for _ in range(R):
    line = input().strip()
    grass.append(line)


for x in range(R):
    y = 0
    while y < C:
        if visited[x][y]:
            visited[x][y] = False
            if grass[x][y] == "#":
                if y < C - 1 and grass[x][y + 1] == "#":
                    visited[x][y + 1] = False
                if x < R - 1 and grass[x + 1][y] == "#":
                    visited[x + 1][y] = False
                cnt += 1
        y += 1

print(cnt)
