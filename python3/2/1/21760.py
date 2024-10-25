"""21760.py
Title: 야구 시즌
Url: https://www.acmicpc.net/problem/21760
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    N, M, k, D = map(int, input().split())
    total_match = (k * M * (M - 1) * N + N * (N - 1) * M * M) // 2
    B = D // total_match
    if B == 0:
        print(f"-1\n")
    else:
        print(f"{B*total_match}\n")
