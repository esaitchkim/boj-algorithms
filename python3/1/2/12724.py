"""12724.py
Title: Minimum Scalar Product (Large)
Url: https://www.acmicpc.net/problem/12724
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    v1 = [*map(int, input().split())]
    v2 = [*map(int, input().split())]
    v1.sort()
    v2.sort(reverse=True)
    res = sum([v1[i] * v2[i] for i in range(n)])
    print(f"Case #{t}: {res}\n")
