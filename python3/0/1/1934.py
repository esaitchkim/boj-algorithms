"""1934.py
Title: 최소공배수
Url: https://www.acmicpc.net/problem/1934
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    a, b = max(A, B), min(A, B)
    r = 1
    while b != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    lcm = A * B // gcd
    print(f"{lcm}\n")
