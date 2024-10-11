"""18786.py
Title: Triangles (Bronze)
Url: https://www.acmicpc.net/problem/18786
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

fences = []
for _ in range(N):
    X, Y = map(int, input().split())
    fences.append([X, Y])

area = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or i == k or j == k:
                continue
            if fences[i][0] == fences[j][0] and fences[i][1] == fences[k][1]:
                area = max(abs(fences[i][1] - fences[j][1]) * abs(fences[i][0] - fences[k][0]), area)

print(f"{area}\n")
