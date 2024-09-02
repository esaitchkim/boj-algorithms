"""11660.py
Title: 구간 합 구하기 5
Url: https://www.acmicpc.net/problem/11660
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    line = [*map(int, input().split())]
    for j in range(len(line)):
        matrix[i][j + 1] = matrix[i - 1][j + 1] + matrix[i][j] + line[j] - matrix[i - 1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = matrix[x2][y2] + matrix[x1 - 1][y1 - 1] - matrix[x2][y1 - 1] - matrix[x1 - 1][y2]
    print(f"{result}\n")
