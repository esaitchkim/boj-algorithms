"""14209.py
Title: Bridž
Url: https://www.acmicpc.net/problem/14209
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

A = 4
K = 3
Q = 2
J = 1
X = 0

N = int(input())
honor_points = 0

for _ in range(N):
    Ki = input().rstrip()
    Ki = [4 if c == "A" else 3 if c == "K" else 2 if c == "Q" else 1 if c == "J" else 0 for c in Ki]
    honor_points += sum(Ki)

print(f"{honor_points}\n")
