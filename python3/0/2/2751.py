"""2751.py
Title: 수 정렬하기 2
Url: https://www.acmicpc.net/problem/2751
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
integers = []

for _ in range(N):
    integer = int(input())
    integers.append(integer)

integers = sorted(integers)

for num in integers:
    print(f"{num}\n")
