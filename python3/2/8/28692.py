"""28692.py
Title: 선형 회귀는 너무 쉬워 2
Url: https://www.acmicpc.net/problem/28692
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
Sx = 0
Sy = 0
Sxx = 0
Sxy = 0

for _ in range(n):
    x, y = map(int, input().split())
    Sx += x
    Sy += y
    Sxx += x**2
    Sxy += x * y

if Sx**2 != n * Sxx:
    a2 = (n * Sxy - Sx * Sy) / (n * Sxx - Sx**2)
    b2 = (Sy - a2 * Sx) / n
    print(f"{a2} {b2}\n")
else:
    print("EZPZ\n")
