"""1388.py
Title: 바닥 장식
Url: https://www.acmicpc.net/problem/1388
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [[True for _ in range(M)] for _ in range(N)]
floor = []
cnt = 0

for _ in range(N):
    line = input().strip()
    floor.append(line)

for x in range(N):
    y = 0
    while y < M:
        if visited[x][y]:
            visited[x][y] = False
            if floor[x][y] == "-":
                z = y + 1
                while z < M:
                    if floor[x][z] == "-":
                        visited[x][z] = False
                        z += 1
                    else:
                        break
            else:
                z = x + 1
                while z < N:
                    if floor[z][y] == "|":
                        visited[z][y] = False
                        z += 1
                    else:
                        break
            cnt += 1
        y += 1

print(cnt)
