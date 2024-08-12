"""15552.py
Title: 빠른 A+B
Url: https://www.acmicpc.net/problem/15552
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    result = A + B
    print(f"{result}\n")
