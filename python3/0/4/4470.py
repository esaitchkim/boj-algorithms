"""4470.py
Title: Number the lines
Url: https://www.acmicpc.net/problem/4470
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

for i in range(1, N + 1):
    input_lines = input()
    input_lines = f"{i}. {input_lines}"
    print(input_lines)
