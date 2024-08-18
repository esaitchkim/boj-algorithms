"""11399.py
Title: ATM
Url: https://www.acmicpc.net/problem/11399
"""

import sys

input = sys.stdin.readline
N = int(input())
P = [*map(int, input().split())]
P.sort()
for i in range(1, len(P)):
    P[i] += P[i - 1]

print(sum(P))
