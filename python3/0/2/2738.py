"""2738.py
Title: 행렬 덧셈
Url: https://www.acmicpc.net/problem/2738
"""

N, M = map(int, input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    lines = [*map(int, input().split())]
    for j in range(M):
        matrix[i][j] += lines[j]

for i in range(N):
    lines = [*map(int, input().split())]
    for j in range(M):
        matrix[i][j] += lines[j]

for i in range(N):
    print(*matrix[i], sep=" ")
