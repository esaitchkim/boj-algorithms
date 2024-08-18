"""9461.py
Title: Padovan Sequence
Url: https://www.acmicpc.net/problem/9461
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

padovan_seq = [1] * 101
for i in range(4, 101):
    padovan_seq[i] = padovan_seq[i - 2] + padovan_seq[i - 3]

T = int(input())

for _ in range(T):
    N = int(input())
    print(f"{padovan_seq[N]}\n")
