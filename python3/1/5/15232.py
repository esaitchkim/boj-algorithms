"""15232.py
Title: Rectangles
Url: https://www.acmicpc.net/problem/15232
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

R = int(input())
C = int(input())

for _ in range(R):
    print(f"{'*'*C}\n")
