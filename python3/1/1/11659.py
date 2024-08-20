"""11659.py
Title: 구간 합 구하기 4
Url: https://www.acmicpc.net/problem/11659
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

numbers = [0] + [*map(int, input().split())]
for i in range(1, len(numbers)):
    numbers[i] += numbers[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    result = numbers[j] - numbers[i - 1]
    print(f"{result}\n")
