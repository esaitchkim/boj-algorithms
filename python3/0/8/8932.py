"""8932.py
Title: Heptathlon
Url: https://www.acmicpc.net/problem/8932
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

formulas = [
    [9.23076, 26.7, 1.835],
    [1.84523, 75, 1.348],
    [56.0211, 1.5, 1.05],
    [4.99087, 42.5, 1.81],
    [0.188807, 210, 1.41],
    [15.9803, 3.8, 1.04],
    [0.11193, 254, 1.88],
]

for _ in range(T):
    scores = [*map(int, input().split())]
    scores = [int(formulas[i][0] * abs(formulas[i][1] - scores[i]) ** formulas[i][2]) for i in range(len(scores))]
    scores = sum(scores)
    print(f"{scores}\n")
