"""4344.py
Title: Above Average
Url: https://www.acmicpc.net/problem/4344
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

C = int(input())

for _ in range(C):
    N, *scores = map(int, input().split())
    average = sum(scores) / N
    cnt = sum([1 for score in scores if score > average])
    print(f"{100*cnt/N:.03f}%\n")
